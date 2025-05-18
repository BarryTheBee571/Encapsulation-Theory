from banl_account import BankAccount

account1 = BankAccount("123456789", "Stephen", 10)
account2 = BankAccount("987654321", "Chris", 1000)

print(f"Account 1 - Owner: {account1.get_owner_name()}, Balance: {account1.get_balance()}")
print(f"Account 2 - Owner: {account2.get_owner_name()}, Balance: {account2.get_balance()}")

account1.set_owner_name("Stephen Wirinata")
account2.set_owner_name("Chris Wong")
print(f"Updated Account 1 Owner: {account1.get_owner_name()}")
account1.deposit(200)
account1.withdraw(100)

print(f"\nUpdated Account 1 Owner: {account2.get_owner_name()}")
account2.deposit(500)
account2.withdraw(1200)