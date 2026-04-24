class Product_EIV:
    def __init__(self_EIV, name_EIV, price_EIV, quantity_EIV):
        self_EIV.__name_EIV = name_EIV
        self_EIV.__price_EIV = price_EIV
        self_EIV.__quantity_EIV = quantity_EIV

    def get_product_info_EIV(self_EIV):
        print("Product:", self_EIV.__name_EIV)
        print("Price:", self_EIV.__price_EIV)
        print("Quantity:", self_EIV.__quantity_EIV)

    def update_quantity_EIV(self_EIV, new_quantity_EIV):
        if new_quantity_EIV >= 0:
            self_EIV.__quantity_EIV = new_quantity_EIV

    def update_price_EIV(self_EIV, new_price_EIV):
        if new_price_EIV > 0:
            self_EIV.__price_EIV = new_price_EIV

# Example usage
product_EIV = Product_EIV("Laptop", 45000, 10)
product_EIV.get_product_info_EIV()
