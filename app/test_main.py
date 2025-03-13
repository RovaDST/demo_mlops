# Import TestClient from FastAPI's testing utilities and the FastAPI application from main.py
from fastapi.testclient import TestClient
from app.main import app

# Create a test client to simulate API requests
client = TestClient(app)

# Define a test function to check the root endpoint "/"
def test_read_main():
    response = client.get("/")  # Send a GET request to "/"
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Verify the response body matches the expected output
    assert response.json() == {"message": "Masterclass Overview MLOPS"}
