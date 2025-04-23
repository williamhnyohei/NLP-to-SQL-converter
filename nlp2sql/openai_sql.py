import openai

def generate_sql(question: str, schema: str, api_key: str) -> str:
    openai.api_key = api_key
    prompt = f"""
Você é um assistente SQL. Gere uma consulta SQL baseada no schema e na pergunta abaixo. Responda apenas com código SQL válido.

Schema:
{schema}

Pergunta:
{question}

SQL:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()
