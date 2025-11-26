def retrieve_relevant_chunks(query_embedding, collection, top_k=3):
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    return results
