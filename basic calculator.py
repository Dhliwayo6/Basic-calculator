'''
The addition function uses two parameters(integers) and 
returns the sum of the numbers
'''

def add(a, b):
     return a + b

'''
The subtract function uses two parameters(integers) and 
returns the difference between the numbers
'''

def subtract(a, b):
     return a - b

'''
The multiply function uses two parameters(integers) and 
returns the profuct of the numbers
'''

def multiply(a, b):
     return a * b

'''
The divide function receives two parameters(integers) and 
returns a float which is a result of the division of 2 numbers
The function also makes sure that the denominator is not a 0 or it returns a prompt
'''

def divide(a, b):
     if b != 0:
          return a/b
     else:
          print('Cannot divide by 0!')
''' The while loop is used here to
allow the user to make calculations consecutively, 
one after the other without having to re-run the program
'''
while True:
     #to handle for errors, the try and except blocks are 
     try:
          num1 = float(input("Enter the first number: "))
          operator = input("Select an operator +,-,*,/ or q to quit the program: ")
          if operator == "q":
               break
          num2 = float(input("Enter the second number: "))

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
               if quotient != None:
                    print(f"The quotient is {quotient}")
          else:
               print("Invalid option")
     except ValueError: # handles integer related errors
          print('You need to input a number')

     except: # handles every other error
          print('An error came up, try again')