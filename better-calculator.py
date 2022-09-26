# 'Better' Calculator

# add 'float' in front of input to convert any possible float values
# the values num1 num2 and op show that we will need two numbers and an operator to make a proper calculator
# if statements will better define the conditions we need so the 'op' or operator functions well with
# if the user does not want to use the operators stated below, use the 'else' condition to output invalid operation
# i am using the round function so I do not have to see so many decimals
# also do not forget to name your variables
#

num1 = float(input("Enter your first number: "))
 op = input("Enter operator: ")
num2 = float(input("Enter your first number: "))

 if op == "+":
     print(round(num1 + num2))
 elif op == "-":
     print(round(num1 - num2))
 elif op == "/":
     print(round(num1 / num2))
 elif op == "*":
     print(round(num1 * num2))
 else:
     print("Invalid operator")
