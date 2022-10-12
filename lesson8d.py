# Bank Account
# Properties include:
# balance,
# account number,
# name of account holder,
# branch,
# active/inactive

# Methods may include:
# check balance,
# deposit money,
# withdraw cash,
# get a loan

# inheritance
# polymorphism
# encapsulation
# exception handling

# Databases - a collection of tables with records
# CRUD
# C - creating a database/table or storing/saving data to the database/table
# R - retrieving data from the database
# U - Update the data
# D - delete the data

# Examples of database languages: MySQL, Oracle, SQLite, PostgreSQL
# pymysql library/module
# We need an interface. We'll use Xampp/phpMyadmin database interface


class Account:
    bank_code = 1000

    def __init__(self, balance, accno, name, branch, status):
        if balance < 0:
            print("Balance cannot be zero")
        elif len(name) == 0:
            print("Please enter your name")
        elif len(accno) != 5:
            print("Invalid account number")
        else:
            print("Bank details captured")
            self.balance = balance
            self.accno = accno
            self.name = name
            self.branch = branch
            self.status = status

    def check_balance(self):
        print(f"Your balance is {self.balance}")
        return self.balance

    def deposit(self, depo_amount):
        if depo_amount <= 0:
            print("Amount is below what's allowed")
        elif depo_amount > 70000:
            print("You have exceeded the deposit amount allowable")
        else:
            if self.status == "active":
                print("Thanks for banking with us!")
                print(f"Your previous balance was {self.check_balance()}")
                self.balance = self.balance + depo_amount
                print(f"Your current balance is {self.balance}")
            else:
                print("Your account is inactive")

    # Create a method to withdraw amount from the bank
    # Ensure the person cannot withdraw more than the amount they have in their account
    # Ensure the person cannot withdraw if their account is inactive
    # Ensure the account has an initial deposit, e.g. 100

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("Your withdrawal amount exceeds what's in your account")
        elif self.status == "inactive":
            print("You need to activate your account first before you can withdraw")
        elif self.balance - withdrawal_amount < 100:
            print("A bank balance of at least Ksh. 100 is required.")
        else:
            print("Amount withdrawn successfully")
            print(f"Your new balance is {self.balance - withdrawal_amount}")
            print("Thank you for banking with us!")


account1 = Account(100, "54321", "Julie Waithera", "Kiambu Branch", "active")

account1.check_balance()
account1.deposit(20000)
account1.withdraw(20100)
