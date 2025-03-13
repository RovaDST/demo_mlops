# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy necessary files and install dependencies
COPY ./requirements.txt ./app /code/

# Create a virtual environment to prevent system pollution
RUN python -m venv /code/venv \
    && /code/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /code/venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the virtual environment path
ENV PATH="/code/venv/bin:$PATH"

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
