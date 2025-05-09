from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_vehicle():
    response = client.post("/vehicles", json={"brand": "Brand", "model": "Model", "manufacture_year": 2020, "mileage": 12000.0, "fuel_type": "Gasoline", "price": 30000.0, "has_fines": False, "has_insurance": True, "color": "Red", "transmission": "Automatic", "doors": 4, "airbag": True, "abs": True, "last_service_date": "2022-08-01"})
   
    assert response.status_code == 200