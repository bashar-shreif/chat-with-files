import os

from dotenv import load_dotenv

from .call_llm import generate_answer
from .chunnker import chunk_documents
from .embedder import embed_texts
from .loader import load_documents_from_folder
from .prompt import prepare_prompt
from .similarity import retrieve_relevant_chunks
from .vector_db import get_db_collection

load_dotenv()


def process_rag(source_directory, user_question):
    source_list = load_documents_from_folder(source_directory)
    my_chunks = chunk_documents(source_list)
    ids_list = [f"chunk_{i}" for i in range(len(my_chunks))]
    text_list = []
    metadata_list = []
    for chunk in my_chunks:
        text_list.append(chunk["text"])
        metadata_list.append(
            {
                "source": chunk["source"],
                "doc_id": chunk["doc_id"],
                "chunk_id": chunk["chunk_id"],
            }
        )
    vectors_list = embed_texts(text_list)
    my_rag_collection = get_db_collection()
    my_rag_collection.upsert(
        ids=ids_list,
        embeddings=vectors_list,
        documents=text_list,
        metadatas=metadata_list,
    )
    question_list = [user_question]
    question_vector = embed_texts(question_list)
    result = retrieve_relevant_chunks(question_vector, my_rag_collection, 3)
    my_prompt = prepare_prompt(user_question, result["documents"][0])
    answer = generate_answer(my_prompt, os.getenv("DEEPSEEK_API_KEY"))
    return answer
