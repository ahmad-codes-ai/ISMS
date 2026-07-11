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

sales = []

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
    found = False
    idx = 0
    for i in inventory:
        if i['id'] == id:
           found = True
           break
        idx+=1

    if found:
        return idx
    else:
        return "Item not found"
    

def update():
    id = int(input("Enter id: "))
    exist = item_exist(id)
    print(exist)
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
        elif up == 2:
            n_cat = input("Enter new category: ")
            inventory[index]['category'] = n_cat
        elif up == 3:
            n_cost = int(input("Enter new cost price: "))
            inventory[index]['cost_price'] = n_cost
        elif up == 4:
            n_sell = int(input("Enter new selling price: "))
            inventory[index]['selling_price'] = n_sell
        else:
            print("Invalid Input")

def delete():
    id = int(input("Enter product id: "))
    exist = item_exist(id)

    if exist:
        idx = item_index(id)
        print(inventory[idx])
        de = input('Are you sure you want to delete this product (y/n)')

        if de == 'y':
            inventory.pop(idx)
            print('This product has been deleted successfully')
        elif de == 'n':
            print('Deletition cancelled')
        else:
            print("Invalid Input given")

    print(inventory)

def restock():
    id = int(input("Enter the id of the product: "))
    exist = item_exist(id)

    if exist:
        idx = item_index(id)
        n_stock = int(input("Enter the amount of items to add in stock: "))
        inventory[idx]['stock']+=n_stock
    else:
        print('Item not found')

def stock_alert():
    for i in inventory:
        if i['stock'] < 3:
            print(f"{i['name']} has low stock: {i['stock']}")

def sell():
    id = int(input("Enter product id: "))
    exist = item_exist(id)

    if exist:
        idx = item_index(id)
        print(f"The product {id} has a stock of {inventory[idx]['stock']}")
        quan = int(input("Enter the amount of product you want to sell: "))
        stock = inventory[idx]['stock']

        if quan < stock or quan == stock:
            profit_1p = inventory[idx]['selling_price'] - inventory[idx]['cost_price'] 
            total_p = profit_1p * quan
            inventory[idx]['sold']+=quan
            inventory[idx]['stock']-=quan
            print(f"{quan} peices of {inventory[idx]['name']} has been sold")
            print(f"Your profit is: {total_p}")
            d = {'id':inventory[idx]['id'], 'sold':inventory[idx]['sold'], 'profit':total_p ,
                 'profit_1p':profit_1p}
            sales.append(d)
        else:
            print(f'Plz enter a value less then or equal to stock: {stock}')

def sale_history():
    for i in inventory:
        print(i)

def return_product():
    id = int(input("Enter product id: "))
    exist = item_exist(id)

    if exist:
        idx = item_index(id)
        quan = int(input("Enter the number of products to return: "))
        inventory[idx]['stock']+=quan
        inventory[idx]['sold']-=quan

        for i in sales:
            if i['id'] == id:
                tp = i['profit_1p'] * quan
                i['profit']-=tp
    else:
        print('Item not found')

    print(inventory)
    print(sales)

def sales_summary():
    total_p = 0
    total_s = 0
    for i in inventory:
        sold = i['sold']
        profit = i['selling_price'] - i['cost_price']
        total_p = total_p + (sold*profit)
        total_s+=sold
    
    print(f"Total products sold: {total_s}")
    print(f"Total profit: {total_p}")
     
def best_selling():
    top = 0
    name = ""
    for i in inventory:
        sold = i['sold']
        if sold > top:
            top = sold
            name = i['name']
    for i in inventory:
        if i["name"] == name:
            t_sold = i['sold']

    print(f"Your most selling product is {name} with {t_sold} items sold")

while True:
    print('------------ Inventory Sales Managment System ------------')
    print("1. Inventory")
    print("2. Sales")
    print("3. Reports")
    print("4. Exit")
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
        elif user_2 == 4:
            update()
        elif user_2 == 5:
            delete()
        elif user_2 == 6:
            restock()
        elif user_2 == 7:
            stock_alert()
        elif user_2 == 8:
            continue

    elif user_1 == 2:
        print("1. Sell Product")
        print("2. View Sales History")
        print("3. Return Product")
        print("4. Back")

        user_22 = int(input("Enter Your choice: "))

        if user_22 == 1:
            sell()
        elif user_22 == 2:
            sale_history()
        elif user_22 == 3:
            return_product()
        elif user_22 == 4:
            continue
        else:
            print("Invalid input")

    elif user_1 == 3:
        print("1. Sales Summary")
        print("2. Best Selling Product")
        print("3. Back")

        user_33 = int(input("Enter your choice: "))

        if user_33 == 1:
            sales_summary()
        elif user_33 == 2:
            best_selling()
        elif user_33 == 3:
            continue
        else:
            print("Invalid Input")
    
    elif user_1 == 4:
        print("Thanks for using this system. GoodBye !!")
        break



print(inventory)
print(sales)