from src.data_preprocessing import load_data
from src.model import train_simple_model
from src.forecast import predict_future

def main():
    df = load_data("data/expenses.csv")
    model = train_simple_model(df)
    preds = predict_future(model, df, periods=3)
    print("Next 3 predicted expenses:", preds)

if __name__ == "__main__":
    main()

