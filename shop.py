def shop():
    choice=input("What would you like to buy? (1=lemon, 2=sugar, 3=ice cubes)\n")
    if choice=="lemons" or "1":
        lemons=int(input("How many lemons do you want to buy?"))
        inventory_dictionary['lemons']+lemons
    elif choice=="sugar"or"2":
        sugar=int(input("How much sugar do you want to buy?"))
        inventory_dictionary['sugar']+sugar
    elif choice=="ice_cubes"or"3":
        ice_cubes=int(input("How many ice_cubes do you want to buy?"))
        inventory_dictionary['ice_cubes']+ice_cubes