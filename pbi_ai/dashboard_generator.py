from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_dashboard_plan(user_prompt):
    system_prompt = """
You are a Power BI expert.

Convert user request into:
1. DAX measures (multiple)
2. Dashboard structure plan

Rules:
- Return simple JSON format
- Assume table = Sales
- Assume column = Amount
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content