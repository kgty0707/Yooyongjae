# gpt api 관련 파일입니다.
import os
from openai import OpenAI
import deepl

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.routes.db_search import search_by_query, search_by_result
from app.routes.load_model import load_model

api_key = os.getenv('GPT_API_KEY')
api_key = os.getenv('GPT_API_KEY')
auth_key = os.getenv('DEEPL_API_KEY')

translator = deepl.Translator(auth_key)
client = OpenAI(api_key=api_key)


router = APIRouter()

pipeline = load_model()


'''
TODO
1. Prompt 구성; 교수님 말투 etc
'''


def generate_answer(request_data):

    prompt = request_data['prompt']
    model_type = request_data['model_type']
    content = search_by_query(prompt)
    if model_type == 'gpt-3.5-turbo':
        answer = gen_gpt(prompt, model_type, content)
    else:
        answer = gen_etc(prompt, content)
    
    
    picture = search_by_result(answer)
    print(answer, picture)

    return answer, picture

        
def gen_gpt(query, model_type, content):

    messages = [{
        "role": "system",
        "content": "You are a professor in korea"
    }, {
        "role": "user",
        "content": f"Write in the tone of a professor speaking to students and Please write in Korean. \nquestion: {query} \ninformation: {content} "
    }]

    print('prompt: ', messages)
    response = client.chat.completions.create(
        model=model_type,
        messages=messages,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message


def gen_etc(query, content):
    query_result = translator.translate_text(query, target_lang="EN-US")
    content_result = translator.translate_text(content, target_lang="EN-US")

    completion = pipeline(
        (
            f"""
            <s>INSTRUCTION: You are a professor in College of Engineering.
            INFORMATION: {content_result}
            INPUT: {query_result} Write like a professor.
            OUTPUT:
            """
        ),
        return_full_text=False,
        max_new_tokens=256,
    )

    completion = completion[0]['generated_text']
    result = translator.translate_text(completion, target_lang="KO")

    return result.text
