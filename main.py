import shop
import recipies

money = 0
inventory_dictionary={"lemons": 0,
                      "sugar": 0,
                      "ice_cubes":0
                      }

print("Welcome to the lemonade stand game")
diff_choice = (input("What difficulty are you chosing 1. easy 2. medium 3. hard:\n"))
if diff_choice == 1 or "easy" or diff_choice == "Easy":
    inventory_dictionary['lemons'] = 500 
    inventory_dictionary['sugar'] = 500
    inventory_dictionary['ice_cubes'] = 400
    money = 2000
elif diff_choice == 2 or "medium" or diff_choice == "Medium":
    inventory_dictionary['lemons'] = 250  
    inventory_dictionary['sugar'] = 250
    inventory_dictionary['ice_cubes'] = 200
    money = 500
elif diff_choice == 3 or "hard" or diff_choice == "Hard":
    inventory_dictionary['lemons'] = 100  
    inventory_dictionary['sugar'] = 100
    inventory_dictionary['ice_cubes'] = 50

    money = 200

game_choices = int(input("What would you like to do? (1=recipe, 2=start the day, see inventory, 4=shop:\n"))
if game_choices == 3:
        print("You have", inventory_dictionary)
if game_choices == 1:
        recipies.recipe()
if game_choices == 2:
        start = input("Starting the day, would you like to open the shop?\n")

if start == "yes":
      input("Opening your shop")
      input("Shop opened, customers rolling in!")
