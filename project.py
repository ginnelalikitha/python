# ==============================
# EXPENSE TRACKER
# ==============================

class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount


class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, title, amount):
        expense = Expense(title, amount)
        self.expenses.append(expense)
        self.save_expense(expense)

    def save_expense(self, expense):
        with open(self.filename, "a") as file:
            file.write(f"{expense.title},{expense.amount}\n")

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    title, amount = line.strip().split(",")
                    self.expenses.append(Expense(title, float(amount)))
        except FileNotFoundError:
            pass

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(f"{expense.title}: ₹{expense.amount}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ₹{total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter expense title: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(title, amount)
            print("Expense added successfully!")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


main()


 
