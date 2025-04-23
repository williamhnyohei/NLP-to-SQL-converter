from sqlalchemy import create_engine, text
import pandas as pd

def is_safe_sql(sql: str) -> bool:
    forbidden = ["DROP", "DELETE", "ALTER", "TRUNCATE", "UPDATE"]
    return not any(word in sql.upper() for word in forbidden)

def run_query(db_uri: str, sql: str, as_json=False, as_csv=False, as_html=False):
    engine = create_engine(db_uri)
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    if as_json:
        return df.to_dict(orient="records")
    if as_csv:
        return df.to_csv(index=False)
    if as_html:
        return df.to_html(index=False)

    return df
