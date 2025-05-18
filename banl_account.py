class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        # Private attributes (marked with '__')
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = balance

    # Getters (methods to access private attributes)
    def get_account_number(self):
        return self.__account_number
    
    def get_owner_name(self):
        return self.__owner_name

    def get_balance(self):
        return self.__balance

    # Setter (to change the owner's name)
    def set_owner_name(self, new_name):
        if new_name.strip():  # Make sure the name isn't empty
            self.__owner_name = new_name
        else:
            print("Invalid name!")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit must be a positive number.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Not enough money or invalid amount.")