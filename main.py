from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID, uuid4,uuid5
app=FastAPI()
class Task(BaseModel):
    id:Optional[UUID]=None
    title:str
    desc:Optional[str]
    completedStatus:bool=False

tasks=[]

@app.post("/tasks/",response_model=Task)
def add_task(task:Task):
    task.id=uuid4()
    tasks.append(task)
    return task
    

@app.get("/")
def read():
    return {"Fast API"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    