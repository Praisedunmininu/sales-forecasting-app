# 📈 Sales Forecasting App (Streamlit + Prophet)

A simple, interactive web app that forecasts retail sales using historical data and Facebook Prophet. Built as a portfolio-ready project to demonstrate time-series forecasting, business thinking, and deployment skills.

---


## 🚀 Project Overview

**Goal:**  
Forecast future sales for a selected product category and store using historical trends.

**Built With:**
- `pandas` – data preprocessing
- `Prophet` – time-series forecasting
- `Plotly` – interactive charts
- `Streamlit` – web app interface

---


## 🌐 Try the Live App

[![🚀 Launch App](https://img.shields.io/badge/🚀%20Launch%20App-Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://salesforecastapp.streamlit.app/)
[![🔍 View Source](https://img.shields.io/badge/🔍%20View%20Source-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/Praisedunmininu/sales-forecasting-app)



## 📊 Features

- 🧼 **Data Cleaning:** Handles dates, filters by store and product family
- 📉 **Time-Series Aggregation:** Resamples data into monthly sales
- 🔮 **Forecasting:** Uses Facebook Prophet to model trends and seasonality
- 📈 **Visualization:** Forecast vs. actuals with confidence intervals (Plotly)
- 🧠 **Model Evaluation:** Mean Absolute Error (MAE) on historical fit
- 💻 **Deployment:** Streamlit app ready for demo or showcase

---

## 📂 Dataset

Source: [Kaggle – Store Sales Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)  
File used: A sample `mini_train.csv` (50KB) slice for deployment. Original full dataset is ~116MB.

---

## 🖼 App Preview

![screenshot](./assets/app-preview.png)  
*(You can upload an actual screenshot from your app into an `assets/` folder for display)*

---

## 🔧 How to Run Locally

1. **Clone the repo:**

<pre lang="markdown"> ```bash git clone https://github.com/Praisedunmininu/sales-forecasting-app.git cd sales-forecasting-app ``` </pre>

2. **Install dependencies:**

<pre lang= "markdown"> pip install -r requirements.txt </pre>

3. Run the App
<pre lang= "markdown">streamlit run app.py </pre>


 ## 🌐 Try the Live App

[![🚀 Launch App](https://img.shields.io/badge/🚀%20Launch%20App-Streamlit-brightgreen?style=for-the-badge&logo=streamlit)](https://salesforecastapp.streamlit.app/)

## 📁 Project Structure

sales-forecasting-app/

│

├── app.py                  # Streamlit app

├── requirements.txt        # App dependencies

├── .gitignore

│

├── data/

│   └── mini_train.csv      # Sample dataset (sliced for deploy)

│

├── notebook/

│   ├── eda.ipynb           # Exploratory analysis

│   └── slice_creator.py    # Script to create small CSV from full dataset

│

└── README.md               # You're reading it 😉

## 📌 Highlights

Realistic business problem (retail sales forecasting)

Clear visual storytelling with Plotly

Deployed & reproducible for employers or collaborators

Shows data science maturity: modeling, EDA, deployment

## 💡 Ideas to Improve

Use full dataset for deeper modeling

Add ARIMA or LSTM for comparison

Forecast at daily granularity

Include national holidays (already in original Kaggle dataset)

Build a dashboard with login or export

## 👋 Author

Islamiat Seriki

📍 Data Science & AI | Passionate about innovation in Africa

🔗 LinkedIn

🔗 GitHub

## 📝 License

This project is open-source and free to use for educational and showcase purposes.
