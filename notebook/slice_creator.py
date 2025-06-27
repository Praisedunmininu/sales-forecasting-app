import pandas as pd
from pathlib import Path

# Load full dataset
df = pd.read_csv("C:/Users/DELL/Desktop/sales-forecastiing-app/data/train.csv", parse_dates=["date"])


# Show all available product families (optional)
print("Available families:", df['family'].unique())

# Filter: Only Store 1 and GROCERY I family
filtered = df[
    (df["store_nbr"] == 1) &
    (df["family"].isin(["GROCERY I", "BEVERAGES"]))
]

# Optionally: Keep only a limited time range (e.g., 2016-2017)
filtered = filtered[filtered["date"] >= "2016-01-01"]

# Save the sliced version
output_path = Path("data/mini_train.csv")
filtered.to_csv(output_path, index=False)

print("✅ Slice created:", output_path, "| Rows:", len(filtered))
