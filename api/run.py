import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from app import db_executor

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(HTTPSRedirectMiddleware)


@app.get("/")
async def get_task_list(user_id: int):
    markdown = db_executor.show_all_tasks(user_id=user_id)
    return {"message": markdown}


@app.post("/task")
async def get_task_list(user_id: int, task_name: str):
    db_executor.create_task(user_id=user_id, task_name=task_name)
    return {"message": 'Задача успешно создана'}


if __name__ == '__main__':
    uvicorn.run("api.run:app", host="swagger", port=8005, reload=True)
