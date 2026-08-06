

import tkinter as tk

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




def button_click(character):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(character))

# Clears the screen
def clear_field():
    entry.delete(0, tk.END)


def calculate():
    expression = entry.get()
    
    # Checking Operator Used
    for operator in ['+', '-', '*', '/']:
        if operator in expression:
            # Split the text box string into the two numbers
            parts = expression.split(operator)
            
            # Dividing Into Parts To Calculate
            if len(parts) == 2 and parts[0] != '' and parts[1] != '':
                num1 = int(parts[0])
                num2 = int(parts[1])
                
                # Call of functions 
                if operator == '+':
                    result = add(num1, num2)
                elif operator == '-':
                    result = subtract(num1, num2)
                elif operator == '*':
                    result = multiply(num1, num2)
                elif operator == '/':
                    result = divide(num1, num2)
                
                # Display of result
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
                return
                
    # In Case Of Error
    entry.delete(0, tk.END)
    entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

# Calculator screen display
entry = tk.Entry(root, width=14, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout (Text, Row, Column)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Dynamic Buttons Using Loop
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=clear_field)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), 
                        command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, sticky="nsew")

root.mainloop()