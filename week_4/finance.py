import sqlite3
import json
import os
from pydantic import BaseModel, PositiveFloat
from datetime import date
from typing import Optional, List

# --- DATA MODEL ---
class Expense(BaseModel):
    name: str
    amount: PositiveFloat
    category: str
    date: date
    description: Optional[str] = None

def save_expense_to_file(expense: Expense):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # SQL Injection Warning: NEVER format strings like f"VALUES ({name})".
    # ALWAYS use placeholders (?) to prevent hackers from breaking your DB.
    cursor.execute('''
        INSERT INTO expenses (name, amount, category, date)
        VALUES (?, ?, ?, ?)
    ''', (expense.name, expense.amount, expense.category, expense.date.isoformat()))
    
    conn.commit()
    conn.close()
    print(f"💾 Saved '{expense.name}' to Database!")

# --- LOGIC & ALGORITHMS (WEEK 2) ---

def analyze_expenses():
    """Reads data from SQL and calculates totals."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # SQL Command: Get everything
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall() # Returns a list of tuples like (1, 'Burger', 10.0, 'Food', '2025-12-16')
    
    conn.close()

    if not rows:
        print("No expenses found.")
        return

    total_spent = 0.0
    
    print("\n--- Expense List (From Database) ---")
    for row in rows:
        # Row is a tuple: (id, name, amount, category, date)
        # So row[1] is name, row[2] is amount...
        print(f"{row[4]} | {row[1]}: R$ {row[2]:.2f}")
        total_spent += row[2]
        
    print("-" * 30)
    print(f"💰 Total Spent: R$ {total_spent:.2f}")
    print(f"📊 Total Transactions: {len(rows)}")

def filter_by_category():
    """Filters expenses using SQL WHERE clause."""
    target = input("Enter category to filter (e.g., Food): ").strip()
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # SQL Command: Get ONLY matches
    # "COLLATE NOCASE" makes it case-insensitive (Food == food) in SQLite
    query = "SELECT * FROM expenses WHERE category = ? COLLATE NOCASE"
    
    cursor.execute(query, (target,))
    rows = cursor.fetchall()
    
    conn.close()
    
    print(f"\n--- Results for '{target}' ---")
    if not rows:
        print("No matches found.")
    else:
        total = 0
        for row in rows:
            print(f"{row[4]} | {row[1]}: R$ {row[2]:.2f}")
            total += row[2]
        
        print(f"💰 Total in this category: R$ {total:.2f}")

def sort_by_amount():
    """Sorts expenses from highest to lowest using SQL."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # SQL Command: The database does the heavy lifting
    # ORDER BY amount DESC (Descending = High to Low)
    cursor.execute("SELECT * FROM expenses ORDER BY amount DESC")
    rows = cursor.fetchall()
    
    conn.close()
    
    if not rows:
        print("No expenses found.")
        return

    print("\n--- Top Expenses (Highest to Lowest) ---")
    for i, row in enumerate(rows, 1):
        # row[2] is the amount, row[1] is the name
        print(f"#{i} | R$ {row[2]:.2f} - {row[1]} ({row[4]})")


DB_NAME = "expenses.db"

def init_db():
    """Creates the table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # SQL Command to create table
    # IF NOT EXISTS prevents errors if we run this twice
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit() # Save changes
    conn.close()


# --- MAIN MENU ---
def main():
    while True:
        print("\n--- Financial CLI v2.0 ---")
        print("1. Add New Expense")
        print("2. Analyze Total (All)")
        print("3. Filter by Category")
        print("4. Sort by Highest Amount") # <--- NEW
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name_input = input("Expense Name: ")
            amount_input = input("Amount: ")
            category_input = input("Category: ")
            date_input = input("Date (YYYY-MM-DD) or empty: ")

            if not date_input:
                date_input = date.today()

            try:
                expense = Expense(
                    name=name_input,
                    amount=amount_input,
                    category=category_input,
                    date=date_input
                )
                save_expense_to_file(expense)
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            analyze_expenses()

        elif choice == "3":
            filter_by_category()

        elif choice == "4":
            sort_by_amount()

        elif choice == "5":
            print("Exiting...")
            break
            
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    init_db()  # <--- Initialize DB before starting the menu
    main()