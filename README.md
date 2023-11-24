This is a simple Python problem with a few restrictions for added difficulty.

# Instructions

### 1. Starting the Program

1. The following should be displayed once the program starts.

    ```
    Welcome to Yum Spot!
    Please fill out the form below.

    Name: |
    ```

2. The delivery address field should appear after the user enters his/her name.

    ```
    Welcome to Yum Spot!
    Please fill out the form below.

    Name: Juan Dela Cruz
    Delivery Address: |
    ```

3. The contact number field should appear after the user enters his/her delivery address.

    ```
    Welcome to Yum Spot!
    Please fill out the form below.

    Name: Juan dela Cruz
    Delivery Address: L30 B4 Applt St., X City
    Contact No.: |
    ```

### 2. Menu

4. The following information should be displayed once the user completes the form.

    ```
    Hi Juan dela Cruz! You may start ordering now. Max of 3 orders.
    1 - Order
    2 - Cancel
    Enter the number of your choice. |
    ```

5. If the user chooses `1`, the meals menu should display.

6. If `2`, the program should display the message in 1.

7. Suppose the user inputs from `1 - Order`, the following menu should display.

    ```
    ---------------------------------------------------------------------------
                  Meal              Regular(r)      Medium(m)       Large(l)
    1 - Classic Burger Meal         PhP 115         PhP 130         PhP 145
    2 - Cheeseburger Meal           PhP 125         PhP 140         PhP 155
    3 - Chicken Sandwhich Meal      PhP 125         PhP 140         PhP 155
    0 - Back to Main Menu
    ---------------------------------------------------------------------------
    Note: All meals include fries and a soft drink.
    ---------------------------------------------------------------------------
    Enter the number of your meal of choice for Order 1. |
    ```

8. Note: The order number in "Enter the number of your meal of choice for Order 1" should change for the next orders/meals.

9. Suppose the user inputs `0`, the message in 4 should be displayed.

### 3. Ordering and Adding a Meal

10. Suppose the user inputs any number from `1` to `3`, the following prompt should be displayed, asking the user to choose a meal size.

    ```
    What meal size? (r, m, or l) |
    ```

11. The following prompt asking if the user wants to include an add-on should display if the user chooses any meal size.

    ```
    Do you want an add_on? (y/n) |
    ```

12. Suppose the user decides to get an add-on and inputs `y`, the following prompt should display.

    ```
    ---------------------------------------------------------------------------
    Add-ons
    4 - Bottled Water               PhP 20          -               -
    5 - Vanilla Ice Cream Cone      PhP 25          -               -
    6 - Chocolate Sundae            PhP 30          -               -
    7 - Back to Main Menu           -               -               -
    ---------------------------------------------------------------------------
    Enter the number of your add-on for Order 2. |
    ```

13. A message that the add-on is successfully added should be displayed depending on the user's choice. Below is an example of a message saying that bottled water is successfully added. In addition, a prompt asking if the user would like to add an order should also be displayed with the previous message.

    ```
    Bottled Water is successfully added.

    Would you like to add an order? (y/n)
    ```

14. If the user chooses not to include an add-on, a prompt asking if the user would like to add an order should be displayed like in 13.

15. Suppose the user inputs `y` for yes, the following choices and prompt should be displayed. Note that this is similar to 4 except that the message "Hi <user's name>! You may start ordering now. Max of 3 orders." is not included.

    ```
    1 - Order
    2 - Cancel
    Enter the number of your choice. |
    ```

16. Suppose the user chooses `1 - Order`, same process follows (7 to 13). Note that the order number should increase by 1 for every next order/meal (as stated before in 8). The program can take a maximum of 3 orders.

17. Hence, if the user already orderd 3 meals, the prompt "Would you like to add an order? (y/n)" should not appear.

18. The order summary should be displayed if the user chooses `2 - Cancel`.

### 4. Order Summary

19. Suppose the user decides not to add more orders or the maximum number or orders (3) has already been reached, the program should display the order summary and a prompt asking for the amount of money the user will use to pay.

    ```
    ---------------------------------------------------------------------------
    Summary of your orders
    ---------------------------------------------------------------------------
    Order 1                        .
     Regular Classic Burger Meal                    PhP 115
     add Bottled Water             PhP 20
    Order 2
     Large Chicken Sandwhich Meal                   PhP 155
     add Vanilla Ice Cream Cone    PhP 25
    Order 3
     Medium Cheeseburger Meal                       PhP 140
    Amount Due                                      PhP 455
    ---------------------------------------------------------------------------
    How much is your money? |
    ```

20. The add-on and the additional payment should be seen in the order summary.

21. If the user enters an insufficient amount, the following message and prompt should be displayed.

    ```
    You gave an insufficient amount.
    How much is your money? |
    ```

22. The following should be displayed if the user enters a sufficient amount.

    ```
    Delivery details:
    Name: Juan dela Cruz
    Delivery Address: L30 B4 Applt St., X City
    Contact No.: 0917123456

    Thank you for purchasing! You will enjoy your order soon!
    ```

23. The program should display the message and prompt in 1 for the next user.

    ```
    Welcome to Yum Spot!
    Please fill out the form below.

    Name: |
    ```

### 5. Other(s)

24. The following should display whenever the user inputs a choice that is not in the list.
    ```
    You have entered an invalid input.
    Please select from the choices.
    ```

### 6. Restrictions

25. You are not allowed to use `for loop`, `creating functions`, `True`, `False`, `None`, `continue`, `break`, and `importing a library`
