import csv
import os
from datetime import datetime

# Define the filename for storing expenses
FILENAME = 'expenses.csv'

# Define the headers for the CSV file
HEADERS = ['Date', 'Description', 'Category', 'Amount']

def initialize_file():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_expense():
    """Add a new expense to the CSV file."""
    date = input("Enter the date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    description = input("Enter the description: ").strip()
    category = input("Enter the category: ").strip()
    while True:
        try:
            amount = float(input("Enter the amount: ").strip())
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, f"{amount:.2f}"])
    print("Expense added successfully.")

def view_expenses():
    """Display all expenses from the CSV file."""
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) <= 1:
        print("No expenses recorded.")
        return
    print(f"\n{'Index':<6}{'Date':<12}{'Description':<20}{'Category':<15}{'Amount':>10}")
    print("-" * 65)
    for idx, row in enumerate(expenses[1:], start=1):
        date, description, category, amount = row
        print(f"{idx:<6}{date:<12}{description:<20}{category:<15}{amount:>10}")
    print()

def delete_expense():
    """Delete an expense by its index."""
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) <= 1:
        print("No expenses to delete.")
        return
    view_expenses()
    while True:
        try:
            index = int(input("Enter the index of the expense to delete: ").strip())
            if 1 <= index < len(expenses):
                break
            else:
                print(f"Please enter a number between 1 and {len(expenses) - 1}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    removed = expenses.pop(index)
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print(f"Deleted expense: {removed}")

def show_summary():
    """Display a summary of expenses by category and total amount."""
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
    if len(expenses) <= 1:
        print("No expenses recorded.")
        return
    summary = {}
    total = 0.0
    for row in expenses[1:]:
        date, description, category, amount = row
        amount = float(amount)
        total += amount
        summary[category] = summary.get(category, 0.0) + amount
    print("\nExpense Summary by Category:")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")
    print(f"\nTotal Expenses: ${total:.2f}\n")

def main():
    """Main function to run the Expense Tracker."""
    initialize_file()
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
