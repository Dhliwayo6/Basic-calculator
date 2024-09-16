def add(a, b):
     return a + b

def subtract(a, b):
     return a - b

def multiply(a, b):
     return a * b

def divide(a, b):
     if b != 0:
          return a/b
     else:
          print('Cannot divide by 0!')

num1 = int(input("Enter the first number: "))
operator = input("Select an operator +,-,*,/: ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    sum = add(num1, num2)
    print(f"The sum is {sum}")
elif operator == "-":
     difference = subtract(num1, num2)
     print(f"The difference is {difference}")
elif  operator == "*":
     product = multiply(num1, num2)
     print(f"The product is {product}")
elif  operator == "/":
     quotient = divide(num1, num2)
     print(f"The quotient is {quotient}")
else:
     print("Invalid option")