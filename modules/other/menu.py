import os
print('''
-[MENU:Other]-
    1) PGP Functions (NOT YET)
    2) Logic Operation XOR
    3) Logic Operation XNOR
    4) Logic Operation AND
    5) Logic Operation NAND
    6) Logic Operation OR
    7) Logic Operation NOR
    8) Logic Operation NOT
   99) Exit
   ''')
opt = input('\033[1;34m[=]\033[0m Option: ')
if opt == '99':
   exit()
   
elif opt == '1':
    os.system('python3 pgp/menu.py')
elif opt == '2':
    os.system('python3 xor/menu.py')
elif opt == '3':
    os.system('python3 xnor/menu.py')
elif opt == '4':
    os.system('python3 and/menu.py')
elif opt == '5':
    os.system('python3 nand/menu.py')
elif opt == '6':
    os.system('python3 or/menu.py')
elif opt == '7':
    os.system('python3 nor/menu.py')
elif opt == '8':
    os.system('python3 not/menu.py')
else:
    print('\033[1;31m[-]\033[0m Unknown option')
    exit()
