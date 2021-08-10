from random import sample
import sqlite3


class BankingSystem:
    def __init__(self):
        self.cards = None
        self.database()

    @staticmethod
    def database():
        with sqlite3.connect('card.s3db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS card (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL UNIQUE,
            pin TEXT NOT NULL,
            balance INTEGER DEFAULT 0 NOT NULL
            );''')

    @staticmethod
    def database_requests(From=None, to=None, amount=None, pin=None, action=False, close=False) -> None:
        with sqlite3.connect('card.s3db') as data:
            cursor = data.cursor()
            if From and to:
                cursor.execute('''
                UPDATE card SET balance = balance + ? WHERE number = ?;
                            ''', [amount, to])
                cursor.execute('''
                UPDATE card SET balance = balance - ? WHERE number = ?;
                            ''', [amount, From])
            elif From and amount:
                cursor.execute('''
                UPDATE card SET balance = balance + ? WHERE number = ?; 
                            ''', [amount, From])
            elif to:
                return cursor.execute('''
                SELECT number FROM card WHERE number = ?;
                            ''', [to]).fetchone()
            elif From and action:
                return cursor.execute('''
                SELECT balance FROM card WHERE number = ?;
                            ''', [From]).fetchone()
            elif From and pin:
                cursor.execute('''
                INSERT INTO card(number, pin) VALUES(?, ?);
                            ''', [From, pin])
            elif From and close:
                cursor.execute('''
                DELETE FROM card WHERE number = ?;
                               ''', [From])
            else:
                return cursor.execute('''SELECT pin FROM card WHERE number = ?;
                            ''', [From]).fetchone()

    def menu(self) -> None:
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            choice = input()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.login()
            elif choice == '0':
                print('Bye!')
                exit()
            else:
                print('Unknown option')

    def account(self, card) -> None:
        while True:
            print('1. Balance\n2. Add funds\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
            choice = input()
            if choice == '1':
                print(f"\nBalance: {BankingSystem.database_requests(From=card, action=True)[0]}\n")
            if choice == '2':
                print('Enter deposited amount:')
                self.database_requests(From=card, amount=int(input()))
                print('\nAmount added\n')
            elif choice == '3':
                new_card = input('Enter card number:\n')
                if card == new_card:
                    print('You can\'t transfer money to the same account!\n')
                elif not BankingSystem.luhn_algorithm(new_card):
                    print('You probably made a mistake in the card number. Please try again!\n')
                elif not BankingSystem.database_requests(to=new_card):
                    print('Such card does not exist.\n')
                else:
                    new_balance = int(input('Enter how much money you want to transfer:\n'))
                    if new_balance > BankingSystem.database_requests(From=card, action=True)[0]:
                        print('\nNot enough money\n')
                    else:
                        BankingSystem.database_requests(card, new_card, new_balance)
                        print('\nSuccess!\n')
            elif choice == '4':
                BankingSystem.database_requests(From=card, close=True)
                print('\nThe Account has been closed!\n')
                return
            elif choice == '5':
                self.menu()
            elif choice == '0':
                print('Bye!')
                exit()

    def login(self) -> None:
        card = input('Enter your card number:\n')
        PIN = input('Enter your PIN:\n')

        try:
            if BankingSystem.database_requests(From=card)[0] == PIN:
                print('You have successfully logged in!\n')
                self.account(card)
            else:
                print('Wrong card number or PIN\n')
        except TypeError:
            print('Wrong card number or PIN\n')

    @staticmethod
    def luhn_algorithm(card) -> bool:
        processing_card = []
        for index, digit in enumerate(card):
            if index % 2 == 0:
                double_digit = int(digit) * 2
                if double_digit > 9:
                    double_digit -= 9

                processing_card.append(double_digit)
            else:
                processing_card.append(int(digit))

        return True if sum(processing_card) % 10 == 0 else False

    @staticmethod
    def generate_numbers() -> tuple:
        while True:
            random_card = '400000' + ''.join([str(n) for n in sample(range(9), 9)]) + '3'
            random_PIN = ''.join([str(n) for n in sample(range(9), 4)])
            if BankingSystem.luhn_algorithm(random_card):
                if random_card == BankingSystem.database_requests(to=random_card):
                    continue
                else:
                    BankingSystem.database_requests(From=random_card, pin=random_PIN)
                    yield random_card, random_PIN
            else:
                continue

    def create_account(self) -> None:
        card, PIN = next(self.generate_numbers())
        print('\nYour card has been created')
        print(f'Your card number:\n{card}')
        print(f'Your card PIN:\n{PIN}\n')


BankingSystem().menu()