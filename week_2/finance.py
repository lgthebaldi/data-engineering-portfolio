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

# --- FILE HANDLING ---
def load_expenses():
    """Reads the JSON file and returns a list of dictionaries."""
    if not os.path.exists("expenses.json"):
        return []
    
    with open("expenses.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_expense_to_file(expense: Expense):
    """Saves the validated expense to the JSON file."""
    existing_data = load_expenses()
    new_data = expense.model_dump(mode='json')
    existing_data.append(new_data)
    
    with open("expenses.json", "w") as f:
        json.dump(existing_data, f, indent=4)
    
    print(f"💾 Saved '{expense.name}' to expenses.json successfully!")

# --- LOGIC & ALGORITHMS (WEEK 2) ---

def analyze_expenses():
    """Reads data and calculates basic statistics (Summation)."""
    data = load_expenses()
    if not data:
        print("No expenses found.")
        return

    total_spent = 0.0
    print("\n--- Expense List (Chronological) ---")
    for item in data:
        print(f"{item['date']} | {item['name']}: ${item['amount']}")
        total_spent += item['amount']
        
    print("-" * 30)
    print(f"💰 Total Spent: ${total_spent:.2f}")
    print(f"📊 Total Transactions: {len(data)}")

def filter_by_category():
    """Filters expenses based on user input (Linear Search)."""
    data = load_expenses()
    if not data:
        print("No expenses found.")
        return

    target = input("Enter category to filter (e.g., Food): ").strip()
    
    filtered_list = []
    for item in data:
        if item['category'].lower() == target.lower():
            filtered_list.append(item)
            
    print(f"\n--- Results for '{target}' ---")
    if not filtered_list:
        print("No matches found.")
    else:
        total = 0
        for item in filtered_list:
            print(f"{item['date']} | {item['name']}: ${item['amount']}")
            total += item['amount']
        print(f"💰 Total in this category: ${total:.2f}")

def sort_by_amount():
    """Sorts expenses from highest to lowest (Sorting Algorithm)."""
    data = load_expenses()
    if not data:
        print("No expenses found.")
        return

    # THE ALGORITHM: Sort by 'amount' in descending order
    # key=lambda x: x['amount'] -> Tells python to look at the price
    # reverse=True -> Highest first
    sorted_data = sorted(data, key=lambda x: x['amount'], reverse=True)
    
    print("\n--- Top Expenses (Highest to Lowest) ---")
    for i, item in enumerate(sorted_data, 1):
        print(f"#{i} | ${item['amount']} - {item['name']} ({item['date']})")

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
    main()