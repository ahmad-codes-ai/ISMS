inventory = [
    {
        "id": 1001,
        "name": "Gaming Mouse",
        "category": "Accessories",
        "cost_price": 1200,
        "selling_price": 1800,
        "stock": 20,
        "sold": 5
    },
    {
        "id": 1002,
        "name": "Mechanical Keyboard",
        "category": "Accessories",
        "cost_price": 3500,
        "selling_price": 5000,
        "stock": 12,
        "sold": 8
    },
    {
        "id": 1003,
        "name": "24-inch Monitor",
        "category": "Display",
        "cost_price": 22000,
        "selling_price": 28000,
        "stock": 7,
        "sold": 3
    },
    {
        "id": 1004,
        "name": "USB-C Cable",
        "category": "Cables",
        "cost_price": 300,
        "selling_price": 600,
        "stock": 35,
        "sold": 18
    },
    {
        "id": 1005,
        "name": "Laptop Stand",
        "category": "Accessories",
        "cost_price": 1800,
        "selling_price": 2600,
        "stock": 10,
        "sold": 4
    }
]

def add():
    id = int(input("Enter id: "))
    name = input("Enter name of product: ")
    category = input("Enter category of product: ")
    cost = int(input("Enter cost price: "))
    sell = int(input("Enter selling price: "))
    stock = int(input("Enter stock: "))
    sold = 0

    d = {'id': id, 'name': name, 'category':category,'cost_price':cost,'selling_price':sell,
         'stock':stock, 'sold':sold}
    inventory.append(d)


while True:
    print('------------ Inventory Sales Managment System ------------')
    print("1. Inventory")
    print("2. Sales")
    print("3. Reports")
    print("4. Search")
    print("5. Exit")
    user_1 = int(input("Enter Your choice (0-5): "))

    if user_1 == 1:
        print("1: Add Product")
        print("2: View Products")
        print("3: Search Product")
        print("4: Update Product")
        print("5: Delete Product")
        print("6: Restock Product")
        print("7: Low Stock Report")
        print("8: Back")
        user_2 = int(input("Enter Your choice (0-8): "))

        if user_2 == 1:
            add()


print(inventory)