class Bank:
    def __init__(self,balance):
        self.balance=balance
        
    def getdata(self):
        name=input("Enter Account Holder Name: ")
        self.name=name
        account_no=input("Enter Account Number: ")
        self.account_no=account_no
        account_type=input("Enter Account Type: ")
        self.account_type=account_type
        
    def displaydata(self):
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.account_no}")
        print(f"Account Type: {self.account_type}")      
        print(f"Current Balance: {self.balance}")
            
    def deposit(self):
        amount=int(input("Enter amount to deposit: "))
        self.balance+=amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        
    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if amount>self.balance:
            print("Insufficient funds")
        else:
            self.balance-=amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
acc1=Bank(1000)
acc1.getdata()
while True:
    print("\n1. Display Account Details\n2. Deposit\n3. Withdraw\n4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        acc1.displaydata()
    elif choice==2:
        acc1.deposit()
    elif choice==3:
        acc1.withdraw()
    elif choice==4:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")                    