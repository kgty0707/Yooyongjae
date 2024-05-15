import transformers
import deepl
import time
import os

auth_key = os.getenv('DEEPL_API_KEY')

translator = deepl.Translator(auth_key)

model = transformers.AutoModelForCausalLM.from_pretrained(
    'player1537/Dolphinette',
)

tokenizer = transformers.AutoTokenizer.from_pretrained(
    'player1537/Dolphinette',
)

pipeline = transformers.pipeline(
    'text-generation',
    model=model,
    tokenizer=tokenizer,
)

# TODO User Query도 한국어로 변환
# TODO INFORMATION도 영어 번역본 준비 해야 됨
# 위 모델 사용할 경우 emotion을 추출하기 보다 답변에 따른 벡터 서치를 통해 사진을 추출해야함

start_time = time.time()

query = "교수님의 생일은 언제야?"
query_result = translator.translate_text(query, target_lang="EN-US")

print(query_result)

content = "교수님의 생일은 7월 25일이라고 학생들이 말합니다."
content_result = translator.translate_text(content, target_lang="EN-US")
print(content_result)
# completion = pipeline(
#     (
#         r"""<s>INSTRUCTION: You are an AI assistant that helps people find"""
#         r"""information. INPUT: Answer this question: what is the capital of"""
#         r"""France? Be concise. OUTPUT:"""
#     ),
#     return_full_text=False,
#     max_new_tokens=512,
# )

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
    max_new_tokens=512,
)

completion = completion[0]['generated_text']

print(completion)


result = translator.translate_text(completion, target_lang="KO")
print(result.text)

end_time = time.time()
print(end_time - start_time)