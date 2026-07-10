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

def view():
    for i in inventory:
        print(i)

def search():
    print('1: Search with id: ')
    print('2: Search with name: ')
    s = int(input("Enter your choice: "))
    found = False
    if s == 1:
        id = int(input("Enter id: "))
        for i in inventory:
            if i['id'] == id:
                found = True
                print(i)
    if s == 2:
        name = input("Enter name of product: ")
        for i in inventory:
            if i['name'].lower().strip() == name.lower().strip():
                found = True
                print(i)
    if not found:
        print("No items with this data exist")

def item_exist(id):
    '''This function is a helper function that will not print something just will return
    True is the product is found in the inventory only take id as input. It is created to 
    not write seraching logic again and again in update/restock/sell functions'''

    found = False
    for i in inventory:
        if i['id'] == id:
            found = True
    if found:
        return True
    else:
        return False
    
def item_index(id):
    '''This is a helper function that will return the index position of an item found
    in the inventory'''
    idx = 0
    for i in inventory:
        if i['id'] == id:
           return idx
           break
        else:
            return False

def update():
    id = input("Enter id: ")
    exist = item_exist(id)
    if exist:
        index = item_index(id)
        print("1: Name")
        print("2: Categry")
        print("3: Cost Price")
        print("4: Selling Price")
        up = int(input("Enter your choice: "))
        
        if up == 1:
            n_name = input("Enter new name: ")
            inventory[index]['name'] = n_name        


    

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
        elif user_2 == 2:
            view()
        elif user_2 == 3:
            search()

