from customer_class import Customer
import random
def start_day(recipe, cost, inventory):
    sweetness=recipe['sugar']-recipe['lemons']
    customer_sweetness=0
    customer = Customer()
    bought=0

    if sweetness==0:
        customer_sweetness=0
    elif sweetness==1:
        customer_sweetness=1
    elif sweetness==2:
        customer_sweetness=2
    elif sweetness==3
        customer_sweetness=3
    else:
        customer_sweetness=4
    for I in range(random.randint(15,20))
        if customer['sweetness']==customer_sweetness:
            if recipe['ice']==customer['ice']
                if customer['price']==cost:
    bought+=1
    money+=bought*cost
    inventory['lemons']=-recipe['lemons']*bought
    inventory['sugar']=-recipe['sugar']*bought
    inventory['ice']=-recipe['ice']*bought
    print(bought "customers bought your lemonade.")