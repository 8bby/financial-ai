from openai import OpenAI
import json

client = OpenAI()

def extract_financials(text):
    prompt = f"""
Extract these financial metrics from the text.

Return ONLY valid JSON.

Fields:
- revenue
- net_income
- ebitda
- gross_profit
- cash_balance

If not found, return null.

TEXT:
{text[:4000]}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract financial data."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
