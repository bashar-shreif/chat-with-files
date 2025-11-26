def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk.strip())
        start = end - overlap  # Create overlap

    return chunks


def chunk_documents(documents, chunk_size=500, overlap=50):
    all_chunks = []

    for doc_idx, doc in enumerate(documents):
        chunks = chunk_text(doc["content"], chunk_size, overlap)
        for chunk_idx, chunk in enumerate(chunks):
            all_chunks.append(
                {
                    "text": chunk,
                    "source": doc["source"],
                    "doc_id": doc_idx,
                    "chunk_id": chunk_idx,
                    "chunk_length": len(chunk),
                }
            )

    return all_chunks
