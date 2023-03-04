from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

shouldContinue = True
while shouldContinue:
    choice = input(f"What would you like to have? ({drink_menu.get_items()}): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        print(f"Money: ${money_machine.profit}")
    else:
        drink = drink_menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
