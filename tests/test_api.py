from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'AI Workflow API is running'}

def test_predict_country():
    response = client.get('/predict/USA')
    assert response.status_code == 200
    assert 'prediction' in response.json()

def test_predict_all():
    response = client.get('/predict/all')
    assert response.status_code == 200
    assert 'prediction' in response.json()
