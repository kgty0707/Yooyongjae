# gpt api 관련 파일입니다.
import os
import openai
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv

api_key = os.getenv('GPT_API_KEY')
router = APIRouter()

'''
TODO
Prompt 구성;
교수님 말투
'''

class PromptRequest(BaseModel):
    prompt: str

@router.post('/prompt')
async def generate_answer(request_data: PromptRequest):
    prompt = request_data.prompt
    openai.api_key = os.getenv('API_KEY')
    pre_prompt = "한국어로 친절하게 대답해줘 :)\n\n"
    try:
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": pre_prompt + prompt}
            ],
            max_tokens=3000,
            stop=None,
            temperature=0.5
        )
        answer = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse(content={'answer': answer})
