import math

class BankAccount:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount - 2*(math.floor(amount/100))  # odejmuje 2 za każde
        # 100

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Operation impossible')

    def change_ownership(self, new_owner: str):
        self.owner = new_owner

    def __str__(self):  # zamiast display()
        return (f'This is account number {self.number} belonging to {self.owner} and '
                f'credited with PLN {self.balance}.')

def main():
    some_account = BankAccount(123456789, 'John Smith', 4200)
    print(some_account)

    some_account.deposit(450)
    print(some_account)

    some_account.withdraw(5000)
    some_account.withdraw(4000)
    print(some_account)

    some_account.change_ownership('Anna Smith')
    print(some_account)

if __name__ == '__main__':
    main()