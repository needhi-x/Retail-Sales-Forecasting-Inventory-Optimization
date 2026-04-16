import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start='2024-01-01', periods=180)

data = []

for date in dates:
    base_sales = 150
    
    # Weekend spike
    if date.weekday() >= 5:
        base_sales += 50
    
    # Seasonal variation
    seasonal = 20 * np.sin(date.dayofyear / 365 * 2 * np.pi)
    
    # Random noise
    noise = np.random.randint(-20, 20)
    
    sales = int(base_sales + seasonal + noise)
    
    data.append([date, "Milk", sales])

df = pd.DataFrame(data, columns=["date", "product", "sales"])

df.to_csv("data/raw_sales.csv", index=False)

print("Dataset generated successfully!")