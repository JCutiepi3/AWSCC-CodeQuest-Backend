class ShoppingList:

    def list(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_list(self):
        if not self.items:
            print("Your shopping list is empty.")
        else:
            print("Your Current Shopping List:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} is now removed from the list.")
        else:
            print(f"{item} is not found in the shopping list.")


def main():
    shopping_list = ShoppingList()

    while True:
        print("\n[Shopping List for today]")
        print("1. <Add item>")
        print("2. <View list>")
        print("3. <Remove Item>")
        print("4. <Quit>")

        choice = input("Enter your desired option (1-4): ")

        if choice == "1":
            item = input("Enter the item to add to the list: ")
            shopping_list.add_item(item)
        elif choice == "2":
            shopping_list.view_list()
        elif choice == "3":
            item = input("Please enter the item that you want to remove: ")
            shopping_list.remove_item(item)
        elif choice == "4":
            print("Thank you for using our program.")
            print("<<EXITING PROGRAM>>")
            break
        else:
            print("Oops! You have entered an INVALID input.")
            print("Please correctly input the following (1-4)!!")



