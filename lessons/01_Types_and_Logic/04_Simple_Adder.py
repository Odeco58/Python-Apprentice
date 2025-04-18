"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""
from tkinter import messagebox, simpledialog, Tk
division = number1 / number2
multiplication = number1 * number2
addition = number1 + number2
subtraction = number1 - number2
operator = "division, multiplication, addition, subtraction "
number1 = simpledialog.askinteger("Your number", "Pick a number.")
number2= simpledialog.askinteger("Your number", "Pick a number.")
messagebox.showinfo("wehth",number1 + number2)


# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Display the sum of the two numbers 

# Keep the window open

