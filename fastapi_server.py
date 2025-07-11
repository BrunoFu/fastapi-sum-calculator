# fastapi_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 添加CORS中间件，允许前端调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义接收数据的数据结构
class Numbers(BaseModel):
    a: int
    b: int

@app.post("/sum")
def calculate_sum(data: Numbers):
    result = data.a + data.b
    return {"sum": result}

# 添加一个简单的根路径，方便测试
@app.get("/")
def read_root():
    return {"message": "FastAPI 服务正在运行！访问 /docs 查看 API 文档"} 