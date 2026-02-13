import main

def recipe():
    recipe=[]
    recipe.append(int(input("How many lemons do you want for each cup:\n")))
    recipe.append(int(input("How much sugar do you want for each cup:\n")))
    recipe.append(int(input("How many ice cubes do you want for each cup:\n")))
    if recipe(0) == 1000 or recipe(1) == 1000 or recipe(2) == 1000:
        print("You have too much lemons, sugar, or icecubes")
    print("Your recipe is\n", recipe)

        
    

        