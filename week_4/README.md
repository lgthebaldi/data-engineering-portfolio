# Week 4: SQL Database Integration 🗄️

In this phase, I migrated the application's storage layer from a flat JSON file to **SQLite**. This represents a shift towards "System Design," focusing on data integrity, query performance, and security.

## 🔄 Architecture Change
* **Before (Week 1-3):** Loaded entire JSON file into RAM. $O(N)$ operations. Risk of corruption.
* **After (Week 4):** Direct SQL transactions. Database engine handles sorting and filtering. $O(log N)$ potential with indexes.

## 🛢 Database Schema
The application automatically initializes a local `expenses.db` with the following structure:

| Column     | Type    | Description                  |
|------------|---------|------------------------------|
| `id`       | INTEGER | Primary Key (Auto Increment) |
| `name`     | TEXT    | Name of the expense          |
| `amount`   | REAL    | Value (Float)                |
| `category` | TEXT    | Category (e.g., Food)        |
| `date`     | TEXT    | Date in ISO format           |

## 🛡️ Security Note
* **SQL Injection Prevention:** All queries use parameterized inputs (placeholders `?`) instead of f-string formatting. This prevents attackers from injecting malicious SQL commands.

## 💻 Code Highlight
Refactoring from Python Sort to SQL Sort:
```python
# The Database engine sorts 100x faster than Python for large datasets
cursor.execute("SELECT * FROM expenses ORDER BY amount DESC")

🚀 How to Run
Create environment: python3 -m venv .venv && source .venv/bin/activate

Install dependencies: pip install -r requirements.txt

Run: python finance.py