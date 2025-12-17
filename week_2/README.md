# Week 2: Algorithms & Analytics 🧠

Building on Week 1, this phase adds intelligence to the system. I implemented core data processing algorithms to query and rank the financial data.

## 🎯 Key Features
* **Interactive Menu:** A loop-based interface for continuous use.
* **Aggregation Engine:** Calculates total spending by iterating through data structures.
* **Linear Search:** A filtering algorithm that scans the dataset to find specific categories (Case Insensitive).
* **Sorting Engine:** Ranks expenses from highest to lowest using Python's Sort with Lambda keys.

## 🧐 Engineering Decisions
* **Why manual filtering?** Instead of using Pandas immediately, I wrote the filtering logic manually to better understand how data selection works under the hood ($O(N)$ complexity).
* **Immutability:** The sorting function creates a *new* view of the data, preserving the original chronological order in the database.

## 💻 Code Highlight
Sorting with Lambda functions:
```python
# Sorts by 'amount' in descending order (Expensive -> Cheap)
sorted_data = sorted(data, key=lambda x: x['amount'], reverse=True)

🚀 How to Run
Activate the environment (if not active).

Run: python finance.py