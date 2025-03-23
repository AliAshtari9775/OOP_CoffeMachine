from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

not_finished = True

# Creating a Coffee Maker Class
my_coffee_maker = CoffeeMaker()

# Creating a Menu Class
my_menu = Menu()
my_menu_items = my_menu.get_items()

# Creating a MoneyMachine Class
my_money_machine = MoneyMachine()

while not_finished:
    # Printing the menu items for user input
    user_input = input(f"What would you like? ({my_menu_items}):").lower()
    try:
        # Creating a MenuItem Class form the input
        order = my_menu.find_drink(user_input)

        # Checking sufficient ingredients
        sufficient = my_coffee_maker.is_resource_sufficient(order)
        if sufficient:
            if my_money_machine.make_payment(order.cost):
                my_coffee_maker.make_coffee(order)
    except AttributeError:
        if user_input == 'report':
            my_coffee_maker.report()
            my_money_machine.report()
        elif user_input == 'off':
            print("The Coffee Machine is shut down.")
            not_finished = False
