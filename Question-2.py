import re


def supermarket_shopping(budgets):
    product_name = input("\nEnter product : ")
    product_quantity = float(re.findall(r"[-+]?\d*\.\d+|\d+", input("Enter quantity : "))[0])
    product_price = float(input("Enter price : "))

    amount_left = 0
    for values in shopping_list.values():
        amount_left += values[1]
    amount_left = budgets - amount_left

    if amount_left < product_price:
        print("\nCan't buy the product because it's price is more than left amount.\n")
    else:
        amount_left = 0
        if product_name in shopping_list:
            shopping_list[product_name][0], shopping_list[product_name][1] = product_quantity, product_price
        else:
            shopping_list[product_name] = []
            shopping_list[product_name].append(product_quantity)
            shopping_list[product_name].append(product_price)
        for values in shopping_list.values():
            amount_left += values[1]
        amount_left = budgets - amount_left
        print("\nAmount left : {0}.\n".format(amount_left))


if __name__ == "__main__":
    shopping_list = {}
    budget = int(input("Enter Your Budget : "))
    while True:
        choice = input(
            "1. Add an item.\n2. Exit.\nEnter Your Choice : ")
        if choice == "1":
            supermarket_shopping(budgets=budget)
        elif choice == "2":
            amount_left = 0
            for values in shopping_list.values():
                amount_left += values[1]
            amount_left = budget - amount_left
            product = ""
            max_price_product = 0.0
            for j, i in shopping_list.items():
                if i[1] <= amount_left:
                    if max_price_product < i[1]:
                        product = j
                        max_price_product = i[1]
            if len(product):
                print("\nAmount left can buy you {0}.\n".format(product))
                print("Grocery List is :")
                print("Product Name\tQuantity\tPrice")
                for i, j in shopping_list.items():
                    print(i, "\t", str(j[0]) + " kg", "\t", j[1])
            else:
                exit("Goodbye!!!")
        else:
            print("!!! Wrong Selection.\n")
