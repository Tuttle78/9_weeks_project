import recipies
import shop

day_num=0
money = 0
days=0
inventory_dictionary={"lemons": 0,
                      "sugar": 0,
                      "ice_cubes":0
                      }

def shop(inventory_dictionary):
    choice=input("What would you like to buy? (1=lemon, 2=sugar, 3=ice cubes)\n")
    if choice=="lemons" or choice == "1":
        lemons=int(input("How many lemons do you want to buy?\n"))
        inventory_dictionary['lemons']+=lemons
    elif choice== "sugar" or "2":
        sugar=int(input("How much sugar do you want to buy?\n"))
        inventory_dictionary['sugar']+=sugar
    elif choice=="ice_cubes"or"3":
        ice_cubes=int(input("How many ice_cubes do you want to buy?\n"))
        inventory_dictionary['ice_cubes']+ice_cubes

print("Welcome to the lemonade stand game")
diff_choice = (input("What difficulty are you chosing? (1 = easy, 2 = medium, 3 = hard)\n"))
if diff_choice == "1" or diff_choice == "Easy":
    inventory_dictionary['lemons'] = 500 
    inventory_dictionary['sugar'] = 500
    inventory_dictionary['ice_cubes'] = 400
    money = 2000
    days=42
elif diff_choice == "2" or diff_choice == "Medium":
    inventory_dictionary['lemons'] = 250  
    inventory_dictionary['sugar'] = 250
    inventory_dictionary['ice_cubes'] = 200
    money = 500
    days=28
elif diff_choice == "3" or diff_choice == "Hard":
    inventory_dictionary['lemons'] = 100
    inventory_dictionary['sugar'] = 100
    inventory_dictionary['ice_cubes'] = 50
    money = 200
    days=14
else:
    print("invalid, quitting game")
while day_num<days:
    game_choices = int(input("What would you like to do? (1 = recipe, 2 = start the day, 3 = see inventory, = 4 shop)\n"))
    if game_choices == 3:
        print("You have", inventory_dictionary)
        continue
    elif game_choices == 1:

        recipies.recipe()
    elif game_choices == 4:
        shop.shop()

        print("You have", inventory_dictionary)
    if game_choices == 1:
            recipies.recipe()
    if game_choices == 2:
        day_num+=1
        print("Day", day_num)
        print("Opening your shop")
        print("Shop opened, customers rolling in!")
    if game_choices == 3:
        print("You have", inventory_dictionary)
    if game_choices == 1:
        recipies.recipe()