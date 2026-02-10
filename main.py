import shop
money=0
print("Welcome to the lemonade stand game")
diff_choice = (input("What difficulty are you chosing 1. easy 2. medium 3. hard:\n"))
if diff_choice == 1 or "easy" or "Easy":
    shop.ingredients(500, 500, 450)
    money=2000
if diff_choice == 2 or "medium" or "Medium":
    shop.ingredients(250, 250, 200)
    money=500
if diff_choice == 3 or "hard" or "Hard":
    shop.ingredients(100, 100, 50)
    money=200
game_choices = int(input("What would you like to do 1. recipe 2. start the day 3. see inventory 4. shop:\n"))
if game_choices == 3:
    print("You have",shop.ingredients)