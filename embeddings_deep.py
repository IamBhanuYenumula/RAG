from langchain_ollama.embeddings import OllamaEmbeddings
import numpy as np

embeddings = OllamaEmbeddings(model="bge-m3")
embedding = embeddings.embed_query("what is langchain?")
print(f"Dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")

norm = np.linalg.norm(embedding)
print(f"L2 Norm: {norm:.4f}")

  # Is it normalized?
is_normalized = 0.99 < norm < 1.01  # Allow small float 
print(f"Is Normalized: {is_normalized}")


def basic_embeddings():


    text = "This is a test document"
    single_embedding = embeddings.embed_query(text)
    print(f"vector dimensions: {len(single_embedding)}")
    print(f"First 5 values: {single_embedding[:5]}")
    print(f"vector norm: {np.linalg.norm(single_embedding):.4f}")

def similarity_search():
    docs = [
        "python is a programming language",
        "Javascript is used for wed development",
        "machine learning enables AI applications",
        "Deep Learning uses neural networks",
        "Cats are popular pets",
    ]

    query = "what programming language exists"

    doc_vector = embeddings.embed_documents(docs)
    query_vector = embeddings.embed_query(query)

    #compute cosine similarity
    def cosine_similarity(vec1,vec2):
        return np.dot(vec1,vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))

    similarities = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vector]

    #rank documents by similarity
    ranked_docs = sorted(zip(docs,similarities),key=lambda x:x[1], reverse=True)

    print(f"Query: {query}\n")
    print("Ranked by similarity:")
    for doc, score in ranked_docs:
        print(f" {score:.4f}: {doc}")


if __name__ == "__main__":
    similarity_search()