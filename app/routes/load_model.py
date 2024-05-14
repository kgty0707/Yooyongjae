import transformers

from fastapi.responses import JSONResponse

# TODO
# 1. GPT 이외에 모델 로드
# 2. 모델 타입에 따른 모델 선택

def load_model():
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

    return pipeline


class Model:
    def __init__(self, model_type):
        self.model_type = model_type

    def get_model_type(self):
        if self.model_type == 'gpt-3.5-turbo':
            return self.model_type
        elif self.model_type == 'player1537/Dolphinette':
            return self.model_type
        else:
            return JSONResponse(content={'Error': 'Please Select Model.'})
