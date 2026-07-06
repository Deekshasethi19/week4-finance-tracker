"""
Project Name: Personal Finance Tracker
Name: Deeksha

Description:
Personal Finance Tracker is a Python-based application that helps users manage daily expenses. It allows users to add, update, delete, search, and filter expenses, generate reports, track monthly budgets, manage recurring expenses, and store data using JSON and CSV files.
"""



"""
main.py

This is the main file of Personal Finance Tracker.
"""

# Importing required classes
from expenses import Expense, ExpenseManager
from file_handler import FileHandler
from reports import ReportGenerator
from utils import Utility

# Creating objects
expense_manager = ExpenseManager()
file_handler = FileHandler()
utility = Utility()

# Load previous data from JSON file
expense_manager.expense_list = file_handler.load_json()


# Function to add new expense
def add_new_expense():

    print("\n------ Add New Expense ------")

    try:

        # Taking expense details from user
        expense_id = int(input("Enter Expense ID : "))

        # Check if expense id already exists
        for expense in expense_manager.get_expense_list():

           if expense.expense_id == expense_id:

            print("Expense ID already exists.")

            return

        # Check expense id
        if not utility.check_expense_id(expense_id):

            print("Invalid Expense ID.")
            return

        date = input("Enter Date (YYYY-MM-DD) : ")

        amount = float(input("Enter Amount : ₹"))

        category = input("Enter Category : ")

        # Check category
        if utility.check_category(category) == False:

            print("Category cannot be empty.")
            return

        description = input("Enter Description : ")

        # Check description
        if utility.check_description(description) == False:

            print("Description cannot be empty.")
            return

        recurring = input("Recurring Expense (Yes/No) : ")

        recurring = utility.check_recurring(recurring)

        # If user enters invalid value
        if recurring is None:

            return

        # Create expense object
        expense = Expense(
            expense_id,
            date,
            amount,
            category,
            description,
            recurring
        )

        # Add expense into list
        expense_manager.add_expense(expense)

        # Save data into JSON
        file_handler.save_json(
            expense_manager.get_expense_list()
        )

    except Exception as e:

        print("Error :", e)


# Function to delete expense
def delete_expense():

    print("\n------ Delete Expense ------")

    try:

        # Ask expense id
        expense_id = int(input("Enter Expense ID : "))

        # Remove expense
        expense_manager.remove_expense(expense_id)

        # Save updated list
        file_handler.save_json(
            expense_manager.get_expense_list()
        )

    except Exception as e:

        print("Error :", e)


# Function to display all expenses
def display_expenses():

    print("\n------ Expense List ------")

    expense_manager.display_expenses()


# Function to search expenses
def search_expense():

    print("\n------ Search Expense ------")

    print("1. Search by Category")
    print("2. Search by Date")
    print("3. Search by Amount")

    choice = input("Enter Choice : ")

    if choice == "1":

        category = input("Enter Category : ")

        result = expense_manager.search_category(category)

    elif choice == "2":

        date = input("Enter Date (YYYY-MM-DD) : ")

        result = expense_manager.search_date(date)

    elif choice == "3":

        minimum = float(input("Minimum Amount : "))

        maximum = float(input("Maximum Amount : "))

        result = expense_manager.search_amount(
            minimum,
            maximum
        )

    else:

        print("Invalid Choice.")
        return

    # Display searched result
    if len(result) == 0:

        print("\nNo Expense Found.\n")

    else:

        print("\n------ Search Result ------\n")

        for expense in result:

            print(expense)

            print("-" * 40)

# Function to generate reports
def generate_reports():

    print("\n------ Reports ------")

    # Create ReportGenerator object
    report = ReportGenerator(
        expense_manager.get_expense_list()
    )

    print("1. Category Wise Report")
    print("2. Monthly Report")
    print("3. Monthly Spending Trend")
    print("4. Expense Statistics")
    print("5. Text Based Chart")

    choice = input("Enter Choice : ")

    if choice == "1":

        report.category_report()

    elif choice == "2":

        report.monthly_report()

    elif choice == "3":

        report.monthly_trend()

    elif choice == "4":

        report.expense_statistics()

    elif choice == "5":

        report.show_chart()

    else:

        print("Invalid Choice.")


# Function to set monthly budget
def set_budget():

    utility.set_budget()


# Function to check budget status
def check_budget():

    # Calculate total expense
    total = expense_manager.total_expense()

    # Compare total expense with budget
    utility.check_budget(total)


# Function to export data into CSV
def export_csv():

    file_handler.export_csv(
        expense_manager.get_expense_list()
    )


# Function to import data from CSV
def import_csv():

    # Load expense list from CSV
    expense_manager.expense_list = (
        file_handler.import_csv()
    )

    # Save imported data into JSON also
    file_handler.save_json(
        expense_manager.get_expense_list()
    )

    print("CSV Imported Successfully.")


# Function to create backup
def create_backup():

    file_handler.create_backup()


# Function to restore backup
def restore_backup():

    file_handler.restore_backup()

    # Reload data after restoring backup
    expense_manager.expense_list = (
        file_handler.load_json()
    )

# Function to update expense
def update_expense():

    print("\n------ Update Expense ------")

    try:

        # Ask expense id from user
        expense_id = int(input("Enter Expense ID : "))

        # Update expense
        expense_manager.update_expense(expense_id)

        # Save updated data
        file_handler.save_json(
            expense_manager.get_expense_list()
        )

    except Exception as e:

        print("Error :", e)


# Function to filter expenses
def filter_expense():

    print("\n------ Filter Expenses ------")

    print("1. Filter by Category")
    print("2. Filter by Amount")
    print("3. Show Recurring Expenses")

    choice = input("Enter Choice : ")

    # Filter using category
    if choice == "1":

        category = input("Enter Category : ")

        result = expense_manager.filter_by_category(category)

    # Filter using amount
    elif choice == "2":

        minimum = float(input("Enter Minimum Amount : "))

        maximum = float(input("Enter Maximum Amount : "))

        result = expense_manager.filter_by_amount(
            minimum,
            maximum
        )

    # Show recurring expenses
    elif choice == "3":

        result = expense_manager.show_recurring_expenses()

    else:

        print("Invalid Choice.")
        return

    # Display result
    if len(result) == 0:

        print("\nNo Expense Found.\n")

    else:

        print("\n------ Filter Result ------\n")

        for expense in result:

            print(expense)

            print("-" * 40)


# Main Menu
while True:
    print("=" * 45)
    print("\n========== Personal Finance Tracker ==========")
    print("=" * 45)
    
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Update Expense")
    print("4. Display All Expenses")
    print("5. Search Expense")
    print("6. Filter Expense")
    print("7. Generate Reports")
    print("8. Set Monthly Budget")
    print("9. Check Budget Status")
    print("10. Export to CSV")
    print("11. Import from CSV")
    print("12. Create Backup")
    print("13. Restore Backup")
    print("14. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":

        add_new_expense()

    elif choice == "2":

        delete_expense()

    elif choice == "3":

        update_expense()

    elif choice == "4":

        display_expenses()

    elif choice == "5":

        search_expense()

    elif choice == "6":

        filter_expense()

    elif choice == "7":

        generate_reports()

    elif choice == "8":

        set_budget()

    elif choice == "9":

        check_budget()

    elif choice == "10":

        export_csv()

    elif choice == "11":

        import_csv()

    elif choice == "12":

        create_backup()

    elif choice == "13":

        restore_backup()

    elif choice == "14":

        print("\nThank You for Using Personal Finance Tracker.")

        break

    else:

        print("Invalid Choice. Please Try Again.")    