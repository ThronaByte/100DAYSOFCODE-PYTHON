print("Welcome To ThronaByte Coffee Machine")
# #1
from coffe_machine_menu import resources, MENU

def resource_sufficient(menu_ingredient):
    #3 hot flavours (latte/espresso/cappuccino)
    # 2. check resources sufficient
    """Ensures enough ingredients for the selected coffee."""
    for item in menu_ingredient:
        if menu_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return  False
    return True

def process_coins():
    # it has 4types of coin the penny(1 cent:N0.01),
    # nickel(5 cents:N0.05) ,dime(10 cents:N0.10) and quarter(25 cents:N0.25)
    # 3 process coins
    """Handles calculating the total value of coins inserted."""
    print("Insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dime? ")) * 0.10
    total += int(input("how many nickel? ")) * 0.05
    total += int(input("how many penny? ")) * 0.01
    return  total
profit = 0
def transaction_successful(money_received, flavour_cost):
    # 4 check transaction successful
    """Determines if the user has inserted enough money and returns either True or False."""
    if money_received >= flavour_cost:
        change = round(money_received - flavour_cost, 2)
        print(f"Here is your change: N{change} ")
        global profit
        profit += flavour_cost
        return  True
    else:
        print("Not enough money. Money refunded")
        return  False

def make_coffee(flavour_name, ingredients):
    # 5 make coffee
    """Prepares the coffee if the transaction is successful."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your ({flavour_name}☕🥛). Enjoy...")

def coffee_machine():
    """Integrates all the logic together for smooth operation."""
    is_off = True
    while is_off:
        user = input("what would you like? (latte/espresso/cappuccino): ").lower()
        # # 2
        while user not in ["latte", "espresso", "cappuccino", "report", "off"]:
            user = input("Invalid Input! \nwhat would you like? (latte/espresso/cappuccino): ").lower()

        # TODO: Turn off the machine by entering "off" to the prompt. (my code should execute when this happens)
        if user == "off":
            print("Coffee First, Your Bullshit Second\nGoodBye...👋☕")
            is_off = False
        # 1 print report
        elif user == "report":
            print(f"""
            water: {resources['water']}ml,
            milk: {resources['milk']}ml,
            coffee: {resources['coffee']}g,
            profit: N{profit}
            """)
        else:
            flavour = MENU[user]
            if resource_sufficient(flavour['ingredients']):
                transaction = process_coins()
                transaction_successful(money_received=transaction, flavour_cost=flavour['cost'])
                make_coffee(flavour_name=user, ingredients=flavour['ingredients'])
coffee_machine()
