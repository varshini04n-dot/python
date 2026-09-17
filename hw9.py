class account:
    def __init__(self, holder_name, balance):
        self._holder_name=holder_name
        self._balance=balance
    def __add__(self, other):
        return self._balance+other._balance
class SavingAccount(account):
    def calculate_interest(self):
        return self._balance*0.05
class CurrentAccount(account):
    def calculate_interest(self):
        return self._balance*0.02
saving_acc=SavingAccount("Ravi",10000)
current_acc=CurrentAccount("Anjali",15000)
print("Saving Account Holder:", saving_acc._holder_name)
print("Current Account Holder:", current_acc._holder_name)
print("Saving Account Balance:", saving_acc._balance)
print("Current Account Balance:", current_acc._balance)
print("Saving Account Interest:", saving_acc.calculate_interest())
print("Current Account Interest:", current_acc.calculate_interest())
print("Total Balance in Saving Account:", saving_acc+ current_acc)