from customer_class import Customer
import random
def start_day(recipe, cost, inventory):
    sweetness=recipe['sugar']-recipe['lemons']
    customer = Customer()
    bought=0

    for I in range(random.randint(300,500)):
        if customer['sweetness']==sweetness-1:
            if recipe['ice_cubes']==customer['ice']-1:
                if customer['price']==cost:
                    bought+=1
    money+=bought*cost
    inventory['lemons']=-recipe['lemons']*bought
    inventory['sugar']=-recipe['sugar']*bought
    inventory['ice_cubes']=-recipe['ice_cubes']*bought
    print(bought, "customers bought your lemonade.")