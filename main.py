from recipe import game_recipe
from shop import shop_screen
recipe={
    "lemons":0,
    "sugar":0,
    "ice_cubes":0  
    }
cost=0
goal=0
day_num=0
money=0
days=0
inventory_dictionary={"lemons": 0,
                      "sugar": 0,
                      "ice_cubes" : 0,
                      }

print("Welcome to the lemonade stand game")
diff_choice = (input("What difficulty are you chosing? (1 = easy, 2 = medium, 3 = hard)\n"))
if diff_choice == "1" or diff_choice == "Easy":
    inventory_dictionary['lemons'] = 500
    inventory_dictionary['sugar'] = 500
    inventory_dictionary['ice_cubes'] = 400
    money = 60
    goal=300
    days=42

elif diff_choice == "2" or diff_choice == "Medium":
    inventory_dictionary['lemons'] = 250  
    inventory_dictionary['sugar'] = 250
    inventory_dictionary['ice_cubes'] = 200
    money = 500
    days=28
    goal =500
elif diff_choice == "3" or diff_choice == "Hard":
    inventory_dictionary['lemons'] = 100
    inventory_dictionary['sugar'] = 100
    inventory_dictionary['ice_cubes'] = 50
    money = 200
    days=21
    goal=500
else:
    print("invalid, quitting game")

while day_num<days:
    if money>= goal:
        print("You Win!")
        break
    if money<=0:
        print("You went bankrupt.")
    game_choices = int(input("What would you like to do? (1 = recipe, 2 = start the day, 3 = see inventory | 4 = shop)\n"))
    if game_choices == 3:
        print("You have", inventory_dictionary, "and $"+ str(money))

    if game_choices == 4:
        shop_screen(inventory_dictionary, money)
    
    if game_choices == 2:
        day_num+=1
        print("Day", day_num)
        print("Opening your shop")
        print("Shop opened, customers rolling in!")

    if game_choices == 1:
        game_recipe(recipe, cost)