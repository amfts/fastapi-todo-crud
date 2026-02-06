from fastapi import FastAPI, Depends, HTTPException  
from sqlalchemy.orm import Session  
from typing import List  
  
from . import models, schemas  
from .database import engine, get_db  
  
# Crear tablas en la BD  
models.Base.metadata.create_all(bind=engine)  
  
app = FastAPI(  
    title="TODO API",  
    description="API REST para gestionar tareas",  
    version="1.0.0"  
)  
  
@app.get("/")  
def read_root():  
    return {"message": "TODO API - Usa /docs para ver la documentación"}  
  
@app.post("/todos/", response_model=schemas.Todo, status_code=201)  
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):  
    """Crear una nueva tarea"""  
    db_todo = models.Todo(**todo.model_dump())  
    db.add(db_todo)  
    db.commit()  
    db.refresh(db_todo)  
    return db_todo  
  
@app.get("/todos/", response_model=List[schemas.Todo])  
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):  
    """Obtener todas las tareas"""  
    todos = db.query(models.Todo).offset(skip).limit(limit).all()  
    return todos  
  
@app.get("/todos/{todo_id}", response_model=schemas.Todo)  
def read_todo(todo_id: int, db: Session = Depends(get_db)):  
    """Obtener una tarea específica"""  
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()  
    if todo is None:  
        raise HTTPException(status_code=404, detail="Tarea no encontrada")  
    return todo  
  
@app.put("/todos/{todo_id}", response_model=schemas.Todo)  
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):  
    """Actualizar una tarea"""  
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()  
    if todo is None:  
        raise HTTPException(status_code=404, detail="Tarea no encontrada")  
      
    update_data = todo_update.model_dump(exclude_unset=True)  
    for key, value in update_data.items():  
        setattr(todo, key, value)  
      
    db.commit()  
    db.refresh(todo)  
    return todo  
  
@app.delete("/todos/{todo_id}", status_code=204)  
def delete_todo(todo_id: int, db: Session = Depends(get_db)):  
    """Eliminar una tarea"""  
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()  
    if todo is None:  
        raise HTTPException(status_code=404, detail="Tarea no encontrada")  
      
    db.delete(todo)  
    db.commit()  
    return None