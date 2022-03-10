"""
Program: orders.py
Author: Justin Merwin
Purpose: Utilize OOP to create an application that allows the user to create, delete, or modify orders.
         This allowed me to practice a variety of fundamental concepts.
"""

order_amount = ""
order_type = ""
order_number = ""

class OrderClass:
    def __init__(self, order_amount, order_type, order_number):
        self.order_amount = order_amount
        self.order_type = order_type
        self.order_number = order_number

    def setAmount(self, order_amount):
        self.amount = order_amount

    def setType(self, order_type):
        self.order_type = order_type

    def setNumber(self, order_number):
        self.order_number = order_number

    def orderAmount(self):
        return self.order_amount

    def orderType(self):
        return self.order_type

    def orderNumber(self):
        return self.order_number

    def orderRemove(self):
        try:
            orderRemove_number = int(input("Enter order to remove: "))
        except ValueError:
            print("Invalid input, try again.")

    def orderEdit(self):
        try:
            orderEdit_number = int(input("Enter order to edit: "))
        except ValueError:
            print("Invalid input, try again.")

    def orderDisplay(self):
        print(15 * "=", "Order List", 15 * "=")
        print("Order Number: ", self.orderNumber())
        print("Order Type: ", self.orderType())
        print("Order Amount:", self.orderAmount())
        print(41 * "=")

def menuPrint():
    print(15 * "=", "McMenu", 15 * "=")
    print("1. Display Orders.")
    print("2. Add New Order.")
    print("3. Remove Order.")
    print("4. Edit Order.")
    print("5. Save Order.")
    print("6. Exit")
    print(41 * "=")

def main():
    orders = []
    while True:
        menuPrint()
        menuChoice = int(input("Pick an option: "))
        if menuChoice == 1:
            for order in orders:
                order.orderDisplay()
        elif menuChoice == 2:
            try:
                order_number = int(input("What is your order number? "))
                order_type = str(input("What is your order type? "))
                order_amount = float(input("What is your order amount? "))
                order = OrderClass(order_amount, order_type, order_number)
                orders.append(order)
            except:
                print("Invalid input. Try again.")
        elif menuChoice == 3:
            try:
                order_number = int(input("Which order would you like to remove? "))
                for order in orders:
                    if order.orderNumber() == order_number:
                        orders.remove(order)
            except:
                    print("Invalid order. Try again. ")
        elif menuChoice == 4:
            try:
                order_number = input("Which order would you like to edit? ")
                for order in orders:
                    if order.orderNumber() == order_number:
                        new_number = input("Enter new order number: ")
                        new_type = input("Enter new order type: ")
                        new_amount = input("Enter new amount: ")
                        order.setNumber(new_number)
                        order.setType(new_type)
                        order.setAmount(new_amount)
                        print(order_number, "has been changed to:", new_number)
            except:
                    print("Invalid order number. Try again. ")
        elif menuChoice == 5:
            file_name = input("Enter file name: ")
            print("Saving...")
            f = open(file_name, "w")
            for order in orders:
                f.write(order.orderNumber() + "," + order.orderType() + "," + order.orderAmount() + "\n")
            f.close()
            print("Data saved")
        elif menuChoice == 6:
            print("Exiting... ")
            break
        else:
            print("Exiting... ")
            break

if __name__ == "__main__":
    main()
