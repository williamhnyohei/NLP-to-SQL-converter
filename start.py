import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app

load_dotenv()

schema = """
Tabela: vendas
Colunas:
- id (INTEGER)
- produto (TEXT)
- quantidade (INTEGER)
- preco (REAL)
- data (TEXT)
"""

question = "Qual o total de vendas por produto?"
db_uri = os.getenv("DATABASE_URI")
api_key = os.getenv("OPENAI_API_KEY")
return_format = os.getenv("RETURN_FORMAT", "json")

client = TestClient(app)
response = client.post("/consultar", json={
    "schema": schema,
    "question": question,
    "db_uri": db_uri,
    "openai_key": api_key,
    "return_format": return_format
})

print("Status:", response.status_code)
print("Resposta:", response.json())
