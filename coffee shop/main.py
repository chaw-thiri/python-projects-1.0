from art import logo
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}
resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 1000,
}
coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
total_money = 0


def coffee():
    # else:
    #     return 'I think you clicked something wrong. please try again.'
    required_coffee = MENU[coffee_type]['ingredients']['coffee']
    required_milk = MENU[coffee_type]['ingredients']['milk']
    required_water = MENU[coffee_type]['ingredients']['water']
    if (resources['water'] >= required_water
            and resources['milk'] >= required_milk
            and resources['coffee'] >= required_coffee):
        cash(required_coffee, required_milk, required_water)
    else:
        print('I am sorry.😢 There is no enough ingredients for your coffee.')
        print('Please choose another type.')


def report():
    print(f"Total money is : {total_money}")
    print(f'Remaining water : {resources["water"]} ml')
    print(f'remaining coffee seeds {resources["coffee"]} seeds.')
    print(f'Remaining milk {resources["milk"]} ml.')


def cash(required_coffee, required_milk, required_water):
    print('Please insert coins.')
    cash_quarters = float(input('No of quarters : ')) * 0.25
    cash_dimes = float(input('No of dimes : ')) * 0.1
    cash_nickles = float(input('No of nickles : ')) * 0.05
    cash_pennies = float(input('No of pennies : ')) * 0.01
    total_payment = cash_quarters + cash_dimes + cash_nickles + cash_pennies
    if total_payment >= MENU[coffee_type]['cost']:
        refund = total_payment - MENU[coffee_type]['cost']
        print(f"Your total payment :{total_payment}")
        print(f"The cost of your coffee :{MENU[coffee_type]['cost']}")
        print(f"Refund :{refund}")
        global total_money
        total_money += MENU[coffee_type]["cost"]

        resources['water'] = resources["water"] - required_water
        resources["coffee"] = resources["coffee"] - required_coffee
        resources["milk"] = resources["milk"] - required_milk
    else:
        print('You do not have enough coins')
        print('Please select another type of coffee.')


print(logo)
print('Welcome to our coffee shop:')
while True:
    coffee_type = input("""Choose the type of coffee: 'c' for cappuccino, 'l' for latte ,or 'e' for espresso.
                                Type 'off' to turn off the coffee machine.
                                Type 'report' to see the status of the ingredients. : """).lower()
    if coffee_type == "c":
        coffee_type = 'cappuccino'
    elif coffee_type == "l":
        coffee_type = 'latte'
    elif coffee_type == 'e':
        coffee_type = "espresso"

    if coffee_type == 'report':
        report()
    elif coffee_type == 'off':
        print('Goodbye')
        break
    else:
        coffee()
