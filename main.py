from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    complete: bool = False

# get all todos
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos

# get a single todo
@app.get('/todo/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

# create a new todo
@app.post('/todo', response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# update an existing todo
@app.put('/todo/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, update_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = update_todo
            return update_todo
    raise HTTPException(status_code=404, detail='Todo not found')

@app.delete('/todo/{todo_id}')
def delete(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {'message': 'Todo deleted'}
    raise HTTPException(status_code=404, detail='Todo not found')