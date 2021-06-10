import time
import os
import util
import decimal
class atm:
    def atm_intro(self):
        util.print_wait_clr("Welcome, to the riverside national bank!", 2)
    def first_menu(self):
        input("Please insert your debit card (Press Enter)")
        os.system("cls")
        print("Card inserted, thank you for choosing us!")
        time.sleep(2)

    def fake_loading(self):
        load_seq = ["Connecting to network", "Getting public key", "Comparing",
                    "Public and private keys compared", "Sending results to server", "waiting for server response",
                    "Everything checks up", "Connecting", "Connected successfully",
                    "Connecting to database", "Loading user experience"]

        seq_time = [0.5, 0.9, 0.5, 1, 0.6, 2, 1, 3, 0.4, 0.7, 1.5]

        i = 0
        while i < len(seq_time):
            print(load_seq[i]+"...")
            time.sleep(seq_time[i])
            i = i+1

        os.system("cls")
        util.print_wait_clr("You're connected to the Riverside National bank ATM", 4)
    #---------------------- MAIN MENU ---------------------------------------

    def main_menu(self, user):
        if user.has_riverside_acc == False:
            util.print_wait_clr("no account was found associated to this card", 3)
            util.print_wait_clr("we will proceed to the creation of your riverside account.", 4)
            util.print_wait_clr("generating-profile...", 0.5)
            util.print_wait_clr("profile generated successfully", 1)
            user.has_riverside_acc = True
            util.print_wait_clr("Launching...", 2)
            self.main_menu(user)
        else:
            os.system("cls")
            print("       _______________________________")
            print(">>>>>>| Welcome to Riverside Bank ATM |-----------*")
            print("      '-------------------------------'\n")
            print("  " + "~ Checking Account: [" + user.get_checking() + "$" + " (" + str(user.currency) + ")] ~")
            print("  " + "~ Saving Account: [" + user.get_saving() + "$" + " (" + str(user.currency) + "] ~\n")
            print(" "+user.get_formated_profile())
            print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*~>")
            print("What do you want to do?\n1. Withdraws\n2. Deposit\n3. Exit")
            input_choice = int(input())
            if input_choice == 1:
                withdraw_choice = 0

                while True:
                    os.system("cls")
                    print(user.get_formated_profile())
                    print("Which account do you want to withdraw from ?")
                    print("1. Checking account \n2. Saving Account\n3. Exit")
                    try:
                        withdraw_choice = decimal.Decimal(input())
                    except:
                        print("wrong input")
                    if withdraw_choice == 1:
                        while True:
                            print(user.get_formated_profile())
                            number_choice = input("How much you want to withdraw: ")
                            if number_choice.isdigit() and user.get_checking() >= number_choice:
                                user.remove_checking(float(number_choice))
                                break
                            else:
                                print("not enough money in the checking account.")
                                break
                    elif withdraw_choice == 2:
                          while True:
                            print(user.get_formated_profile())
                            number_choice = input("How much you want to withdraw: ")
                            if number_choice.isdigit() and user.get_saving() >= number_choice:
                                user.remove_saving(float(number_choice))
                                break
                            else:
                                print("not enough money in the saving account.")
                    elif withdraw_choice == 3:
                        self.main_menu(user)
                    else:
                        continue
            elif input_choice == 2:
                while True:
                    os.system("cls")
                    print(user.get_formated_profile())
                    print("-------------------------------------------------------")
                    print("Which account do you want to deposit from ?")
                    print("1. Checking account \n2. Saving Account\n3. Exit")
                    try:
                        deposit_choice = decimal.Decimal(input())
                    except:
                        print("wrong input")
                    if deposit_choice == 1:
                        while True:
                            os.system("cls")
                            print(user.get_formated_profile())
                            number_choice = input("How much you want to deposit: ")
                            if number_choice.isdigit() and float(user.get_money()) >= float(number_choice):
                                user.add_checking(float(number_choice))
                                break
                            else:
                                if number_choice.isdigit():
                                    print("Not enough money")
                                    time.sleep(2)
                                    break
                                else:
                                    print("Wrong input")
                                    time.sleep(2)
                    elif deposit_choice == 2:
                        while True:
                            os.system("cls")
                            print(user.get_formated_profile())
                            print("-------------------------------------------------------")
                            number_choice = input("How much you want to deposit: ")
                            if number_choice.isdigit() and float(user.get_money()) >= float(number_choice):
                                user.add_saving(float(number_choice))
                                break
                            else:
                                if number_choice.isdigit():

                                    print("Not enough money")
                                    time.sleep(2)
                                    break
                                else:
                                    print("Wrong input")
                                    time.sleep(2)
                    elif deposit_choice == 3:
                        self.main_menu(user)
                    else:
                        continue
            elif input_choice == 3:
                self.main_menu(user)
            else:
                self.main_menu(user)
                
    def init(self, user):
        self.atm_intro()
        self.first_menu()
        self.fake_loading()
        self.main_menu(user)