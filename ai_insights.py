import openai

def generate_ai_insights(summary_text, api_key):
    openai.api_key = api_key

    prompt = f"""
    You are a financial data analyst.
    Analyze the following financial summary and explain the user's
    financial stability in simple, clear language.
    Give practical suggestions. No investment advice.

    Data Summary:
    {summary_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

