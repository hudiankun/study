class BankAccount:#定义银行账户类
    def __init__(self,acct_number,acct_name):#定义BankAccount属性
        self.acct_number=acct_number
        self.acct_name=acct_name
        self.balance=0.0

        #以下定义BankAccount类的方法
    def displayBalance(self):
        print("The account balance is:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("You deposited",amount)
        print("The new balance is :",self.balance)
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("You withdraw",amount)
            print("The new balance is:",self.balance)
        else:
            print("You tried to withdraw ",amount)
            print("The account balance is:",self.balance)
            print("Withdraw denied. Not enough funds.")

#定义类 BankAccount的子类interestAccount
class interestAccount(BankAccount):
    def  __init__ (self,acct_number,acct_name,rate):
        BankAccount.__init__(self,acct_number,acct_name)
        self.rate=rate
    def addinterest(self):
        interest=self.balance*self.rate
        print("adding interest to the account,",self.rate*100,"percent")
        self.deposit(interest)

#调用子类
myAccount=interestAccount(234567,"Warren Sande",0.11)
print("Account name:",myAccount.acct_name)
print("Account number:",myAccount.acct_number)
myAccount.displayBalance()
myAccount.deposit(34.52)
myAccount.addinterest()
myAccount.withdraw(12.22)
