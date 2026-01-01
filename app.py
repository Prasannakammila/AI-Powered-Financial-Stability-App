import streamlit as st
import matplotlib.pyplot as plt

from analysis import load_data, calculate_metrics, financial_stability
from ai_insights import generate_ai_insights

# Page config
st.set_page_config(
    page_title="AI-Driven Financial Stability Analyzer",
    layout="wide"
)

st.title("AI-Driven Financial Stability Analyzer")

# Load and analyze data
df = load_data()
metrics = calculate_metrics(df)
status = financial_stability(metrics["avg_savings_rate"])

# KPI Section
col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"₹{metrics['total_income']}")
col2.metric("Total Expense", f"₹{metrics['total_expense']}")
col3.metric("Total Savings", f"₹{metrics['total_savings']}")

# Financial Status
st.subheader("Financial Health Status")
st.info(f"Your financial status is: **{status}**")

# Monthly Expense Trend
st.subheader("Monthly Expense Trend")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Expense"])
ax.set_xlabel("Month")
ax.set_ylabel("Expense")
st.pyplot(fig)

# Category-wise Expense
st.subheader("Category-wise Expenses")
category_data = df.groupby("Category")["Expense"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(category_data.index, category_data.values)
ax2.set_ylabel("Total Expense")
st.pyplot(fig2)

# ---------------- AI INSIGHTS SECTION ----------------

st.subheader("AI Financial Insights")

api_key = st.text_input("Enter OpenAI API Key", type="password")

if api_key:
    summary = f"""
    Total Income: {metrics['total_income']}
    Total Expense: {metrics['total_expense']}
    Total Savings: {metrics['total_savings']}
    Average Savings Rate: {metrics['avg_savings_rate']:.2f}%
    Financial Status: {status}
    """

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing financial stability..."):
            insights = generate_ai_insights(summary, api_key)
            st.success("AI Analysis Complete")
            st.write(insights)

