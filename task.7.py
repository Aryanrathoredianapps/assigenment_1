class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def Deposit(self , a):
         self.balance = self.balance + a
    
    def Withdrawal(self , d):
    
            self.balance = self.balance - d
    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance )



newAccount = BankAccount(1234567891, "Aryan" , 9700)
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.display()
