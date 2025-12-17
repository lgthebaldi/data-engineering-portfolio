import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, PositiveFloat
from typing import List, Optional  # <--- This is the key import!

# 1. Setup the App
app = FastAPI(title="Financial API", description="Week 5: My First API")
DB_NAME = "expenses.db"

# 2. Pydantic Models
class ExpenseCreate(BaseModel):
    name: str
    amount: PositiveFloat
    category: str
    date: str 

class ExpenseResponse(ExpenseCreate):
    id: int

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- API ENDPOINTS ---

@app.get("/")
def read_root():
    return {"status": "System Online", "version": "1.0"}

@app.post("/expenses/", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO expenses (name, amount, category, date)
        VALUES (?, ?, ?, ?)
    ''', (expense.name, expense.amount, expense.category, expense.date))
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {**expense.dict(), "id": new_id}

# GET with Filter
@app.get("/expenses/", response_model=List[ExpenseResponse])
def read_expenses(category: Optional[str] = None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if category:
        # Filter Logic (Case Insensitive)
        cursor.execute("SELECT * FROM expenses WHERE category = ? COLLATE NOCASE", (category,))
    else:
        # Get All Logic
        cursor.execute("SELECT * FROM expenses")
        
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "name": row[1],
            "amount": row[2],
            "category": row[3],
            "date": row[4]
        })
    
    return results