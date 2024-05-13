# 모든 데이터를 저장하고, 디비 서치를 하는 파일입니다.
# 사진 이름을 디비에 넣어서 벡터 서치 후 반환
from pinecone import Pinecone
from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

api_key = os.getenv('GPT_API_KEY')
info_key = os.getenv('INFO_API_KEY')
img_key = os.getenv('IMG_API_KEY')

client = OpenAI(api_key=api_key)
info_pc = Pinecone(api_key=info_key)
img_pc = Pinecone(api_key=img_key)

def search_by(index, query):

    embedding = client.embeddings.create(
        model ="text-embedding-3-small",
        input = query
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

    return text


def search_by_query(query):
    ''' TODO
    사용자 질문을(query) 기반으로 벡터 서치 후
    정보 1개 반환
    '''
    index = info_pc.Index("yoo")
    result = search_by(index, query)
    
    return result


def search_by_result(answer):
    ''' TODO
    사용자 감정을(emotion) 기반으로 벡터 서치 후
    db에 있는 사진 중 가장 유사한 사진 1개를 반환
    '''
    index = img_pc.Index("yoo-img")
    result = search_by(index, answer)

    return result