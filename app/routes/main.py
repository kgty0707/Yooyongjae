from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.routes.load_model import Model
from app.routes.model import generate_answer


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/main")
def hello():
    return {"message": "yooyongjae"}

@router.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse(
        name="back_test.html",
        request=request
    )

@router.get("/send_query", response_class=HTMLResponse)
def send_query(request: Request, model_type: str, query: str):
    ''' TODO
    1. 모델 타입에 따른 모델 선택
    generate_answer
    '''

    model_type = Model(model_type)
    request_data = {
        'prompt': query,
        'model_type': model_type,
    }

    answer, picture = generate_answer(request_data)
    return templates.TemplateResponse(
        name="main.html",
        request=request,
        context={"answer": answer, "picture": picture}
    )

