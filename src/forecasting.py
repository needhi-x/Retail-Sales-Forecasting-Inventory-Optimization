from sklearn.linear_model import LinearRegression

def train_model(df):
    features = ['day', 'month', 'week', 'lag_1', 'lag_7']
    X = df[features]
    y = df['sales']
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def forecast(model, df):
    features = ['day', 'month', 'week', 'lag_1', 'lag_7']
    df['predicted_sales'] = model.predict(df[features])
    return df