# gpt api 관련 파일입니다.
import os
import openai
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from app.routes.db_search import search_by_query, search_by_emotion

api_key = os.getenv('GPT_API_KEY')
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
    
    # TODO
    # Emotion과 Answer Filter
    lines = answer.strip().split('\n')
    for line in lines:
        if ': ' in line:
            key, value = line.split(': ', 1)
            result[key.strip()] = value.strip()
    # Emotion은 Picture Vector Search 후 Picture 반환
    picture = search_by_emotion(result['emotion'])

    return result['answer'], picture


async def rag_prompt(query, model_type, content):
    openai.api_key = os.getenv('API_KEY')
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
                    emotion:
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