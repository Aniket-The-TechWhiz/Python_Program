#WAP to create student class that takes name ans marks of three subjects as arguments in cunstructor.
#then create a method to print avegrage.

'''class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def getaverage(self):
        sum=(self.m1+self.m2+self.m3)/3
        print(sum)

obj=Student("aniket",2,3,4)
obj.getaverage()'''

#WAP to create account with 2 attribute = Balance and Account no.
#create method for debit ,credit,& balance

class Account :
    def __init__(self,balance,Account_no):
        self.balance=balance
        self.Account_no=Account_no
    
    def credit(self,credit_ammount):
        self.balance+=credit_ammount
        print("Rs.",credit_ammount," is credited")
        print("Total Balance :",self.balance)
        
    def debit(self,debit_ammount):
        self.balance-=debit_ammount
        print("Rs.",debit_ammount," is Debited")
        print("Total Balance :",self.balance)

    def show_balance(self):
        print("Account no :",self.Account_no," \nBalance :",self.balance)

obj=Account(2000,"Mahabank1205")
obj.debit(1000)
obj.credit(2000000)
obj.show_balance()

