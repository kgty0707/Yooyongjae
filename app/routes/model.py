# gpt api 관련 파일입니다.
import os
import openai
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.routes.db_search import search_by_query, search_by_result

api_key = os.getenv('GPT_API_KEY')
openai.api_key = os.getenv('API_KEY')

origin_path = "./APP/AI/dataset/image_data/"

router = APIRouter()

'''
TODO
1. Prompt 구성; 교수님 말투 etc
'''


class PromptRequest(BaseModel):
    prompt: str


async def generate_answer(request_data: PromptRequest):
    result = {}

    prompt = request_data.prompt
    model_type = request_data.model_type
    content = search_by_query(prompt)
    answer = rag_prompt(prompt, model_type, content)
    
    picture = origin_path + search_by_result(answer)

    return answer, picture


async def rag_prompt(query, model_type, content):
    # TODO
    # 현재는 GPT 모델로 설정되어 있음
    # 모델 타입에 따른 분기 설정
    try:
        response = await openai.ChatCompletion.create(
            model=model_type,
            messages=[
                {
                    "role": "system",
                    "content": "instruction"},
                {
                    "role": "user",
                    "content": f'''

                    # 예시 5개 보여주기
                    Emotion example list: 웃고있는_행복한_안경을쓰고있는.png

                    document: {content}
                    question: {query}

                    answer:
                    '''
                 }
            ],
            max_tokens=3000,
            stop=None,
            temperature=0.5
        )
        answer = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return answer