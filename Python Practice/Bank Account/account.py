class Account:
    
    def __init__(self, filepath):
        self.filepath = filepath
        
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Rs {amount} has been Withdrawn from your account, Balance: {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Rs {amount} has been Deposited to your account, Balance: {self.balance}")
    
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            
# Class Definition ends here  
acc = Account('balance.txt')
print(f"Initial Balance: {acc.balance}")
acc.deposit(1000)
acc.withdraw(500)
print(acc.balance)
acc.commit()
