import json
from embeddings import embed

DATA_FILE = "data.txt"
DB_FILE = "vector_db.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

print("Loading data...")
texts = load_data()

print("Creating embeddings...")
vectors = embed(texts)

records = []
for text, vec in zip(texts, vectors):
    records.append({
        "text": text,
        "vector": vec
    })

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(records, f)

print("✅ Ingestion complete — vector_db.json created")
