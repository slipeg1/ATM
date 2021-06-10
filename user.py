class user:
    currency = "USD"
    checking_account = 200.0
    saving_account = 0.0
    wallet = 1000.0
    has_riverside_acc = False

    name = ""
    def __init__(self, name, age):
        user.name = name
        self.age = age

    def print_wallet(self):
        print(format(self.wallet, '.2f'))
    def get_money(self):
        return format(self.wallet, '.2f')
    def get_checking(self):
        return format(self.checking_account, '.2f')
    def get_saving(self):
        return format(self.saving_account, '.2f')
    def get_formated_profile(self):
         formated_output = "[ Name: "+self.name+" | Age: "+str(self.age)+" | Wallet: "+str(self.wallet)+"$"+" ]"
         return formated_output
    def add_money(self, number):
        ""
        ""
    def remove_money(self, number):
        """"""
    def add_checking(self, number):
        self.checking_account += number
        self.wallet -= number
    def remove_checking(self, number):
        self.checking_account -= number
        self.wallet += number
    def add_saving(self, number):
        self.saving_account += number
        self.wallet -= number
    def remove_saving(self, number):
        self.saving_account -= number
        self.wallet += number
