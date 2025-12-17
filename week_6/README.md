# Week 6: The Capstone - Containerized Microservice 🐳

This is the culmination of Phase 1. I combined **FastAPI**, **SQLite**, and **Docker** into a production-ready microservice. The entire system is orchestrated using **Docker Compose**, allowing for single-command deployment.

## 🌟 Features
* **Zero-Config Deployment:** No need to install Python or create virtual environments. Just requires Docker.
* **Orchestration:** `docker-compose.yml` manages the build process, network ports, and storage volumes automatically.
* **Data Persistence:** Uses a Bind Mount to ensure `expenses.db` survives container restarts.

## 🛠 Tech Stack
* **Language:** Python 3.10
* **Framework:** FastAPI
* **Database:** SQLite
* **Infrastructure:** Docker & Docker Compose

## 🚀 How to Run (The "Magic" Command)

1. Ensure Docker is installed.
2. Run the orchestration command:
   ```bash
   sudo docker compose up --build


   Access the API:

Swagger UI: http://localhost:8000/docs

API Root: http://localhost:8000/

📂 Project Structure
docker-compose.yml: The infrastructure manager.

Dockerfile: The blueprint for the container image.

main.py: The application logic (API).

requirements.txt: Dependencies.