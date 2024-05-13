from pinecone import Pinecone
from openai import OpenAI
import os

api_key = os.getenv('GPT_API_KEY')
pinecone_key = os.getenv('PINECONE_API_KEY')
client = OpenAI(api_key=api_key)
pc = Pinecone(api_key=pinecone_key)

index = pc.Index("yoo-img")

question = "웃는 얼굴"

embedding = client.embeddings.create(
    model ="text-embedding-3-small",
    input = question
).data[0].embedding

query_result=index.query(
  vector=embedding,
  top_k=1,
  include_values=False,
  include_metadata=True
)

for result in query_result.matches:
  id = result.id
  text = result.metadata['text']
  score = result.score
  print(id,score,text)