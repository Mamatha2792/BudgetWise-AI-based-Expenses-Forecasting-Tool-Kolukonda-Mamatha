
from sklearn.linear_model import LinearRegression

def train_simple_model(df):
    X = df[['month_index']].values
    y = df['expense'].values
    model = LinearRegression()
    model.fit(X, y)
    return model
