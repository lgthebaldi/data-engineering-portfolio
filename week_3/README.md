# Week 3: Containerized Application 🐳

In this phase, I transformed the local Python script into a portable **Docker Container**. This ensures the application runs identically on any machine (Linux, Windows, Mac, or Cloud) without requiring the user to install Python or dependencies manually.

## 🏗 Architecture
* **Base Image:** `python:3.10-slim` (Lightweight Linux).
* **Isolation:** All dependencies (`pydantic`) are installed inside the container, keeping the host system clean.
* **Persistence:** Uses **Docker Volumes (Bind Mounts)** to save the `expenses.json` file to the host machine, preventing data loss when the container stops.

## 🚀 How to Run (Docker)

### 1. Build the Image
Create the "Cake Mold" from the Dockerfile:
```bash
    docker build -t financial-cli .

2. Run the Container

    docker run -it -v $(pwd):/app financial-cli

-it: Interactive mode (required for user input).

-v $(pwd):/app: Maps your current folder to the container so expenses.json is saved on your disk.

📂 File Structure
Dockerfile: The "Recipe" for building the environment.

requirements.txt: List of dependencies installed inside the container.

finance.py: The source code (injected into the container).