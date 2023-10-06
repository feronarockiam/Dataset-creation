import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Define product categories and product names
product_categories = {
    "Electronics": ["TV", "Mobile", "Laptop", "Headphones", "Camera", "Tablet", "Smartwatch", "Speaker", "Gaming Console", "Monitor"],
    "Clothing": ["T-Shirt", "Jeans", "Dress", "Shoes", "Jacket", "Sweater", "Hoodie", "Socks", "Hat", "Skirt"],
    "Groceries": ["Milk", "Bread", "Eggs", "Rice", "Cereal", "Pasta", "Fruits", "Vegetables", "Snacks", "Canned Food"],
    "Home Appliances": ["Refrigerator", "Washing Machine", "Microwave", "Toaster", "Coffee Maker", "Blender", "Iron", "Vacuum Cleaner"],
    "Toys": ["Action Figure", "Board Game", "Doll", "LEGO Set", "Remote Control Car", "Puzzle", "Art Supplies", "Plush Toy", "Building Blocks", "Toy Car"]
}

# Generate Dataset 2: Stock Details with 500 rows
stock_data = []
for stock_id in range(1, 501):
    stock_category = random.choice(list(product_categories.keys()))
    product_name = random.choice(product_categories[stock_category])
    in_stock = random.randint(50, 200)
    stock_data.append([stock_id, product_name, stock_category, in_stock])

stock_df = pd.DataFrame(stock_data, columns=["StockID", "ProductName", "StockCategory", "InStock(Units)"])

# Generate Dataset 3: Section Data with 500 rows
section_data = []
for _ in range(500):
    section_name = random.choice(list(product_categories.keys()))
    avg_time_spent = round(random.uniform(10, 60), 2)  # Average time spent in minutes
    people_count = random.randint(20, 100)
    section_data.append([section_name, avg_time_spent, people_count])

section_df = pd.DataFrame(section_data, columns=["SectionName", "AvgTimeSpent(min)", "PeopleCount"])

# Generate Dataset 1: Daily Data with 500 rows using the relationships
daily_data = []
for user_id in range(1, 501):
    stock_category = random.choice(list(product_categories.keys()))
    product_name = random.choice(product_categories[stock_category])
    time_spent_on_counter = round(random.uniform(5, 30), 2)  # Time spent in minutes

    daily_data.append([user_id, product_name, stock_category, time_spent_on_counter])

daily_df = pd.DataFrame(daily_data, columns=["UserID", "ProductName", "ProductCategory", "TimeSpentOnCounter"])

# Save the three datasets to CSV files with 500 rows each
stock_df.to_csv("stock_details_500_rows.csv", index=False)
section_df.to_csv("section_data_500_rows.csv", index=False)
daily_df.to_csv("daily_data_500_rows.csv", index=False)

print("CSV files with 500 rows for all three datasets generated successfully.")
