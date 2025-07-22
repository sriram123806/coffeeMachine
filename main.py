logo = """
        __________________
        |                |''''''
         |    COFFEE    |     ' 
          |            |     '
           |__________|'''''
           |__________|
           
  """

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
price = 0
def amount(user_paid,choosed_order):
    if user_paid > MENU[choosed_order]["cost"]:
        a_1 = user_paid - MENU[choosed_order]["cost"]
        print(f"cost of order : ${MENU[choosed_order]["cost"]}")
        print(f"your balance amount : ${a_1}")

    elif user_paid < MENU[choosed_order]["cost"]:
        print(f"cost of order : ${MENU[choosed_order]["cost"]}")
        print("sorry!!its not enough amount")
        print("*****************************THANK YOU*****************************")
        return

def gameplay(selected_item):
    water_used = MENU[selected_item]["ingredients"].get("water",0)
    milk_used = MENU[selected_item]["ingredients"].get("milk",0)
    coffee_used = MENU[selected_item]["ingredients"].get("coffee",0)
    if water_used < resources["water"]:
        n = resources["water"] - water_used
        resources["water"] = n
        if resources["water"] <= 0 :
            resources["water"] = 0
            print("sorry!! there is not sufficient amount of ingredients")
            print("*****************************THANK YOU*****************************")

    elif milk_used < resources["milk"]:
        m = resources["milk"] - milk_used
        resources["milk"] = m
        if resources["milk"] <= 0 :
            resources["milk"] = 0
            print("sorry!! there is not sufficient amount of ingredients")
            print("*****************************THANK YOU*****************************")

    elif coffee_used < resources["coffee"]:
        k = resources["coffee"] - milk_used
        resources["coffee"] = k
        if  resources["coffee"] <= 0 :
            resources["coffee"] = 0
            print("sorry!! there is not sufficient amount of ingredients")
            print("*****************************THANK YOU*****************************")

project = True
while project:
    print("*****************************WELCOME*****************************")
    print(logo)
    select = input("select your need!! (espresso/latte/cappuccino) : ").lower()
    if select == "espresso" or select == "latte" or select == "cappuccino":
        print("please enter your amount")
        penny = int(input("enter penny :")) * 0.01
        nickel = int(input("enter nickel :")) * 0.05
        dine = int(input("enter dine :")) * 0.10
        quarter = int(input("enter quarter :")) * 0.25
        total = penny + nickel + dine + quarter
        print(f"your total amount : ${total}")
        price += MENU[select]["cost"]
        amount(total,select)
        gameplay(select)

    Report = input("do you need report,type yes or no : ").lower()
    if Report == "yes":
        print(f"water:{resources["water"]}")
        print(f"milk:{resources["milk"]}")
        print(f"coffee:{resources["coffee"]}")
        print(f"money:${price}")
    else:
        print("*****************************THANK YOU*****************************")

    again = input("do you need anything else : yes or no : ").lower()
    if again == "yes":
        project = True

    elif resources["water"] <= 0 and resources["milk"] <= 0 and resources["coffee"] <= 0 :
        project = False
        print("\n" * 20)
        print("sorry!! there is not sufficient amount of ingredients")
        print(f"your total amount :${price}")
        print("*****************************THANK YOU*****************************")

    else:
        project = False
        print("\n"*20)
        print(f"your total amount :${price}")
        print("*****************************THANK YOU*****************************")









