# Week 5: REST API with FastAPI ⚡

In this phase, I transitioned the application from a local CLI to a web-based **REST API**. This allows external clients (Websites, Mobile Apps) to interact with the data via standard HTTP requests.

## 🏗 Architecture
* **Framework:** FastAPI (Modern, high-performance Python framework).
* **Server:** Uvicorn (ASGI Server).
* **Database:** SQLite (Integrated directly into the endpoints).
* **Validation:** Pydantic models automatically validate incoming JSON payloads.

## 🔌 Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `GET` | `/` | Health Check (System Status). |
| `POST` | `/expenses/` | Create a new expense. Expects JSON payload. |
| `GET` | `/expenses/` | Retrieve all expenses. |
| `GET` | `/expenses/?category=Food` | Filter expenses by category using Query Parameters. |

## 🚀 How to Run
1. Create environment: `python3 -m venv .venv && source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Start the Server:
   ```bash
   uvicorn main:app --reload