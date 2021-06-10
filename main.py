import time
import os
import ATM
import decimal
import user
#The idea is to basically make an ATM
#might end up in a fully fledged city rpg who knows

manu = user.user("manu", 23)

manu.print_wallet()
ATM = ATM.atm()
ATM.init(manu)