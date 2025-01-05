# define functions

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return ("Error Division by 0")
    else:
       return a / b
    

def calculator ():
    print("Welcome to Chief Odili Calculator written with Python")

    #collect input
    try:
        data1 = int(float(input("Enter your first number: ")))
        data2 = int(float(input("Enter your second number: ")))

    except ValueError:
        print("Invalid input! only numeric values are accepted and processed")
        return
    
    print("Select an operation below:")
    

    # take operation input

    operation = input("Enter the operation (+,-,*,/): ")

    # perfom the selected operation

    if operation == "+":
        print(f"\n The solution to {data1} + {data2} = {add(data1, data2)}")
    elif operation == "-":
        print(f"\n The solution to {data1} - {data2}= {subtract(data1, data2)}")
    elif operation == "*":
        print(f"\n The solution to {data1} * {data2}= {multiply(data1, data2)}")
    elif operation == "/":
        print(f"\n The solution to {data1} / {data2}= {divide(data1, data2)}")
    else:
        print("invalid input, Kindly choose a valid operation which include (+, -, *, and /)")
    
# Ask the user if they want to perform another calculation
    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if again == "yes":
        calculator()  # Recursively call the calculator function again
    else:
        print("Thank you for using the calculator!")

# Start the calculator program
calculator()

