"""
file_handler.py

This file is used to save and load expense data.
"""

import json
import csv
import os
import shutil

from expenses import Expense


class FileHandler:

    # Constructor
    def __init__(self):

       # Create required folders if they don't exist
        os.makedirs("data", exist_ok=True)
        os.makedirs("exports", exist_ok=True)
        os.makedirs("data/backup", exist_ok=True)

        # File paths
        self.json_file = "data/expenses.json"
        self.csv_file = "exports/expenses.csv"
        self.backup_folder = "data/backup"

    # Save data into JSON file
    def save_json(self, expense_list):

        try:

            data = []

            for expense in expense_list:

                data.append(expense.to_dictionary())

            with open(self.json_file, "w") as file:

                json.dump(data, file, indent=4)

            print("Data saved successfully.")

        except Exception as e:

            print("Error :", e)

    # Load data from JSON file
    def load_json(self):

        expense_list = []

        try:

            if not os.path.exists(self.json_file):

                return expense_list

            with open(self.json_file, "r") as file:

                data = json.load(file)

            for item in data:

                expense = Expense(
                    item["expense_id"],
                    item["date"],
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["recurring"]
                )

                expense_list.append(expense)

        except Exception as e:

            print("Error :", e)

        return expense_list

    # Export data into CSV file
    def export_csv(self, expense_list):

        try:

            with open(self.csv_file, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Expense ID",
                    "Date",
                    "Amount",
                    "Category",
                    "Description",
                    "Recurring"
                ])

                for expense in expense_list:

                    writer.writerow([
                        expense.expense_id,
                        expense.date,
                        expense.amount,
                        expense.category,
                        expense.description,
                        expense.recurring
                    ])

            print("CSV exported successfully.")

        except Exception as e:

            print("Error :", e)

    # Import data from CSV file
    def import_csv(self):

        expense_list = []

        try:

            with open(self.csv_file, "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    expense = Expense(

                        int(row["Expense ID"]),
                        row["Date"],
                        float(row["Amount"]),
                        row["Category"],
                        row["Description"],
                        row["Recurring"] == "True"

                    )

                    expense_list.append(expense)

        except Exception as e:

            print("Error :", e)

        return expense_list

    # Create backup
    def create_backup(self):

        try:

            if not os.path.exists(self.backup_folder):

                os.makedirs(self.backup_folder)

            backup_file = self.backup_folder + "/expenses_backup.json"

            shutil.copy(self.json_file, backup_file)

            print("Backup created successfully.")

        except Exception as e:

            print("Error :", e)

    # Restore backup
    def restore_backup(self):

        try:

            backup_file = self.backup_folder + "/expenses_backup.json"

            shutil.copy(backup_file, self.json_file)

            print("Backup restored successfully.")

        except Exception as e:

            print("Error :", e)