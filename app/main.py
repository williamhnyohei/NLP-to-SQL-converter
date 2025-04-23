from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlp2sql import generate_sql, run_query, is_safe_sql

app = FastAPI()

class QueryRequest(BaseModel):
    schema: str
    question: str
    db_uri: str
    openai_key: str
    return_format: str = "json"  # json, csv, html

@app.post("/consultar")
def consultar(request: QueryRequest):
    sql = generate_sql(request.question, request.schema, request.openai_key)
    if not is_safe_sql(sql):
        raise HTTPException(status_code=400, detail="SQL perigoso detectado")

    if request.return_format == "json":
        result = run_query(request.db_uri, sql, as_json=True)
    elif request.return_format == "csv":
        result = run_query(request.db_uri, sql, as_csv=True)
    elif request.return_format == "html":
        result = run_query(request.db_uri, sql, as_html=True)
    else:
        raise HTTPException(status_code=400, detail="Formato inválido")
    
    return {"sql": sql, "resultado": result}
