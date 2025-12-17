# Week 1: Financial Data Validator 🛡️

A CLI tool focused on **Data Quality**. Unlike simple scripts that accept any input, this project enforces strict type validation before data is ever saved to disk.

## 🎯 Key Concepts
* **Virtual Environments:** Used `.venv` to isolate dependencies, preventing system-wide conflicts.
* **Pydantic Models:** Defines a strict contract for data. If a user tries to enter text for a price, the system rejects it immediately.
* **Persistence:** Saves data to a local `expenses.json` file so information survives after the program closes.

## 💻 Code Highlight
Refusing bad data at the door:
```python
class Expense(BaseModel):
    name: str
    amount: PositiveFloat  # <--- Automatically rejects negative numbers
    category: str
    date: date



    🚀 How to Run
Activate the environment: source .venv/bin/activate

Install dependencies: pip install -r requirements.txt

Run: python finance.py