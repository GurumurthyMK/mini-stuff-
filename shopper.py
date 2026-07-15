# Create a product catalog and a shopping cart with the below features
# Product catalog : Display(), Edit(), Add(), Delete()
# Shopping card : Display(), Add(), Delete(), Checkout()

# Building the product catalog
products_cat = [
    {"Name": "Milk", "Price": 50, "SKU": 10},
    {"Name": "Curd", "Price": 60, "SKU": 10},
    {"Name": "Biscuit", "Price": 30, "SKU": 50},
    {"Name": "Maggi", "Price": 100, "SKU": 30},
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
                item["Name"] = n_name
                break
        return "Invalid entries"

    # defining logic for editing SKU
    def edit_sku():
        try:
            sku = int(input("Enter the name of the product to be modified: "))
        except ValueError:
            return "Invalid entry"

        for item in products_cat:
            if sku == item.get("SKU"):
                print("Product found")
                n_sku = int(input("Enter the new SKU: "))
                item["SKU"] = int(n_sku)
                break
        return "Invalid entries"

    # initial edit mode router
    def prd_edit():
        edit_mode = input(
            "Edit product name: 1\nEdit product SKU: 2\nEnter your choice : "
        )
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
        item_price = int(input("Enter the price of the item to added: "))
        item_sku = int(input("Enter the total SKU of product: "))
        # creating new entry to append
        new_entry = {"Name": item_name, "Price": item_price, "SKU": item_sku}
        # avoiding duplicates and append
        for i in products_cat:
            if i.get("Name") == new_entry.get("Name"):
                print("Duplicate found please use edit product option to modify")
            else:
                products_cat.append(new_entry)
        return "Invalid entries"

    def menu():
        while True:
            choices = input(
                "1. Display product catalog"
                "\n2. Edit products in log"
                "\n3. Add products to log"
                "\n4. Remove prodcuts from log"
            )
            if choices == "1":
                prd_cat_dis()
            elif choices == "2":
                prd_edit()
            elif choices == "3":
                add_prd()
            elif choices == "4":
                del_prd()
                break

    menu()


# Building shopping cart features
def shop_cart_feat(shopping_cart, products_cat):

    # display shopping cart items
    def tc_dis():
        for item in shopping_cart:
            print(item)

    # defining adding logic
    def add_prd_tc():
        tc_dis()
        add_name = input("Enter the name of the product to be added: ")
        add_sku = input("Enter the quantiy of the product: ")
        # creating a new entry to append to tc dict while checking for copies
        new_entry = {"Name": add_name, "SKU": int(add_sku)}
        for item in shopping_cart:
            if (new_entry.get("Name")) == item.get("Name"):
                print("Duplicate found")
            else:
                shopping_cart.append(new_entry)
        # modifying prodducts catalog to match new stock
        for item in products_cat:
            if item.get("Name") == new_entry.get("Name"):
                item["SKU"] = item["SKU"] - add_sku
        return "Invalid entries"

    # defining deleting logic
    def dlt_tc() -> None:
        tc_dis()
        name = input("Enter the name of the product to be deleted: ")
        dl_sku = int(
            input("Enter the number of these products to be removed from cart")
        )
        # safelly removing the mentioned amount of products
        for item in shopping_cart:
            if name == item.get("Name"):
                print("Product found, Now deleting.....")
                item["SKU"] = item["SKU"] - dl_sku
                if item["SKU"] == 0:
                    del item
                break

    # defining checkout logic
    def checkout_tc() -> None:
        tc_dis()
        # displaying total item cost
        for item in shopping_cart:
            item["Price"] = item["price"] * item["SKU"]
            total_cost = sum(item.get("Price"))
            print(f"The toal cost of items are: {total_cost}")
            if total_cost > 1000:
                total_cost = total_cost - total_cost / 100 * 10
                print(f"Applied discount of 10% - updated total: {total_cost}")
            elif total_cost > 5000:
                total_cost = total_cost - total_cost / 100 * 20
                print(f"Applied discount of 20% - updated total: {total_cost}")

        pay = input("Do you want to continue and pay (Y/N): ")
        if pay == "Y":
            print("Thank you for your purchase! ")
        else:
            print("Sure, please resume shopping")


    def menu():
        while True:
            choices = input(
                "1. Display products in cart"
                "\n2. Add products to cart"
                "\n3. Delete products from cart"
                "\n4. Checkout prodcuts from cart"
            )
            if choices == "1":
                tc_dis()
            elif choices == "2":
                add_prd_tc()
            elif choices == "3":
                dlt_tc()
            elif choices == "4":
                checkout_tc()
                break

    menu()

# defining router
def request_router():
    while True:
        personnel = input("Are you an admin(Y/n): ")
        if personnel == "Y":
            product_cat_feat(products_cat)
        else:
            shop_cart_feat(shopping_cart, products_cat)
request_router