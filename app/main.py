# 원 페이지로 작동하는 라우터를 구현하는 파일입니다.

from fastapi import FastAPI, Depends, Path, HTTPException

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "yooyongjae"}