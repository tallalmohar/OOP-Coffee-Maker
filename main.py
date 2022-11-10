from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()  # report object
money_machine = MoneyMachine()  # report object money
menu_object = Menu()

isMachine_on = True
while isMachine_on is True:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")


    if user_coffee.lower() == "off":
        isMachine_on = False
    elif user_coffee.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_object.find_drink(user_coffee)
        if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffee_maker.make(drink)




