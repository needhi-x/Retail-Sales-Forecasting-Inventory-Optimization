def create_features(df):
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['week'] = df['date'].dt.isocalendar().week
    
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    
    df.fillna(0, inplace=True)
    return df