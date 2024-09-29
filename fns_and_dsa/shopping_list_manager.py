#shopping_list
def display_menu():
    print(" Shopping list Menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. View the list")
    print("4. Exit")
def add_item(shopping_list):
    item = input("Enter the item to add: ")
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    else:
        print("Add an item to the list.")

def remove_item(shopping_list):
    item = input(f"Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print(f"current shopping list: ")
        for index, item in enumerate(shopping_list, start=0):
            print(f"{index}. {item}")
    else:
        print("Shopping list is empty!")

def main():
    """main function to run the shopping list manager"""
    shopping_list = []

    display_menu()
    while True:
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting the shopping list.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")


#run the main function
if __name__ == "__main__":
    main()
