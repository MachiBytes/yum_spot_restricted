food_menu = {
    "1": {
        "Name": "Classic Burger Meal", 
        "Price": {
            "r": 115, 
            "m": 130, 
            "l": 145
        }
    },
    "2": {
        "Name": "Cheeseburger Meal", 
        "Price": {
            "r": 125, 
            "m": 140, 
            "l": 155
        }
    },
    "3": {
        "Name": "Chicken Sandwhich Meal", 
        "Price": {
            "r": 125, 
            "m": 140, 
            "l": 155
        }
    }
}
add_ons = {
    "4": {
        "Name": "Bottled Water",
        "Price": 20
    },
    "5": {
        "Name": "Vanilla Ice Cream Cone",
        "Price": 25
    },
    "6": {
        "Name": "Chocolate Sundae",
        "Price": 30
    }
}

app_running = 1
while app_running == 1:
    print("Welcome to Yum Spot!")
    print("Please fill out the form below.")
    print()
    name = input("Name: ")
    delivery_address = input("Delivery Address: ")
    contact_number = input("Contact No.: ")
    print()

    is_ordering = 1
    orders = []  # [{"meal", "size", "add-on"}]

    while is_ordering == 1:
        if len(orders) == 0:
            print(f"Hi {name}! You may start ordering now. Max of 3 orders.")
        print("1 - Order")
        print("2 - Cancel")
        will_order = input("Enter the number of your choice: ")
        print()
        if will_order not in ["1", "2"]:
            print("You have entered an invalid input.")
            print("Please select from the choices.")
            print()
        elif will_order == "1":
            # Reset variables
            meal_chosen = ""
            while meal_chosen not in ["1", "2", "3", "0"]:
                # Show Menu
                print()
                print("-" * 75)
                print("Meal".center(32, " ")                        + "Regular(r)".ljust(16, " ") + "Medium(m)".ljust(16, " ") + "Large(l)")
                print("1 - Classic Burger Meal".ljust(32, " ")      + "PhP 115".ljust(16, " ") + "PhP 130".ljust(16, " ") + "PhP 145")
                print("2 - Cheeseburger Meal".ljust(32, " ")        + "PhP 125".ljust(16, " ") + "PhP 140".ljust(16, " ") + "PhP 155")
                print("3 - Chicken Sandwhich Meal".ljust(32, " ")   + "PhP 125".ljust(16, " ") + "PhP 140".ljust(16, " ") + "PhP 155")
                print("0 - Back to Main Menu")
                print("-" * 75)
                print("Note: All meals include fries and a soft drink.")
                print("-" * 75)
                # Take input
                meal_chosen = input(f"Enter the number of your meal of choice for Order {len(orders) + 1}. ")
                print()
                if meal_chosen not in ["1", "2", "3", "0"]:
                    print("You have entered an invalid input.")
                    print("Please select from the choices.")
                    print()

            if meal_chosen != "0":
                # check if input is in choices
                if meal_chosen != "0":
                    # check meal size
                    meal_size = ""
                    chosen_add_on = ""
                    while meal_size not in ["r", "m", "l"]:
                        meal_size = input("Enter the size of your meal (r, m, l): ")
                        print()
                        if meal_size not in ["r", "m", "l"]:
                            print("You have entered an invalid input.")
                            print("Please select from the choices.")
                            print()
                    add_add_ons = ""
                    while add_add_ons not in ["y", "n"]:
                        add_add_ons = input("Do you want to add add-ons? (y/n): ")
                        print()
                        if add_add_ons not in ["y", "n"]:
                            print("You have entered an invalid input.")
                            print("Please select from the choices.")
                            print()
                    if add_add_ons == "y":
                        chosen_add_on = ""
                        while chosen_add_on not in ["4", "5", "6", "7"]:
                            # Show Add-ons
                            print()
                            print("-" * 75)
                            print("Add-ons")
                            print("4 - Bottled Water".ljust(32, " ") + "PhP 20".ljust(16, " ") + "-".ljust(16, " ") + "-".ljust(16, " "))
                            print("5 - Vanilla Ice Cream Cone".ljust(32, " ") + "PhP 25".ljust(16, " ") + "-".ljust(16, " ") + "-".ljust(16, " "))
                            print("6 - Chocolate Sundae".ljust(32, " ") + "PhP 30".ljust(16, " ") + "-".ljust(16, " ") + "-".ljust(16, " "))
                            print("7 - Back to Main Menu".ljust(32, " ") + "-".ljust(16, " ") + "-".ljust(16, " ") + "-".ljust(16, " "))
                            print("-" * 75)
                            chosen_add_on = input(f"Enter the number of your add-on for Order {len(orders) + 1}. ")
                            print()
                            if chosen_add_on not in ["4", "5", "6", "7"]:
                                print("You have entered an invalid input.")
                                print("Please select from the choices.")
                                print()
                            elif chosen_add_on != "7":
                                print(f"{add_ons[chosen_add_on]['Name']} is successfully added.")
                                print()
                    orders.append({"meal": meal_chosen, "size": meal_size, "add-on": chosen_add_on})
                    if len(orders) < 3:
                        place_another_order = ""
                        while place_another_order not in ["y", "n"]:
                            place_another_order = input("Do you want to place another order? (y/n): ")
                            print()
                            if place_another_order not in ["y", "n"]:
                                print("You have entered an invalid input.")
                                print("Please select from the choices.")
                                print()
                            elif place_another_order == "n":
                                is_ordering = 0
                    else:
                        is_ordering = 0
        elif will_order == "2":
            is_ordering = 0
        
    if len(orders) > 0:
        print("-" * 75)
        print("Summary of your orders")
        print("-" * 75)
        i = 0
        total_amount = 0
        while i < len(orders):
            order = orders[i]["meal"]
            size = orders[i]["size"]
            meal_prize = food_menu[order]['Price'][size]
            add_on = orders[i]["add-on"]
            add_on_prize = 0
            sizes = {"r": "Regular", "m": "Medium", "l": "Large"}[size]
            order_name = f"{sizes} {food_menu[order]['Name']}"
            print(f"Order {i + 1}\n {order_name.ljust(30 + 16, ' ')} PhP {meal_prize}")
            if add_on not in ["", "7"]:
                print(f" add {add_ons[add_on]['Name']}".ljust(31, " ") + f"PhP {add_ons[add_on]['Price']}")
                add_on_prize = add_ons[add_on]['Price']
            total_amount += meal_prize + add_on_prize
            i += 1
        print("Amount Due".ljust(32 + 16, " ") + f"PhP {total_amount}")
        print("-" * 75)
        your_money = 0
        while your_money < total_amount:
            your_money = int(input("How much is your money? "))
            print()
            if your_money < total_amount:
                print("You gave an insufficient amount.")
        print("Delivery details:")
        print(f"Name: {name}")
        print(f"Address: {delivery_address}")
        print(f"Contact No.: {contact_number}")
        print()
        print("Thank you for purchasing! You will enjoy your order soon!")
        print()
        print()
    if len(orders) > 0:
        pass
    