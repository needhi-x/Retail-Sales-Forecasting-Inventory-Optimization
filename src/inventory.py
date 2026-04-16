import numpy as np
import pandas as pd

def calculate_inventory(df, lead_time=7, service_level=1.65):
    
    avg_demand = df['predicted_sales'].mean()
    std_dev = df['predicted_sales'].std()
    
    safety_stock = service_level * std_dev * np.sqrt(lead_time)
    reorder_point = (avg_demand * lead_time) + safety_stock
    
    return safety_stock, reorder_point


def generate_inventory_table(df, reorder_point):
    
    df['current_stock'] = df['predicted_sales'] * 1.2
    
    df['reorder_flag'] = df['current_stock'].apply(
        lambda x: "YES" if x < reorder_point else "NO"
    )
    
    return df