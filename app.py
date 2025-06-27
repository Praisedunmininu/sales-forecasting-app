# app.py – Streamlit Sales Forecast

import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Sales Forecast", layout="wide")
st.title("📈 Sales Forecasting Demo (Prophet)")

@st.cache_data
def load_data():
    csv_path = Path("data/train.csv")
    df = pd.read_csv(csv_path, parse_dates=["date"])
    return df

raw = load_data()


with st.expander("See raw data preview"):
    st.write(raw.head())


# Sidebar Filters
st.sidebar.header("🔧 Filters")

store_ids = sorted(raw["store_nbr"].unique())
families = sorted(raw["family"].unique())

store_choice = st.sidebar.selectbox("Store number", store_ids, index=0)
family_choice = st.sidebar.selectbox("Product family", families, index=families.index("GROCERY I") if "GROCERY I" in families else 0)
months_ahead = st.sidebar.slider("Forecast horizon (months)", 3, 12, 6)

#Prepare the time-series

@st.cache_data  # re-runs only if filters change
def make_monthly(df, store, family):
    filt = df[(df["store_nbr"] == store) & (df["family"] == family)]
    monthly = (filt
               .set_index("date")
               .resample("M")
               .agg({"sales": "sum"})
               .reset_index())
    return monthly

monthly = make_monthly(raw, store_choice, family_choice)
st.write(monthly.head())

# Train Prophet & forecast

@st.cache_resource  # expensive ⇒ keep in memory while filters unchanged
def train_prophet(hist_df):
    dfp = hist_df.rename(columns={"date": "ds", "sales": "y"})
    m = Prophet()
    m.fit(dfp)
    return m

model = train_prophet(monthly)

future   = model.make_future_dataframe(periods=months_ahead, freq="M")
forecast = model.predict(future)


# Buid interactive Plotly chart
# Separate past & future rows for colouring
cutoff = monthly["date"].max()

fig = go.Figure()

# Actuals
fig.add_trace(go.Scatter(x=monthly["date"],
                         y=monthly["sales"],
                         mode="lines+markers",
                         name="Actual"))

# Forecast
fig.add_trace(go.Scatter(x=forecast["ds"],
                         y=forecast["yhat"],
                         mode="lines",
                         line=dict(dash="dash"),
                         name="Forecast"))

# Uncertainty band
fig.add_trace(go.Scatter(
    x=pd.concat([forecast["ds"], forecast["ds"][::-1]]),
    y=pd.concat([forecast["yhat_upper"], forecast["yhat_lower"][::-1]]),
    fill="toself",
    fillcolor="rgba(0,100,80,0.2)",
    line=dict(color="rgba(255,255,255,0)"),
    hoverinfo="skip",
    name="Confidence"
))

fig.update_layout(title=f"Store {store_choice} – {family_choice}",
                  xaxis_title="Date",
                  yaxis_title="Sales")

st.plotly_chart(fig, use_container_width=True)

#Show quick metrics
from sklearn.metrics import mean_absolute_error

# Error on history
merged = monthly.merge(forecast[["ds", "yhat"]], left_on="date", right_on="ds", how="left")
mae  = mean_absolute_error(merged["sales"], merged["yhat"])
st.metric("Mean Absolute Error (history)", f"${mae:,.0f}")

