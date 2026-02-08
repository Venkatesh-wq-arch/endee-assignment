from sentence_transformers import SentenceTransformer

# load small fast embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert list of texts into vector embeddings
    """
    vectors = model.encode(texts)
    return vectors.tolist()
