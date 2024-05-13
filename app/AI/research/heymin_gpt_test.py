import os
import time
from openai import OpenAI

api_key = os.getenv('GPT_API_KEY')

client = OpenAI(api_key=api_key)

# def get_response(info):
#     retry_delay = 1  # start with a 1 second delay
#     while True:
#         try:
#             response = openai.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system",
#                      "content": "You are Yoo Yong-jae, an assistant professor at Hanyang University's School of Artificial Intelligence and Convergence in Korea. Write in Korean with the tone of a professor."},
#                     {"role": "user",
#                      "content": 
#                      f"""
#                         information: {info}
#                         question(by student): What's the professor doing next week?
#                      """},
#                 ]
#             )
#             return response['choices'][0]['message']['content']
#         except openai.RateLimitError as e:
#             print(f"Rate limit exceeded, retrying in {retry_delay} seconds...")
#             time.sleep(retry_delay)
#             retry_delay *= 2  # Exponential backoff
#         except openai.OpenAIError as e:
#             print(f"An error occurred: {e}")
#             break

# info = "교수님은 다음주에 이크라 학회 출장을 간다."
# response_content = get_response(info)
# print(response_content)


model = "gpt-3.5-turbo"

# 질문 작성하기
query = "텍스트를 이미지로 그려주는 모델에 대해 알려줘."

# 메시지 설정하기
messages = [{
    "role": "system",
    "content": "You are a helpful assistant."
}, {
    "role": "user",
    "content": query
}]

response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
response_message = response.choices[0].message.content
print(response_message)