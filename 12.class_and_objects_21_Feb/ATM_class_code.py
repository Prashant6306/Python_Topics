class BankATM:
    def __init__(self):
        self.secret_code = ''
        self.account_bal  = 0
        self.show_menu()  # auto-call!

    def show_menu(self):
        choice = input('''
        Welcome! Choose an option:
        1. Create PIN
        2. Change PIN
        3. Check Balance
        4. Withdraw Cash
        5. Exit
        Your choice: ''')
        if choice == '1':
            self.set_pin()
        elif choice == '2':
            self.update_pin()
        elif choice == '3':
            self.check_balance()
        elif choice == '4':
            self.do_withdraw()
        elif choice == '5':
            exit()

    def set_pin(self):
        c = input('New PIN: ')
        self.secret_code = c
        b = input('Opening bal: ')
        self.account_bal = int(b)
        print('PIN created!')
        self.show_menu()

    def update_pin(self):
        cur = input('Current PIN: ')
        if cur == self.secret_code:
            nw = input('New PIN: ')
            self.secret_code = nw
            print('PIN updated!')
        else:
            print('Wrong PIN!')
        self.show_menu()
    
    def check_balance(self):
        p = input('PIN: ')
        if p == self.secret_code:
            print('Bal:',self.account_bal)
        else:
            print('Wrong PIN!')
        self.show_menu()

    def do_withdraw(self):
        p = input('PIN: ')
        if p == self.secret_code:
            a = int(input('Amount: '))
            if a <= self.account_bal:
                self.account_bal = self.account_bal - a
                print('Done! Bal:',self.account_bal)
            else: print('Insufficient!')
        else: print('Wrong PIN!')
        self.show_menu()

obj1=BankATM()
obj1.set_pin()

def sum():
    pass

sum()
