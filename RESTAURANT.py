total = 0
print("==MENU==")
print("____RESTAURANT MENU____")
print("1...APPLE............500")
print("2...BANANA...........200")
print("3...GRAPE............300")
print("4...MANGO............400")
print("q...Exit the Menu.......") 
my_dict = {"1": ("apple", 500),
    "2": ("banana", 200),
    "3": ("grape", 300),
    "4": ("mango", 400)}
while True:
    try:
        user = input("Enter your choice: ")
         if user == "q":
            break
        item = my_dict[user][1]
        total+=item
    except Exception:
        print(f"your input is not valid, it is not in the menu list")
print(f"hence your final bill is:{total}")


        
