# hiding internal  implementation

# class that demonstrates lack of encapsulation ( for educational purposes)
class BadBankAccountWithoutEncapsulation:
    def __init__(self, balance):
        self.balance = balance
account = BadBankAccountWithoutEncapsulation(0.0) 
account.balance =-1
print(account.balance) 

# implenting encapsulation
class BankAccount:
    def __init__(self):
        self._balance = 0.0
    @property
    def balance(self):
        return self._balance    
    def deposit(self, amount):
        if amount <=0:
            raise ValueError (" deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(" withdraw amount must be positive.")
        if amount >= self._balance:
            raise ValueError(" insufficient funds")
        self._balance -= amount

account1 = BankAccount()
print(account1.balance)

try:
    account1.deposit(1000)
    print(account1.balance)
except ValueError as e:
    print(f"ERROR: {e}")    
try:
    account1.withdraw(2000)
    print(account1.balance)
except ValueError as e:
    print(f"ERROR: {e}")
try:
    account1.withdraw(50)
    print(account1.balance)
except ValueError as e:
    print(f"Error: {e}")    
try:
    account1.deposit(300)
    print(account1.balance)
except ValueError as e:
    print(f"ERROR: {e}")    






