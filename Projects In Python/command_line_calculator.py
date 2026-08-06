print('Hello, Welcome To Simple Calculator!')
i=int(input('Enter first number: '))
j=int(input('Enter second number: '))
k=input('Enter operation (+, -, *, /): ')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b
    
if k == '+':
    print(f'{i} + {j} = {add(i, j)}')
elif k == '-':
    print(f'{i} - {j} = {subtract(i, j)}')
elif k == '*':
    print(f'{i} * {j} = {multiply(i, j)}')
elif k == '/':
    print(f'{i} / {j} = {divide(i, j)}')
else:
    print('Invalid operation! Please enter a valid operation (+, -, *, /).')

