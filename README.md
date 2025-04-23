# NLP-to-SQL-converter

A FastAPI-based service that converts natural language questions into executable SQL queries using OpenAI, with SQL safety validation and multi-format output.

---

## 🔎 Overview
This project enables developers and analysts to query relational databases using plain English or any other language. By providing the database schema and a user question, the API returns the corresponding SQL statement and executes it, returning the result.

---

## 🌐 Features
- ✍️ Natural language to SQL conversion (via OpenAI API)
- ⚡ FastAPI-powered REST endpoint
- ✅ SQL safety validation (blocks DROP, DELETE, ALTER...)
- ♻ Supports SQLite, PostgreSQL, MySQL
- 📄 Output formats: JSON, CSV, HTML
- ⚙ Ready for production deployment or integration

---

## 🚀 Quick Start

### ▶️ Option 1: Use as a Python module
You can directly import and use the library in your Python scripts:

```python
from nlp2sql import generate_sql, run_query, is_safe_sql

schema = """
Tabela: vendas
Colunas:
- id (INTEGER)
- produto (TEXT)
- quantidade (INTEGER)
- preco (REAL)
- data (TEXT)
"""

question = "Qual o total vendido por produto?"
db_uri = "sqlite:///example.db"
openai_key = "sk-..."

sql = generate_sql(question, schema, openai_key)

if is_safe_sql(sql):
    result = run_query(db_uri, sql, as_json=True)
    print(result)
else:
    print("Unsafe SQL detected")
```

### 🌐 Option 2: Run the API server

#### 1. Clone the repository
```bash
git clone https://github.com/williamhnyohei/NLP-to-SQL-converter.git
cd NLP-to-SQL-converter
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Configure environment
Rename the example:
```bash
cp .env.example .env
```
Fill in your OpenAI key and database URI.

#### 4. Run the API
```bash
uvicorn app.main:app --reload
```

Access documentation at: `http://localhost:8000/docs`

---

## 📊 Example Request
### POST /consultar
```json
{
  "schema": "Tabela: vendas\nColunas:\n- id (INTEGER)\n- produto (TEXT)\n- quantidade (INTEGER)\n- preco (REAL)\n- data (TEXT)",
  "question": "Qual o total vendido por produto?",
  "db_uri": "sqlite:///example.db",
  "openai_key": "sk-...",
  "return_format": "json"
}
```

---

## 📅 Roadmap
- [x] SQL safety validation
- [x] Multi-format support
- [ ] Local GEN IA for Data Safety
- [ ] Web interface
- [ ] Integration with vector DB for semantic querying

---

## ✍️ License
This project is licensed under the MIT License.

---

## 🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📖 Acknowledgments
Built with OpenAI, SQLAlchemy, FastAPI, and love by [@williamhnyohei](https://github.com/williamhnyohei)
