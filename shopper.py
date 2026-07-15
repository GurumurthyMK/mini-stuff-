# Create a product catalog and a shopping cart with the below features 
# Product catalog : Display(), Edit(), Add(), Delete()
# Shopping card : Display(), Add(), Delete(), Edit(), Checkout() 

# Building the product catalog 
products_cat = [
    {"Name": "Milk", "Price": 50, "SKU": 10},
    {"Name": "Curd", "Price": 60, "SKU": 10},
    {"Name": "Biscuit", "Price": 30, "SKU": 50},
    {"Name": "Maggi", "Price": 100, "SKU": 30}
]

# inititalising empty schopping cart
shopping_cart = [{}]


# Product catalog features 
def product_cat_feat(products_cat):
    # displaying product catalog
    def prd_cat_dis():
        for item in products_cat:
            print(item)
    
    # defining logic for editing name
    def edit_name():
        name = input("Enter the name of the product to be changed: ")
        for item in products_cat:
            if name == item.get("Name"):
                print("Product found")
                n_name = input("Enter the new name: ")
                item["Name"] == n_name
                break
        return "Invalid entries"
    
    # defining logic for editing SKU 
    def edit_sku():
        sku = input("Enter the name of the product to be modified: ")
        for item in products_cat:
            if sku == item.get("SKU"):
                print("Product found")
                n_sku = input("Enter the new SKU: ")
                item["SKU"] == n_sku
                break
        return "Invalid entries" 
  
    # initial edit mode router
    def prd_edit():
        edit_mode = input("Edit product name: 1"
                          "\nEdit product SKU: 2"
                          "\nEnter your choice : ")  
        if "1" in edit_mode:
            edit_name()
        elif "2" in edit_mode:
            edit_sku()
        else:
            "Invalid input"
   
    # defining deletion logic
    def del_prd():
        name = input("Enter the name of the product to be deleted: ")
        for i, item in enumerate(products_cat):
            if name == item.get("Name"):
                print("Product found, Now deleting.....")
                products_cat.pop(i)
                break
        return "Invalid entries"
    
    # defining adding product logic
    def add_prd():
        item_name = input("Enter the name of the product to be added: ")
        item_price = input("Enter the price of the item to added: ")
        item_sku = input("Enter the total SKU of product: ")
        # creating new entry to append 
        new_entry = { "Name": item_name, "Price": item_price, "SKU": item_sku}
        # avoiding duplicates and append 
        for i in products_cat:
            if not any(i.get("Name")) == new_entry.get("Name"):
                products_cat.append(new_entry)
            else:
                print("Duplicate found please use edit product option to modify")
        return "Invalid entries"
    
    


