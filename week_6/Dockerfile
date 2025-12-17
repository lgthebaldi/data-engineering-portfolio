# 1. Base Image
FROM python:3.10-slim

# 2. Setup Folder
WORKDIR /app

# 3. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the API Code
COPY main.py .

# 5. Network: Expose port 8000
EXPOSE 8000

# 6. Command: Start the Server
# --host 0.0.0.0 is MANDATORY for Docker to accept outside connections
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]