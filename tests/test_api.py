from fastapi.testclient import TestClient  
from app.main import app  
  
client = TestClient(app)  
  
def test_read_root():  
    response = client.get("/")  
    assert response.status_code == 200  
    assert "message" in response.json()  
  
def test_create_todo():  
    response = client.post(  
        "/todos/",  
        json={"title": "Test Task", "description": "Test Description"}  
    )  
    assert response.status_code == 201  
    assert response.json()["title"] == "Test Task"  
  
def test_read_todos():  
    response = client.get("/todos/")  
    assert response.status_code == 200  
    assert isinstance(response.json(), list)  
  
def test_read_todo():  
    # Primero crear una tarea  
    create_response = client.post(  
        "/todos/",  
        json={"title": "Task to Read"}  
    )  
    todo_id = create_response.json()["id"]  
      
    # Luego leerla  
    response = client.get(f"/todos/{todo_id}")  
    assert response.status_code == 200  
    assert response.json()["title"] == "Task to Read"  
  
def test_update_todo():  
    # Crear tarea  
    create_response = client.post(  
        "/todos/",  
        json={"title": "Task to Update"}  
    )  
    todo_id = create_response.json()["id"]  
      
    # Actualizar  
    response = client.put(  
        f"/todos/{todo_id}",  
        json={"completed": True}  
    )  
    assert response.status_code == 200  
    assert response.json()["completed"] == True  
  
def test_delete_todo():  
    # Crear tarea  
    create_response = client.post(  
        "/todos/",  
        json={"title": "Task to Delete"}  
    )  
    todo_id = create_response.json()["id"]  
      
    # Eliminar  
    response = client.delete(f"/todos/{todo_id}")  
    assert response.status_code == 204  
      
    # Verificar que no existe  
    get_response = client.get(f"/todos/{todo_id}")  
    assert get_response.status_code == 404