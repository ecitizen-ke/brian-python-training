# static attributes
class User:
    user_count = 0
    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count +=1
    def display_user(self):    
        print(f"username: {self.username}, email: {self.email}")

user1 = User("Ian", "ian@gmail.com")  
 
print(User.user_count)  
print(user1.user_count)

class BankAcount:
    def __init__(self, id, account_no, name, balance=0):
        self.id= id 
        self.account_no = account_no
        self.name = name
        self.balance = balance
    def deposit(self,amount, transaction_type ="deposit"):
        self.amount= amount
        if amount > 0:
            self.balance+=amount 
            self.transaction_type = transaction_type
            print (f"{self.name}'s new balance is: {self.balance}")
        else:
            print("deposit amount must be positive")   
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
    def log_transaction(self):
        print(f"Logging {self.transaction_type} of ${self.amount} New balance: ${self.balance}")

account1 = BankAcount(12345, 123, "yator", 1000) 
print(account1.deposit(100)) 
print(account1.is_valid_interest_rate(2))
print(account1.is_valid_interest_rate(20))
print(account1.log_transaction())




