from typing import Dict, List
from models import Customer, Account, Transaction

class Bank:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.accounts: Dict[str, Account] = {}
        self.transactions: Dict[str, Transaction] = {}

    def add_customer(self, name: str) -> Customer:
        customer = Customer(name)
        self.customers[customer.id] = customer
        return customer

    def get_customers(self) -> List[Customer]:
        return list(self.customers.values())

    def open_account(self, customer_id: str, initial_balance: float = 0.0) -> Account:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        account = Account(customer_id, initial_balance)
        self.accounts[account.id] = account
        self.customers[customer_id].accounts.append(account.id)
        return account

    def get_account(self, account_id: str) -> Account:
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id]

    def deposit(self, account_id: str, amount: float) -> Transaction:
        account = self.get_account(account_id)
        account.balance += amount
        transaction = Transaction(account_id, amount, 'deposit')
        self.transactions[transaction.id] = transaction
        account.transactions.append(transaction.id)
        return transaction

    def withdraw(self, account_id: str, amount: float) -> Transaction:
        account = self.get_account(account_id)
        if account.balance < amount:
            raise ValueError("Insufficient funds")
        account.balance -= amount
        transaction = Transaction(account_id, amount, 'withdraw')
        self.transactions[transaction.id] = transaction
        account.transactions.append(transaction.id)
        return transaction

    def get_customer_accounts(self, customer_id: str) -> List[Account]:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return [self.accounts[acc_id] for acc_id in self.customers[customer_id].accounts]

    def get_account_transactions(self, account_id: str) -> List[Transaction]:
        account = self.get_account(account_id)
        return [self.transactions[tid] for tid in account.transactions]