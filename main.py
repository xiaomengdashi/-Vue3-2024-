from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn

app = FastAPI() 

origins = [
    "http://localhost", 
    "http://localhost:4173", 
    "http://localhost:9090", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=[""],
    allow_headers=[""],
)


@app.get("/api/v1/login/code") 
def code():
    data = { 
    "code": 0,
    "data": "http://dummyimage.com/100x40/dcdfe6/000000.png&text=V3Admin", 
    "message": "获取验证码成功"
    }

    return data

class UserInfo(BaseModel):
    code: str 
    password: str
    username: str


@app.post("/api/v1/users/login") 
def login(userinfo: UserInfo):
    print(userinfo)
    if userinfo.code == "V3Admin" and userinfo.username=="admin" and userinfo.password=="12345678": 
        result = {
            "code": 0, 
            "data": {
                "token": "token-admin" 
                },
                "message":"登录成功" 
            }
    else: 
        result = {
            "code": 400,
            "message":"登录失败" 
        }
        
    return result


@app.get("/api/v1/users/info") 
def info():
    result={
        "code": 0, 
        "data": {
            "username": "admin", 
            "roles": ["admin"] 
        },
        "message": "获取用户详情成功"
    }

    return result
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3333)
    print(123)