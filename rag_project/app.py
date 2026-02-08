import json
import math
from embeddings import embed

DB_FILE = "vector_db.json"

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    return dot / (na * nb)

# load vector DB
db = json.load(open(DB_FILE, "r", encoding="utf-8"))

def rag_answer(question):
    qv = embed([question])[0]

    scores = []
    for r in db:
        s = cosine(qv, r["vector"])
        scores.append((s, r["text"]))

    scores.sort(reverse=True)

    context = " ".join(t for _, t in scores[:2])

    answer = f"""
Retrieved Context:
{context}

Generated Answer:
Based on the retrieved knowledge, {context}
"""
    return answer


q = input("Ask a question: ")
print(rag_answer(q))
