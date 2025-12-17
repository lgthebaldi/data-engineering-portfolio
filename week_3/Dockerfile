# 1. Base Image: Linux + Python 3.10 (Slim version)
FROM python:3.10-slim

# 2. Setup the work folder inside the container
WORKDIR /app

# 3. Copy dependency file
COPY requirements.txt .

# 4. Install dependencies (Cleanly)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY finance.py .

# 6. Default command to run
CMD ["python", "finance.py"]