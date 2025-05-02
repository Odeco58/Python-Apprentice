"""487578585
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog 
number1 = simpledialog.askinteger("Your number", "Pick a number.")
number2= simpledialog.askinteger("Your number", "Pick a number.")
operator = simpledialog.askstring("Your number", "Pick an operator.")
if operator =="/": 
 division = number1 / number2
 messagebox.showinfo('What you are', division)
elif operator == "*": 
 multiplication = number1 * number2
 messagebox.showinfo('What you are', multiplication)
elif operator == "-": 
 subtraction = number1 - number2
 messagebox.showinfo('What you are', subtraction)
elif operator == "+": 
 addition = number1 + number2
 messagebox.showinfo('What you are', addition)






# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Display the sum of the two numbers 

# Keep the window open

