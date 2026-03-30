num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        
    else:
        print("Error: Division by zero")
else:   
    print("Invalid operation")
    result = None

if result is not None: 
    equation = f"{num1} {operation} {num2} = {result}"
    print(f"Result: {equation}")

# Write the result to a file
with open("equations.txt", "a") as file:
    if result is not None:
        file.write(f"{equation} = {result}\n")
    
# Read and display the contents of the file
try:
    with open("equations.txt", "r") as file:
        content = file.read()
        if content:
            print("\nPrevious calculations:")
            print(content)
        else:
            print("\nNo previous calculations found.")
except FileNotFoundError:
    print("\nNo previous calculations found.")
