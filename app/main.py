# Import FastAPI framework
from fastapi import FastAPI

# Initialize a FastAPI instance (creates the application)
app = FastAPI()

# Define a GET endpoint at the root URL "/"
@app.get("/")
async def read_main():
    """
    Returns a message confirming the API is running.
    """
    return {"message": "Masterclass Overview MLOPS"}
