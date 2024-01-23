import os

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
            "coffee": 54,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 80,
}


def start():
    on = True
    money = 0
    CLEAR = os.system('cls')

    def calc_resource(ingredient):
        for _ in ingredient:
            if ingredient[_] > resources[_]:
                _ = input(f"Sorry there is not enough {_}.\n press enter to continue: ")
                return False
        return True

    def coins():
        print("Please, insert coins:")
        quarters = float(input("Quarters($0.25): ")) * 0.25
        dimes = float(input("Dimes($0.10): ")) * 0.10
        nickles = float(input("Nickles($0.05): ")) * 0.05
        pennies = float(input("Pennies($0.01): ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total

    def calc_money(cost, bank):
        if bank > cost:
            dif2 = bank - cost
            change = input(f"You change is ${dif2}. Type 1 to get it or 2 to keep in credits:\n").lower()
            if change == "1":
                print(f"Here, take your coins ${dif2}")
                return 0
            else:
                return dif2
        if bank < cost:
            dif = cost - bank 
            print(f"You need to deposit more ${dif}")
            while coins() < dif:
                print(f"No enough money, ${dif} refunded.")
        else:
            return 0

    def report():
        for _ in resources:
            print(_, resources[_])
        print(f"Money = ${money}")

    def make_coffee(coffee, ingredients):
        for _ in ingredients:
            resources[_] -= ingredients[_]
        print(f"Enjoy your {coffee}")

    while on:
        choice = input("What would you like?\nEspresso - $1.5\nLatte - $2.5\nCappuccino - $3.0\Type 'H' to help:\n").lower()
        if choice == "h":
            choice = input("Type 'off' to maintenance or 'report' to check resources:\n")
        if choice == "off":
            CLEAR
            print("Maintenance")
            on = False
        elif choice == "report":
            CLEAR
            report()
            x = input("Press enter to continue: ")
            if x == "" or x != "":
                CLEAR
        elif choice == "cappuccino" or choice == "espresso" or choice == "latte":
            product = MENU[choice]
            if calc_resource(product["ingredients"]):
                money += coins()
                money = calc_money(product["cost"],money)
                make_coffee(choice, product["ingredients"])

start()



