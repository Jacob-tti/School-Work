"""
Jacob Barsotti

Program I turned into a class after learning if/elif/else statements. Planning to upgrade and make more effiecient with loops

This Program acts as a virtual shopping cart. Asking the user how many items they'd like to get, then giving the user
a list to choose from. Where they can then decide quantity and it will calculate the price giving the user an update
on the total from just that item, eventually printing a receipt once all items are selected.
"""


def shopping_Cart_App():
    # initializing variables
    apple = 1.50
    bananas = 0.75
    milk = 3.20
    bread = 2.50
    sub_total = 0.0

    # prompting user for how many items they would like
    print("Welcome to the Shopping Cart Program!")
    total_items = input("How many items would you like to buy? (1-3) ")

    # checking that user gave a valid number (1-3)
    if not total_items.isdigit():
        print("Error : please give a number between 1 and 3")
        total_items = input("How many items would you like to buy? (1-3) ")
    else:
        total_items = int(total_items)
        if total_items < 1:
            print("Error : please give a number between 1 and 3")
            total_items = input("How many items would you like to buy? (1-3) ")
        elif total_items > 3:
            print("Error : please give a number between 1 and 3")
            total_items = input("How many items would you like to buy? (1-3) ")

    # printing options of items and their price for users
    print("")
    print("Available items:")
    print(f"1. Apples - ${apple:.2f} each") 
    print(f"2. Bananas - ${bananas:.2f} each")
    print(f"3. Milk - ${milk:.2f} each")
    print(f"4. Bread - ${bread:.2f} each")
    print("")

    # 1 item
    # checks which item the user selected
    if total_items == 1:
        item_digit = int(input("Enter the number of item 1: ")) # translates to int so we will be working with a whole number
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.") # throws error if it doesn't catch

        # asks user for quantity 
        # gets the total cost for the item and its quantity
        # prints so user can see
        # in repeated sections the values get rewritten as the code processes 
        temp_item_quantity = int(input("Enter the quantity: ")) # translates to int because you can't have a half an item
        temp_item_total = temp_item_quantity * temp_item_value # multiplies the item value and quantity for sub total
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}") # prints an update to user
        print("") # formatting
        sub_total += temp_item_total # adds the total to sub_total 
        # other sections the += adds to the value of sub_total 


    # 2 items
    # same as above but runs item selection twice 
    elif total_items == 2:
        item_digit = int(input("Enter the number of item 1: "))
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.")

        temp_item_quantity = int(input("Enter the quantity: "))
        temp_item_total = temp_item_quantity * temp_item_value
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}")
        print("")
        sub_total += temp_item_total

        item_digit = int(input("Enter the number of item 2: "))
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.")

        temp_item_quantity = int(input("Enter the quantity: "))
        temp_item_total = temp_item_quantity * temp_item_value
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}")
        print("")
        sub_total += temp_item_total


    # 3 items
    # runs item selection 3 times
    if total_items == 3:
        item_digit = int(input("Enter the number of item 1: "))
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.")

        # 3 items
        temp_item_quantity = int(input("Enter the quantity: "))
        temp_item_total = temp_item_quantity * temp_item_value
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}")
        print("")
        sub_total += temp_item_total

        item_digit = int(input("Enter the number of item 2: "))
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.")

        temp_item_quantity = int(input("Enter the quantity: "))
        temp_item_total = temp_item_quantity * temp_item_value
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}")
        print("")
        sub_total += temp_item_total

        item_digit = int(input("Enter the number of item 3: "))
        if item_digit == 1:
            temp_item_value = apple
            temp_item_name = "apple"
        elif item_digit == 2:
            temp_item_value = bananas
            temp_item_name = "bananas"
        elif item_digit == 3:
            temp_item_value = milk
            temp_item_name = "milk"
        elif item_digit == 4:
            temp_item_value = bread
            temp_item_name = "bread"
        else:
            print(f"Error: there is no item {item_digit} on the menu. Skipping this item.")

        temp_item_quantity = int(input("Enter the quantity: "))
        temp_item_total = temp_item_quantity * temp_item_value
        print(f"Added: {temp_item_name} x {temp_item_quantity} = ${temp_item_total:.2f}")
        print("")
        sub_total += temp_item_total


    # calculate tax
    tax = sub_total * 0.05
    total = tax + sub_total

    # print receipt
    print("")
    print("Receipt:")
    print(f"Subtotal: ${sub_total:.2f}")
    print(f"Tax (5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")


shopping_Cart_App()