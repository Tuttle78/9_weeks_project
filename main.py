import shop
import recipies

money = 0

inventory_dictionary={"lemons": 0,
                      "sugar": 0,
                      "ice_cubes":0
                      }
money=0
print("Welcome to the lemonade stand game")
diff_choice = (input("What difficulty are you chosing 1. easy 2. medium 3. hard:\n"))
if diff_choice == 1 or "easy" or diff_choice == "Easy":
    inventory_dictionary['lemons'] = 500 ['sugar'] = 500 ['ice_cubes'] = 400
    money = 2000
if diff_choice == 2 or "medium" or diff_choice == "Medium":
    inventory_dictionary['lemons'] = 250 ['sugar'] = 250 ['ice_cubes'] = 200
    money = 500
if diff_choice == 3 or "hard" or diff_choice == "Hard":
    inventory_dictionary['lemons'] = 100 ['sugar'] = 100 ['ice_cubes'] = 50
    money = 200

game_choices = int(input("What would you like to do 1. recipe 2. start the day 3. see inventory 4. shop:\n"))
if game_choices == 3:
    print("You have",shop.ingredients)
if game_choices == 1:
    game_recipe_1 = int(input("How much lemons do you want for each cup:\n"))
    game_recipe_2 = int(input("How much sugar do you want for each cup:\n"))
    game_recipe_3 = int(input("How much ice cubes do you want for each cup:\n"))
    recipe.recipe(game_recipe_1, game_recipe_2, game_recipe_3)
    print("You have",shop.ingredients())
