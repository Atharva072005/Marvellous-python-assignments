

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def display_balance(self):
        print("Name : " + self.name)
        print("Account No : " + self.account_number)
        print("Balance : ", self.balance)

def main():
    acc = BankAccount("123456", "Atharva", 5000)
    acc.deposit(2000)
    acc.withdraw(1000)
    acc.display_balance()

if __name__ == "__main__":
    main()
