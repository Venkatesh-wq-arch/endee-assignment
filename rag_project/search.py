import json
import math
from embeddings import embed

DB_FILE = "vector_db.json"

def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    return dot / (na * nb)

print("Loading vector database...")
db = json.load(open(DB_FILE, "r", encoding="utf-8"))

query = input("Enter your search question: ")

qv = embed([query])[0]

scores = []
for r in db:
    s = cosine(qv, r["vector"])
    scores.append((s, r["text"]))

scores.sort(reverse=True)

print("\nTop semantic matches:\n")
for s, t in scores[:3]:
    print("-", t)
