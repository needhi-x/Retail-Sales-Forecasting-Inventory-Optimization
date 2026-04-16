import matplotlib.pyplot as plt

def plot_sales(df):
    plt.figure(figsize=(10,5))
    
    plt.plot(df['date'], df['sales'], label='Actual Sales')
    plt.plot(df['date'], df['predicted_sales'], label='Forecasted Sales')
    
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Retail Sales Forecasting")
    plt.legend()
    
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('images/forecast.png')
    plt.show()