import pandas as pd

class Product:
    def __init__(self, sku, name, brand, quantity):
        self.sku = sku
        self.name = name
        self.brand = brand
        self.quantity = quantity

    def to_dict(self):
        return {
            "SKU": self.sku,
            "Name": self.name,
            "Brand": self.brand,
            "Quantity": self.quantity
        }

def load_inventory(filename="inventory.csv"):
    try:
        df = pd.read_csv(filename)
        if df.empty:
            raise pd.errors.EmptyDataError
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # If the file doesn't exist or is empty, create an empty DataFrame with the required columns
        df = pd.DataFrame(columns=["SKU", "Name", "Brand", "Quantity"])
    return df

def save_inventory(df, filename="inventory.csv"):
    try:
        df.to_csv(filename, index=False)
    except IOError as e:
        print(f"Error saving inventory to file: {e}")

def add_product(df):
    sku = input("Enter product SKU: ")

    if sku in df["SKU"].values:
        print(f"Product with SKU {sku} already exists.")
        return df

    name = input("Enter product name: ")
    brand = input("Enter product brand: ")
    try:
        quantity = int(input("Enter product quantity: "))
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
    except ValueError as e:
        print(e)
        return df
    
    new_product = Product(sku, name, brand, quantity).to_dict()
    new_product_df = pd.DataFrame([new_product])
    df = pd.concat([df, new_product_df], ignore_index=True)
    save_inventory(df)
    print(f"Product {name} added to inventory.")
    return df

def list_products(df):
    if df.empty:
        print("Inventory is empty.")
        return

    print(df)

def update_product(df):
    sku = input("Enter product SKU to update: ")

    if sku not in df["SKU"].values:
        print(f"Product with SKU {sku} not found.")
        return df

    name = input("Enter new name (leave blank to keep current): ")
    brand = input("Enter new brand (leave blank to keep current): ")
    quantity = input("Enter new quantity (leave blank to keep current): ")

    if name:
        df.loc[df["SKU"] == sku, "Name"] = name
    if brand:
        df.loc[df["SKU"] == sku, "Brand"] = brand
    if quantity:
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError("Quantity must be a positive integer.")
            df.loc[df["SKU"] == sku, "Quantity"] = quantity
        except ValueError as e:
            print(e)
            return df

    save_inventory(df)
    print(f"Product {sku} updated.")
    return df

def delete_product(df):
    sku = input("Enter product SKU to delete: ")

    if sku not in df["SKU"].values:
        print(f"Product with SKU {sku} not found.")
        return df

    df = df[df["SKU"] != sku]
    save_inventory(df)
    print(f"Product {sku} deleted.")
    return df

def search_products(df):
    search_term = input("Enter product name or brand to search: ").lower()
    results = df[df["Name"].str.lower().str.contains(search_term) | df["Brand"].str.lower().str.contains(search_term)]

    if not results.empty:
        print(results)
    else:
        print("No products found.")

def sort_products(df):
    print("Sort by:\n1. SKU\n2. Name\n3. Quantity")
    choice = input("Enter your choice: ")

    if choice == '1':
        sorted_df = df.sort_values(by="SKU")
    elif choice == '2':
        sorted_df = df.sort_values(by="Name")
    elif choice == '3':
        sorted_df = df.sort_values(by="Quantity")
    else:
        print("Invalid choice.")
        return

    print(sorted_df)

def main():
    df = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Products")
        print("6. Sort Products")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            df = add_product(df)
        elif choice == '2':
            list_products(df)
        elif choice == '3':
            df = update_product(df)
        elif choice == '4':
            df = delete_product(df)
        elif choice == '5':
            search_products(df)
        elif choice == '6':
            sort_products(df)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
