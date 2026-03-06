
def game_recipe(recipe, cost):
    
    while True:
        recipe['lemons']=int(input("How many lemons do you want for each cup? (1-4)\n"))
        if recipe['lemons']<=0 or recipe['lemons']>4:
            print(f"Invalid, try again.")
            continue
        else:
            recipe['sugar']=int(input("How much sugar do you want for each cup:\n"))
            if recipe['sugar']<=0 or recipe['sugar']>4:
                print(f"Invalid, try again.")
                continue
            else:
                recipe['ice_cubes']=int(input("How many ice cubes do you want for each cup:\n"))
                if recipe['ice_cubes']<=0 or recipe['ice_cubes']>4:
                    print(f"Invalid, try again.")
                    continue
                else:
                    cost=input(f"How much would you like to sell your lemonade? {recipe['lemons']} lemons, {recipe['sugar']} sugar packs, and {recipe['ice_cubes']} ice cubes, costs ${recipe['lemons']+recipe['sugar']*0.5+recipe['ice_cubes']*0.1}.")
                    break
    

        