class Person:
    def __init__(self,id,first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f"{self.id}, {self.first_name},{self.last_name}")


class Account:
    def __init__(self,number,type,owner,balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return(f"{self.number},{self.type},{self.owner},{self.balance}")


class Bank:
    def __init__(self):
        self.customer = []
        self.account = []

    def add_customer(self,customer):
        # self.customer = customer
        self.customer.append(customer)

    def add_account(self,customer,account):
        if customer in self.customer:
            self.account.append(account)
        else:
            print("Check the name")

    def remove_account(self,account):
        self.account.remove(account)
    def balance_inquiry(self,account):

        acct_index = self.account.index(account)
        acct = self.account[acct_index]
        print(acct.balance)
    def withdrawal(self,account,withdraw_amount):
        acct_index = self.account.index(account)
        acct = self.account[acct_index]
        self.account.remove(account)
        acct.balance = acct.balance - withdraw_amount
        self.account.append(acct)
    def deposit(self,account,deposit_amount):
        acct_index = self.account.index(account)
        acct = self.account[acct_index]
        self.account.remove(account)
        acct.balance = acct.balance + deposit_amount
        self.account.append(acct)
Person1 = Person(1,"John","Smith")
print(Person1)
Account1 = Account(1,"Saving",Person1,1000)
print(Account1)
Bank1 = Bank()
Bank1.add_customer(Person1)
Bank1.add_account(Person1,Account1)


Bank1.balance_inquiry(Account1)
Bank1.deposit(Account1,200)
Bank1.balance_inquiry(Account1)
Bank1.withdrawal(Account1,50)
Bank1.balance_inquiry(Account1)
Bank1.remove_account(Account1)




