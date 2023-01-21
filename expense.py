import os
import csv

# Initialize variables
expenses = []
income = []

def load_data():
    """Load data from CSV files"""
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append({"description": row[0], "amount": float(row[1])})
    if os.path.exists("income.csv"):
        with open("income.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                income.append({"description": row[0], "amount": float(row[1])})

def save_data():
    """Save data to CSV files"""
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense["description"], expense["amount"]])
    with open("income.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for inc in income:
            writer.writerow([inc["description"], inc["amount"]])

def add_expense(description, amount):
    """Add an expense"""
    expenses.append({"description": description, "amount": amount})

def add_income(description, amount):
    """Add an income"""
    income.append({"description": description, "amount": amount})

def show_expenses():
    """Show all expenses"""
    total = 0
    for expense in expenses:
        total += expense["amount"]
        print(f"{expense['description']}: {expense['amount']}")
    print(f"Total expenses: {total}")

def show_income():
    """Show all income"""
    total = 0
    for inc in income:
        total += inc["amount"]
        print(f"{inc['description']}: {inc['amount']}")
    print(f"Total income: {total}")

def show_balance():
    """Show current balance"""
    expenses_total = 0
    for expense in expenses:
        expenses_total += expense["amount"]
    income_total = 0
    for inc in income:
        income_total += inc["amount"]
    print(f"Balance: {income_total - expenses_total}")

# Load data from CSV files
load_data()

while True:
    action = input("What would you like to do? (add expense/income, show expenses/income/balance, exit) ")
    if action == "add expense":
        description = input("Enter the expense description: ")
        amount = float(input("Enter the expense amount: "))
        add_expense(description, amount)
    elif action == "add income":
        description = input("Enter the income description: ")
        amount = float(input("Enter the income: "))
        add_income(description, amount)
    elif action == "show expenses":
        show_expenses()
    elif action == "show income":
        show_income()
    elif action == "show balance":
        show_balance()
    elif action == "exit":
        save_data()
        break
    else:
        print("Invalid action.")
