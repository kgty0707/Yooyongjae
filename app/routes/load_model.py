from fastapi.responses import JSONResponse

# TODO
# 1. GPT 이외에 모델 로드
# 2. 모델 타입에 따른 모델 선택

def load_model():
    '''
    1. GPT 이외에 모델 로드
    - 페이지 로딩 되자마자 로드 시작
    '''
    ...


class Model:
    def __init__(self, model_type):
        self.model_type = model_type

    def model_type(self):
        if self.model_type == 'GPT-3.5':
            return self.model_type
        
        elif self.model_type == 'etc':
            return self.model_type
        
        else:
            return JSONResponse(content={'Error': 'Please Select Model.'})