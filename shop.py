
def shop_screen(inventory, cash):
    print(f"You have ${cash}.")
    choice=input("What would you like to buy? (1: lemon, 2: sugar, 3: ice cubes)\n")

    if choice == "1":
        amount = int(input("how many lemons do you want? ($1 each)\n"))
        
        if cash < amount:
            print("You can't afford that.")
        else:
            cash -= amount
            inventory['lemons'] += amount


    if choice == "2":
        amount = int(input("how many sugar packs do you want? (50 cents each)\n"))
        if cash < amount*0.5:
            print("You can't afford that.")
        else:
            cash -= amount*0.5
            inventory['sugar'] += amount

    if choice == "3":
        amount = int(input("how many ice cubes do you want? (10 cents each)\n"))
        if cash < amount*0.1:
            print("You can't afford that.")
        else:
            cash -= amount*0.1
            inventory['ice_cubes'] += amount
    print(f"You now have ${cash}, {inventory['lemons']} lemons, {inventory['sugar']} sugar, & {inventory['ice_cubes']} ice cubes.")
