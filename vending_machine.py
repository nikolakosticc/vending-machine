import time

product_list = {"Chocolate" : {"quantity" : 1, "price" : 1.5}, "Flips" : {"quantity" : 2, "price" : 1.0}, "Coca Cola" : {"quantity" : 3, "price" : 0.5}}

print("Available items : ")
print("")
print("Chocolate")
print("Flips")
print("Coca Cola")
print("")

def vend():
    global product_list
    product_input = input("Enter a product : ")
    start_time = time.time()

    if product_list[product_input]["quantity"] > 0:
        money = float(input("Enter : " + str("$") + str(product_list[product_input]["price"]) + str(" ")))
        elapsed_time = time.time() - start_time
        if elapsed_time <= 10:
            if money == product_list[product_input]["price"]:
                print("Purchase Succsessfull")
                product_list[product_input]["quantity"] -= 1
            else:
                enter_again = input("Enter 1.5$")
            if product_list[product_input]["quantity"] == 0:
                print("We ran out of certain product")

            vend_again = input("Would you like to buy again y/n?")
            if vend_again == "y":
                vend()
            else:
                return
    else:
        print("U didn't enter the money on time, reseting the vending machine")
        vend()
vend()
