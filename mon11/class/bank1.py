class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
class SavingsAccount(Bank):
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
class CheckingAccount(Bank):
    def __init__(self, name, balance=0, overdraft_limit=500):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False
# Example usage:
savings = SavingsAccount("Alice", 1000)
savings.deposit(500)
savings.add_interest()
print(f"Savings Account Balance for {savings.name}: {savings.get_balance()}")
checking = CheckingAccount("Bob", 500)
checking.withdraw(800)
print(f"Checking Account Balance for {checking.name}: {checking.get_balance()}")
