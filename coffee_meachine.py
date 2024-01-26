resources={"water":1000,"milk":500,"coffee":200}
menu={"latte":{
               "Ingredients":{
                   "water":200,
                   "milk":150,
                   "coffee":24
               },
               "cost":150
                },
       "espresso":{
                 "Ingredients":{
                     "water":50,
                     "milk":30,
                     "coffee":20
                 },
                "cost":100
                },
       "cappuccino":{
                 "Ingredients":{
                       "water":256,
                        "milk":100,
                        "coffee":24
                 },
               "cost":200
                }
       }
def check_resources(Ingredients):
    for item in Ingredients:
        if Ingredients[item]>resources[item]:
            print(f"Sorry! there is no enough {item}")
            return False
    else:
        return True
is_on=True
def process_coins():
    five=int(input("Enter how many 5Rs coins:"))
    ten=int(input("Enter how many 10Rs coins:"))
    twenty= int(input("Enter how many 20Rs coins:"))
    fifty = int(input("Enter how many  50Rs coins:"))
    hundred= int(input("Enter how many 100Rs  coins:"))
    Total=five*5+ten*10+twenty*20+fifty*50+hundred*100
    return Total
def is_payment_successfull(money_recived,coffee_cost):
    if money_recived>=coffee_cost:
        change=money_recived-coffee_cost
        print(f"Here is your Rs{change} change collect it")
        return True
    else:
        print("Sorry! not enough money money refunded")
        return False
def make_coffee(coffee_type,Ingredients):
    for items in Ingredients:
        resources[items]-=Ingredients[items]
    print(f"Here is your coffee enjoy it")
while is_on:
    choice=input("What would you like to have:?(latte/espresso/cappuccino)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}ml")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['Ingredients']):
            payment=process_coins()
            if is_payment_successfull(payment,coffee_type['cost']):
                make_coffee(coffee_type,coffee_type['Ingredients'])
