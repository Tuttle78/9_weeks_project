
def shop_screen(inventory):
    choice=input("What would you like to buy? (1: lemon, 2: sugar, 3: ice cubes)\n")

    if choice == "1":
        amount = int(input("how many lemons do you want? ($1 each)\n"))
        
        if inventory["money"] < amount:
            print("You can't afford that.")
        else:
            inventory["money"] -= amount
            inventory['lemons'] += amount


    if choice == "2":
        amount = int(input("how many sugar packs do you want?\n"))
        if inventory["money"] < amount:
            print("You can't afford that.")
        else:
            inventory["money"] -= amount
            inventory['sugar'] += amount

    if choice == "3":
        amount = int(input("how many ice cubes do you want?\n"))
        inventory['ice_cubes'] += amount
        inventory["money"] -= amount*5
