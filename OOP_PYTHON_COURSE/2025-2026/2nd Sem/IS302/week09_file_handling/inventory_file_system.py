product_EIV = input("Enter product name: ")
price_EIV = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_EIV + "," + price_EIV + "\n")

print("Product saved successfully")
