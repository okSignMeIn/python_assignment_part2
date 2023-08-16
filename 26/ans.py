class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address


class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions


class BankManager:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, customer_id, name, address):
        customer = Customer(customer_id, name, address)
        self.customers.append(customer)
        return customer

    def create_account(self, account_number, customer):
        account = Account(account_number, customer)
        self.accounts.append(account)
        return account

bank_manager = BankManager()
customer = bank_manager.create_customer(1, "John Doe", "123 Main St")
account = bank_manager.create_account(1001, customer)

account.deposit(1000)
account.withdraw(200)
print(account.get_balance())
print(account.get_transaction_history())
