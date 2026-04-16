from src.data_preprocessing import load_data, preprocess
from src.feature_engineering import create_features
from src.forecasting import train_model, forecast
from src.inventory import calculate_inventory, generate_inventory_table
from src.visualization import plot_sales

df = load_data('data/raw_sales.csv')
df = preprocess(df)
df = create_features(df)

model = train_model(df)
df = forecast(model, df)

# Inventory calculation
safety_stock, reorder_point = calculate_inventory(df)

# 👇 VERY IMPORTANT (this creates reorder_flag)
df = generate_inventory_table(df, reorder_point)

# 👇 NOW safe to print
print("\n📦 INVENTORY INSIGHTS")
print(f"Average Demand: {df['predicted_sales'].mean():.2f}")
print(f"Safety Stock: {safety_stock:.2f}")
print(f"Reorder Point: {reorder_point:.2f}")

print("\n🚨 REORDER ALERT SUMMARY")
print(df['reorder_flag'].value_counts())

plot_sales(df)

df.to_csv('outputs/forecast.csv', index=False)
df.to_csv('outputs/inventory_plan.csv', index=False)

df.to_csv('outputs/inventory.csv', index=False)
print("✅ inventory.csv saved in outputs folder")