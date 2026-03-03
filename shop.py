
def shop_screen(inventory):
    choice=input("What would you like to buy? (1: lemon, 2: sugar, 3: ice cubes)\n")

    if choice == "1":
        amount = int(input("how many lemons do you want?\n"))
        inventory['lemons'] += amount
        if inventory["money"] < amount*5:
            print("You can't afford that.")
        else:
            inventory["money"] -= amount*5
    


    if choice == "2":
        amount = int(input("how much sugar do you want?\n"))
        inventory['sugar'] += amount
        inventory["money"] -= amount*5


    if choice == "3":
        amount = int(input("how many ice cubes do you want?\n"))
        inventory['ice_cubes'] += amount
        inventory["money"] -= amount*5
