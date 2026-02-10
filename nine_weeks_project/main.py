import shop
import customer

try:
    money=int(input("How much money would you like to start with? \n"))
    print(shop.ingredients(0, 0, 0))
except TypeError:
    input("Sorry i didnt get that")
else:
    start = input("Would you like to start the day? \n")

if start == "yes":
    input("Great!")
    print("--DAY 1-- \n")
    print(shop.ingredients(0, 0, 0))    
    input(customer.customer)