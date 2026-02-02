# OPTIMIZED-CODING-PROJECTS-PYTHON
This repository dedicates to alll the projects based on python. This repository will post all the programs in a well optimized order, it will focus only on code optimization.
30 DAY PROGRAMME REPOSITORY:
1. Grocery Store Billing System

Menu of grocery items with prices. User selects items until q. Print total bill.

2. Cafe Order System

Menu: Coffee, Tea, Sandwich, Cake. Add items and calculate total amount.

3. Movie Ticket Booking System

Menu: Movie types with ticket price. User chooses number of tickets and movie type. Show total cost.

4. ATM Menu Program

Menu: Deposit, Withdraw, Check Balance, Exit. Keep running until q.

5. Mobile Recharge System

Menu of recharge plans with prices. User selects plan and shows bill.

6. Library Book Issue System

Menu: Issue book, Return book, View issued books, Exit.

7. Student Marks Management System

Menu: Add student marks, View all students, Find topper, Exit.

8. Quiz Game Menu

Menu: Start quiz, View score, Exit. Questions stored in dictionary.

9. Contact Book Program

Menu: Add contact, Search contact, Delete contact, Show all contacts.

10. Shopping Cart Program

Menu: Add item, Remove item, View cart, Checkout.

11. Hotel Room Booking System

Menu: Single room, Double room, Suite. User selects room type and days. Calculate bill.

12. Railway Ticket System

Menu: First class, Second class, Sleeper. User selects and total fare is calculated.

13. Bus Ticket Reservation

Menu of destinations with price. User selects destination and number of seats.

14. Electricity Bill Generator

Menu: Domestic, Commercial. User enters units and bill is calculated.

15. Salary Calculator

Menu: Enter salary, Calculate tax, Show net salary.

16. Bank Account System

Menu: Create account, Deposit, Withdraw, Show balance, Exit.

17. Pizza Ordering System

Menu of pizza types with prices. User orders multiple pizzas and gets bill.

18. Ice Cream Parlour Program

Menu of flavors and prices. User selects and total bill is shown.

19. Online Exam System

Menu: Start exam, Show result, Exit.

20. Inventory Management System

Menu: Add product, Update quantity, View inventory, Exit.

21. Currency Converter Menu

Menu: Dollar to Rupee, Euro to Rupee, Pound to Rupee.

22. Parking Fee System

Menu: Bike, Car, Truck with per-hour fee. User enters hours and total fee.

23. Gym Membership System

Menu: Monthly plan, Quarterly plan, Yearly plan. Show bill.

24. Toll Booth System

Menu of vehicle types with toll charges. User selects vehicle and shows toll fee.

25. Book Store Billing System

Menu of books with prices. User buys books and total bill is printed.

26. Electricity Appliance Usage Bill

Menu: Fan, AC, Heater, TV with unit cost. Calculate monthly bill.

27. Online Food Delivery System

Menu: Burger, Pizza, Fries, Coke. User orders and bill is generated.

28. Voting System

Menu: Cast vote, View results, Exit. Use dictionary to store votes.

29. Feedback Collection System

Menu: Add feedback, View all feedbacks, Exit.

30. Mini Supermarket System (Final Project)

Menu:

Add items

Buy items

View cart

Checkout

Exit

(Combination of restaurant + shopping cart)

#SKELETON

🔑 Common Structure for ALL 30 Programs (like your restaurant code)

Each program should use:

dictionary for menu

while True loop

input() for choice

try/except for errors

q to quit

total = 0 or data storage

Like your restaurant program logic:

Menu dictionary
while True:
    input choice
    if q → break
    try:
        access dictionary
        add price
    except:
        invalid choice
print final result


If you want, next I can give you:
✅ 5 fully written example programs (Restaurant, ATM, Contact Book, Quiz, Shopping Cart)
OR
✅ One universal template you can reuse for all 30
OR
✅ PDF list of these 30 problems

Just reply with:
1) Give 5 sample programs
2) Universal template
3) PDF list
4) All three

NOW PROVIDE A SKELETON FOR ALL THE ABOVE 30 PROBLEMS WHICH INCLUDE DEF,LOOPS,WHILE TRUE,CONDITIONAL STATEMENTS, TRY AND EXCEPT,INPUT ,Q,DICTIONARY
"""
UNIVERSAL MENU-DRIVEN SKELETON (Restaurant-style)
Use this SAME skeleton for all 30 programs.
Just change:
1) MENU dictionary

NOW PROVIDE A SKELETON FOR ALL THE ABOVE 30 PROBLEMS WHICH INCLUDE DEF,LOOPS,WHILE TRUE,CONDITIONAL STATEMENTS, TRY AND EXCEPT,INPUT ,Q,DICTIONARY,LIST,TUPLE,OPERATORS
"""
UNIVERSAL MENU-DRIVEN SKELETON (Restaurant-style)
Works for all your 30 programs.

Includes:
- def functions
- while True loop
- if/elif/else
- try/except
- input + 'q' to quit
- dictionary menu
- list for cart/history/logs
- tuple for storing item data
- operators for totals, counts, etc.

HOW TO USE:
1) Edit MENU_ITEMS (your menu)
2) Edit handle_choice() based on your program
3) Run main()
"""

# -------------------------------
# 1) DATA (Dictionary + Tuples)
# -------------------------------
MENU_ITEMS = {
    "1": ("Item A", 100),   # (name, price)
    "2": ("Item B", 200),
    "3": ("Item C", 300),
}

# List to store history/cart/records
cart = []          # example: [("Item A", 100), ("Item B", 200)]
actions_log = []   # example: ["Added Item A", "Checked out"]

# Variables for calculations
total = 0
count = 0


# -------------------------------
# 2) DISPLAY FUNCTIONS
# -------------------------------
def show_menu():
    print("\n========= MENU =========")
    for key, (name, price) in MENU_ITEMS.items():
        print(f"{key}. {name} - ₹{price}")
    print("q. Quit")
    print("========================")


def show_status():
    """Optional: show current cart and total"""
    print("\n--- CURRENT STATUS ---")
    print("Cart items:", cart)          # list of tuples
    print("Total =", total)
    print("Items count =", count)
    print("----------------------")


# -------------------------------
# 3) CORE LOGIC FUNCTIONS
# -------------------------------
def add_item(choice):
    """Add selected item to cart and update totals."""
    global total, count

    item_name, price = MENU_ITEMS[choice]    # tuple unpacking
    cart.append((item_name, price))          # list + tuple
    total += price                           # operator
    count += 1                               # operator
    actions_log.append(f"Added {item_name} = {price}")
    print(f"✅ Added: {item_name} (₹{price})")


def remove_last_item():
    """Remove last item from cart if exists (useful for cart programs)."""
    global total, count

    if len(cart) == 0:
        print("⚠️ Cart is empty. Nothing to remove.")
        return

    item_name, price = cart.pop()
    total -= price
    count -= 1
    actions_log.append(f"Removed {item_name} = {price}")
    print(f"🗑️ Removed: {item_name} (₹{price})")


def checkout():
    """Final output when user quits."""
    print("\n========= CHECKOUT =========")
    print("Items bought:")
    for i, (name, price) in enumerate(cart, start=1):
        print(f"{i}. {name} - ₹{price}")
    print("----------------------------")
    print("Total items:", count)
    print("Final bill: ₹", total)
    print("============================")


def handle_choice(choice):
    """
    IMPORTANT:
    Modify this for each program:
    - ATM: deposit/withdraw
    - Quiz: ask question
    - Contact book: add/search/delete
    - Booking: multiply price by days/tickets
    """

    # Example extra options (you can keep/remove depending on program)
    if choice == "1" or choice == "2" or choice == "3":
        add_item(choice)

    elif choice == "r":
        remove_last_item()

    elif choice == "s":
        show_status()

    else:
        print("❌ Invalid choice! Please select from menu.")


# -------------------------------
# 4) MAIN LOOP (while True)
# -------------------------------
def main():
    print("✅ Welcome! (Menu-driven program template)")

    while True:
        try:
            show_menu()
            print("Extra commands: s=show status, r=remove last item")
            choice = input("Enter your choice: ").strip().lower()

            if choice == "q":
                actions_log.append("Exited program")
                checkout()
                break

            # If menu choice exists in dictionary → valid item
            if choice in MENU_ITEMS:
                handle_choice(choice)
            else:
                # handle other commands (s, r, etc.) or invalid
                handle_choice(choice)

        except KeyError:
            print("❌ Choice not found in menu dictionary.")
        except ValueError:
            print("❌ Invalid number input.")
        except Exception as e:
            print("⚠️ Something went wrong:", e)

    print("\n✅ Program finished.")
    # Optional: print log
    # print("Action log:", actions_log)


# -------------------------------
# RUN PROGRAM
# -------------------------------
main()

