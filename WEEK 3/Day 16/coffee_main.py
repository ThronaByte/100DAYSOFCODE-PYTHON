from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_off = True
while is_off:
    take_order = input(f"What would you like? {menu.get_items()}: ")
    cmd = ["latte", "espresso", "cappuccino", "report", "off"]
    while take_order not in cmd:
        take_order = input(f"Invalid Input!\nWhat would you like? {menu.get_items()}: ")
    if take_order == "off":
        print("Coffee First, Your Bullshit Second\nGoodBye...👋☕")
        is_off = False
    elif take_order == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(take_order)
        if coffe_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffe_maker.make_coffee(item)
