import pandas as pd

def load_data(path="data/finance_data.csv"):
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def calculate_metrics(df):
    df["Savings"] = df["Income"] - df["Expense"]
    df["Savings_Rate"] = (df["Savings"] / df["Income"]) * 100

    total_income = df["Income"].sum()
    total_expense = df["Expense"].sum()
    total_savings = df["Savings"].sum()
    avg_savings_rate = df["Savings_Rate"].mean()

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "total_savings": total_savings,
        "avg_savings_rate": avg_savings_rate
    }

def financial_stability(avg_savings_rate):
    if avg_savings_rate >= 30:
        return "Stable"
    elif avg_savings_rate >= 15:
        return "Moderate"
    else:
        return "Risk"

