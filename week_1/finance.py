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

# --- FILE HANDLING FUNCTIONS ---
def load_expenses():
    """Reads the JSON file and returns a list of dictionaries."""
    if not os.path.exists("expenses.json"):
        return [] # Return an empty list if file doesn't exist
    
    with open("expenses.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return [] # Return empty list if file is corrupted

def save_expense_to_file(expense: Expense):
    """Saves the validated expense to the JSON file."""
    # 1. Load existing data
    existing_data = load_expenses()
    
    # 2. Convert our Pydantic Object to a Dictionary (JSON-compatible)
    # mode='json' ensures dates are converted to strings automatically
    new_data = expense.model_dump(mode='json') 
    
    # 3. Add to the list
    existing_data.append(new_data)
    
    # 4. Write back to file
    with open("expenses.json", "w") as f:
        json.dump(existing_data, f, indent=4)
    
    print(f"💾 Saved '{expense.name}' to expenses.json successfully!")

# --- MAIN APP ---
def main():
    print("--- Financial CLI v1.0 ---")
    
    name_input = input("Expense Name: ")
    amount_input = input("Amount: ")
    category_input = input("Category: ")
    date_input = input("Date (YYYY-MM-DD) or empty: ")

    if not date_input:
        date_input = date.today()

    try:
        # Validate data
        expense = Expense(
            name=name_input,
            amount=amount_input,
            category=category_input,
            date=date_input
        )
        
        # If we reach this line, data is valid. Save it!
        save_expense_to_file(expense)

    except Exception as e:
        print("\n❌ Error: Data not saved.")
        print(e)

if __name__ == "__main__":
    main()