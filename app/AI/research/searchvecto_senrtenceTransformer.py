from sentence_transformers import SentenceTransformer
import os
from pinecone import Pinecone, ServerlessSpec

pinecone_key = os.getenv('PINECONE_API_KEY')
pc = Pinecone(api_key=pinecone_key)

index = pc.Index("yoo")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Pinecone 인덱스 초기화
index = pc.Index("yoo")
file_path = ".\APP\AI\dataset\crawling_data\yoo.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# 각 텍스트 라인의 ID 생성
ids = [str(x) for x in range(len(data))]
embedded_datas = model.encode(data).tolist()
meta_datas =[{'text':text} for text in data]

records = zip(ids,embedded_datas, meta_datas)
index.upsert(vectors=records)

def make_query(query):
    # Create the query vector using the model
    xq = model.encode(query).tolist()

    # Now query the Pinecone index using keyword arguments
    xc = index.query(vector=xq, top_k=5, include_metadata=True)

    # Extract results
    result = [{'score': match['score'], 'text': match['metadata']['text']} for match in xc['matches']]
    return result

# Example usage
response = make_query("월요일 3시 뭐하셔?")
print(response)