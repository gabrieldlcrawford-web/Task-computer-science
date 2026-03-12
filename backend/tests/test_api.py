from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_task_crud():
    create = client.post('/tasks', json={'title': 'Test task', 'description': 'demo', 'done': False})
    assert create.status_code == 201
    task_id = create.json()['id']

    list_response = client.get('/tasks')
    assert list_response.status_code == 200
    assert any(task['id'] == task_id for task in list_response.json())

    patch = client.patch(f'/tasks/{task_id}', json={'done': True})
    assert patch.status_code == 200
    assert patch.json()['done'] is True

    delete = client.delete(f'/tasks/{task_id}')
    assert delete.status_code == 204
