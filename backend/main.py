from fastapi import FastAPI
from chain import query_sre_logs

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = query_sre_logs(q)
    return {"question": q, "answer": answer}
