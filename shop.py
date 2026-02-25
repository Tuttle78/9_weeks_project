# def shop(inventory_dictionary):
from main import inventory_dictionary 
from main import money

choice=input("What would you like to buy? (1: lemon, 2: sugar, 3: ice cubes)\n")

if choice == 1:
    amount = int(input("how many lemons do you want?\n"))
    
    for each in range(1, amount+1):
        inventory_dictionary["lemon"]+1
        money-5

if choice == 2:
    amount_1 = int(input("how much sugar do you want?\n"))

    for each in range(1, amount_1+1):
        inventory_dictionary["sugar"]+1
        money-5

if choice == 3:
    amount_2 = int(input("how many ice cubes do you want?\n"))

    for each in range(1, amount_2+1):
        inventory_dictionary["ice_cubes"]+1
        money-3

print("You got ",amount+amount_1+amount_2,"from Shop and now have",money,"dollars.")