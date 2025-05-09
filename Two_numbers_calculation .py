
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

def add_function (num1,num2):
    add_num = num1 + num2
    return add_num
output = add_function (num1,num2)
print(f"Addition of {num1} and {num2} is {output}")

def sub_function (num1,num2):
    subtract_num = num1 - num2
    return subtract_num
output = sub_function (num1,num2)
print(f"Subtraction of {num1} and {num2} is {output}")

def multiply_function (num1,num2):
    multiply_num = num1 * num2
    return multiply_num
output = multiply_function (num1,num2)
print(f"Multiplication of {num1} and {num2} is {output}")

def div_function (num1,num2):
    divie_num = num1 / num2
    return divie_num
output = div_function (num1,num2)
print(f"Division of {num1} and {num2} is {output}")