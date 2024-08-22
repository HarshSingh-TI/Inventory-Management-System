Code Structure

The code is organized into several functions and a class to encapsulate the functionality of the inventory management system. Below is a description of each part of the code and the rationale behind their design.

1. Class Definition: Product
Purpose: Encapsulates product attributes and provides a method to convert the product to a dictionary format, which is suitable for creating DataFrames.
Advantage: Using a class helps in organizing product attributes and methods related to a product, enhancing code readability and maintainability.

2. Function: load_inventory
    Purpose: Loads the inventory from a CSV file. If the file does not exist or is empty, it initializes an empty DataFrame with the required columns.
    Advantage: Ensures that the application can handle cases where the CSV file is missing or empty without crashing.

3. Function: save_inventory
    Purpose: Saves the current state of the DataFrame to the CSV file.
    Advantage: Provides a mechanism for persistent storage of product data, ensuring that changes are preserved between runs.

4. Function: add_product
    Purpose: Adds a new product to the DataFrame and saves the updated inventory to the CSV file.
    Advantage: Uses pd.concat() for adding new rows, which is more efficient and compatible with recent versions of pandas compared to the deprecated df.append().

5. Function: list_products
    Purpose: Displays all products in the DataFrame.
    Advantage: Provides a straightforward method for viewing current inventory, which is essential for managing and verifying product data.

6. Function: update_product
    Purpose: Updates product details in the DataFrame and saves the changes.
    Advantage: Allows partial updates where users can change only specific attributes without affecting others, making the update process flexible.

7. Function: delete_product
    Purpose: Removes a product from the DataFrame and updates the CSV file.
    Advantage: Provides a method for removing products, which is crucial for managing inventory when items are no longer available.

8. Function: search_products
    Purpose: Searches for products by name or brand.
    Advantage: Allows users to quickly find products without needing to view the entire inventory, enhancing usability.

9. Function: sort_products
    Purpose: Sorts products based on SKU, Name, or Quantity.
    Advantage: Provides options to view the inventory in different orders, helping users analyze the data more effectively.

10. Function: main
Purpose: Provides a menu-driven interface for interacting with the inventory management system.
Advantage: Offers a simple command-line interface for users to choose actions, making the system easy to use and navigate.


Summary

This Inventory Management System leverages pandas for efficient data handling and CSV file management. Key functions are designed to ensure data integrity, ease of use, and maintainability. By using classes, functions, and pandas methods, the system is both scalable and robust, capable of handling various inventory management tasks with minimal code changes.
