class Item:
    def __init__(self, item_id, name, description, price):
        if item_id <= 0 or price < 0:
            raise ValueError("Invalid ID or price.")
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            raise KeyError("Item already exists.")
        self.items[item_id] = Item(item_id, name, description, price)

    def read_item(self, item_id):
        item = self.items.get(item_id)
        if item:
            return str(item)
        return "Item not found."

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise KeyError("Item not found.")
        item = self.items[item_id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None and price >= 0:
            item.price = price

    def delete_item(self, item_id):
        self.items.pop(item_id, None)

def main():
    manager = ItemManager()
    while True:
        print("Item Management System")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                item_id = int(input("Enter item ID: ").lstrip("0"))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
                print("Item created successfully.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                item_id = int(input("Enter item ID: ").lstrip("0"))
                print(manager.read_item(item_id))
            except ValueError:
                print("Invalid input. Please enter a valid numeric item ID.")
        elif choice == "3":
            try:
                item_id = int(input("Enter item ID: ").lstrip("0"))
                name = input("Enter new name (kindly leave blank to keep unchanged): ") or None
                description = input("Enter new description (kindly leave blank to keep unchanged): ") or None
                price_input = input("Enter new price (kindly leave blank to keep unchanged): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
                print("Item updated successfully.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            try:
                item_id = int(input("Enter item ID: ").lstrip("0"))
                manager.delete_item(item_id)
                print("Item deleted successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric item ID.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()