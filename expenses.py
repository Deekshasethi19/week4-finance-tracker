"""
expenses.py

This file contains Expense class and ExpenseManager class.
"""

# Importing datetime module for date validation
from datetime import datetime


# Creating Expense class
class Expense:

    # Constructor
    def __init__(self, expense_id, date, amount, category, description, recurring=False):

        # Initialize all expense details
        self.expense_id = expense_id
        self.date = self.check_date(date)
        self.amount = self.check_amount(amount)
        self.category = category
        self.description = description
        self.recurring = recurring

    # Function to validate date
    def check_date(self, date):

        try:

            # Check date format
            datetime.strptime(date, "%Y-%m-%d")

            return date

        except ValueError:

            raise ValueError("Enter date in YYYY-MM-DD format.")

    # Function to validate amount
    def check_amount(self, amount):

        amount = float(amount)

        if amount <= 0:

            raise ValueError("Amount should be greater than zero.")

        return amount

    # Convert object into dictionary
    def to_dictionary(self):

        return {

            "expense_id": self.expense_id,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "recurring": self.recurring

        }

    # Display expense details
    def __str__(self):

        return (

            f"\nExpense ID : {self.expense_id}"
            f"\nDate : {self.date}"
            f"\nAmount : ₹{self.amount}"
            f"\nCategory : {self.category}"
            f"\nDescription : {self.description}"
            f"\nRecurring : {self.recurring}"

        )


# Creating ExpenseManager class
class ExpenseManager:

    # Constructor
    def __init__(self):

        # List to store all expenses
        self.expense_list = []

    # Function to add new expense
    def add_expense(self, expense):

        self.expense_list.append(expense)

        print("Expense Added Successfully.")

    # Function to delete expense
    def remove_expense(self, expense_id):

        # Check every expense
        for expense in self.expense_list:

            if expense.expense_id == expense_id:

                self.expense_list.remove(expense)

                print("Expense Deleted Successfully.")

                return

        print("Expense Not Found.")

    # Function to search by category
    def search_category(self, category):

        result = []

        # Compare category
        for expense in self.expense_list:

            if expense.category.lower() == category.lower():

                result.append(expense)

        return result

    # Function to search by date
    def search_date(self, date):

        result = []

        # Compare dates
        for expense in self.expense_list:

            if expense.date == date:

                result.append(expense)

        return result

    # Function to search by amount
    def search_amount(self, minimum, maximum):

        result = []

        # Compare amount range
        for expense in self.expense_list:

            if minimum <= expense.amount <= maximum:

                result.append(expense)

        return result

    # Function to display all expenses
    def display_expenses(self):

        if len(self.expense_list) == 0:

            print("\nNo Expense Found.\n")

            return

        print("\n========== Expense List ==========\n")

        for expense in self.expense_list:

            print(expense)

            print("-" * 40)

    # Function to calculate total expense
    def total_expense(self):

        total = 0

        # Add every expense amount
        for expense in self.expense_list:

            total = total + expense.amount

        return total

    # Function to return complete list
    def get_expense_list(self):

        return self.expense_list
    
        # Function to update expense details
    def update_expense(self, expense_id):

        # Check every expense
        for expense in self.expense_list:

            # Match expense id
            if expense.expense_id == expense_id:

                print("\nLeave blank if you don't want to change any value.\n")

                # Take new amount
                new_amount = input("Enter New Amount : ")

                if new_amount != "":

                    expense.amount = expense.check_amount(new_amount)

                # Take new date
                new_date = input("Enter New Date (YYYY-MM-DD) : ")

                if new_date != "":

                    expense.date = expense.check_date(new_date)

                # Take new category
                new_category = input("Enter New Category : ")

                if new_category != "":

                    expense.category = new_category

                # Take new description
                new_description = input("Enter New Description : ")

                if new_description != "":

                    expense.description = new_description

                # Take recurring status
                new_recurring = input("Recurring Expense (Yes/No) : ")

                if new_recurring != "":

                    if new_recurring.lower() == "yes":

                        expense.recurring = True

                    elif new_recurring.lower() == "no":

                        expense.recurring = False

                    else:

                        print("Invalid Input. Keeping previous value.")

                print("Expense Updated Successfully.")

                return

        print("Expense Not Found.")

    # Function to filter expenses by category
    def filter_by_category(self, category):

        # Empty list to store filtered data
        filtered_list = []

        # Check every expense
        for expense in self.expense_list:

            if expense.category.lower() == category.lower():

                filtered_list.append(expense)

        return filtered_list

    # Function to filter expenses by amount
    def filter_by_amount(self, minimum, maximum):

        # Empty list to store filtered data
        filtered_list = []

        # Check every expense
        for expense in self.expense_list:

            if minimum <= expense.amount <= maximum:

                filtered_list.append(expense)

        return filtered_list

    # Function to display recurring expenses
    def show_recurring_expenses(self):

        # Empty list for recurring expenses
        recurring_list = []

        # Check every expense
        for expense in self.expense_list:

            if expense.recurring:

                recurring_list.append(expense)

        return recurring_list