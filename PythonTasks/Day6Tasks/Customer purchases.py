"""2: Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).
Example Output:
1. Display Products
2. Add Item to Cart
3. View Total Bill
4. Exit
Enter choice: 1
Available Products:
Pen : 10
Notebook : 50
Pencil : 5
1. Display Products
2. Add Item to Cart
3. View Total Bill
4. Exit
Enter choice: 2
Enter product name: Pen
Enter quantity: 3
Item added to cart successfully.
1. Display Products
2. Add Item to Cart
3. View Total Bill
4. Exit
Enter choice: 2
Enter product name: Notebook
Enter quantity: 2
Item added to cart successfully.
1. Display Products
2. Add Item to Cart
3. View Total Bill
4. Exit
Enter choice: 3
Items in Cart:
Pen x 3
Notebook x 2
Total Bill: 130
Example Exception Outputs
ValueError
Enter quantity: abc
Invalid quantity! Please enter a number.
NameError
Enter product name: Eraser
Product not found in store.
TypeError
Cart data type error.
ZeroDivisionError
Calculation error: division by zero"""



# Product names and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Product categories using set
categories = {"Stationery", "Writing", "Education"}

# Product details using tuples
product_details = (
    ("Pen", 10),
    ("Notebook", 50),
    ("Pencil", 5)
)

# Cart using list
cart = []


# Function to display products
def display_products():
    print("\nAvailable Products:")
    for name, price in products.items():
        print(name, ":", price)


# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart.append((name, quantity))
        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")


# Recursive function to calculate total
def recursive_total(index=0):
    if index == len(cart):
        return 0

    name, quantity = cart[index]
    price = products[name]

    return (price * quantity) + recursive_total(index + 1)


# Function to calculate total bill
def calculate_bill():
    try:
        print("\nItems in Cart:")

        for name, quantity in cart:
            print(name, "x", quantity)

        total = recursive_total()
        print("Total Bill:", total)

        # Demonstration of ZeroDivisionError handling
        if total < 0:
            raise ZeroDivisionError

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero")


# Main menu
while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            calculate_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number.")










































