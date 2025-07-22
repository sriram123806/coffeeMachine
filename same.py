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


def used_resource(resources):
    print(f"water:{resources["water"]}")
    print(f"milk:{resources["milk"]}")
    print(f"coffee:{resources["coffee"]}")


def gameplay(selected):
    water_used = MENU[selected]["ingredient"]["water"]
    milk_used = MENU[selected]["ingredient"]["milk"]
    coffee_used = MENU[selected]["ingredient"]["coffee"]
    if water_used < resources["water"]:
        n = resources["water"] - water_used
        resources["water"] = n

    elif milk_used < resources["milk"]:
        m = resources["milk"] - milk_used
        resources["milk"] = m

    elif coffee_used < resources["coffee"]:
        k = resources["coffee"] - milk_used
        resources["coffee"] = k

    else:
        return


def amount(user_paid):
    if user_paid > MENU["espresso"]["cost"]:
        a_1 = user_paid - MENU["espresso"]["cost"]
        print(f"your balance amount : {a_1}")

    elif user_paid > MENU["latte"]["cost"]:
        a_2 = user_paid - MENU["latte"]["cost"]
        print(f"your balance amount : {a_2}")

    elif user_paid > MENU["cuppuccino"]["cost"]:
        a_3 = user_paid - MENU["cuppuccino"]["cost"]
        print(f"your balance amount : {a_3}")

    elif user_paid < MENU["espresso"]["cost"]:
        print("sorry!!its not enough amount")

    elif user_paid < MENU["latte"]["cost"]:
        print("sorry!!its not enough amount")

    elif user_paid < MENU["cuppuccino"]["cost"]:
        print("sorry!!its not enough amount")


def money():
    print("please enter your amount")
    penny = int(input("enter penny :")) * 0.01
    nickel = int(input("enter nickel :")) * 0.05
    dine = int(input("enter dine :")) * 0.10
    quarter = int(input("enter quarter :")) * 0.25
    total = round((penny + nickel + dine + quarter), 2)
    print(f"your total amount : {total}")
    amount(total)


project = True
while project:
    print("*****************************WELCOME*****************************")

    select = input("select your need!! (espresso/latte/cuppuccino) : ")
    if select == "espresso" or select == "latte" or select == "cuppuccino":
        price += MENU[select]["cost"]
        money()
        gameplay(select)

        Report = input("do you need report,type yes or no : ")
        if Report == "yes":
            print(f"water:{resources["water"]}")
            print(f"milk:{resources["milk"]}")
            print(f"coffee:{resources["coffee"]}")
            print(f"money:{price}")

    else:
        print("\n" * 30)
        print("**************************THANK YOU***************************")



