import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Error", "Cannot divide by zero")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.configure(bg='#f0f0f0')

# Title Label
title_label = tk.Label(root, text="Simple Calculator", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
title_label.pack(pady=10, fill=tk.X)

# First Number Entry
entry1_label = tk.Label(root, text="Enter first number:", bg='#f0f0f0')
entry1_label.pack(pady=5)
entry1 = tk.Entry(root, width=10)
entry1.pack(pady=5)

# Second Number Entry
entry2_label = tk.Label(root, text="Enter second number:", bg='#f0f0f0')
entry2_label.pack(pady=5)
entry2 = tk.Entry(root, width=10)
entry2.pack(pady=5)

# Operation Buttons
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="+", command=add, bg="#4CAF50", fg="white", width=5, font=("Helvetica", 12, "bold"))
add_button.grid(row=0, column=0, padx=5, pady=5)

subtract_button = tk.Button(button_frame, text="-", command=subtract, bg="#4CAF50", fg="white", width=5, font=("Helvetica", 12, "bold"))
subtract_button.grid(row=0, column=1, padx=5, pady=5)

multiply_button = tk.Button(button_frame, text="*", command=multiply, bg="#4CAF50", fg="white", width=5, font=("Helvetica", 12, "bold"))
multiply_button.grid(row=1, column=0, padx=5, pady=5)

divide_button = tk.Button(button_frame, text="/", command=divide, bg="#4CAF50", fg="white", width=5, font=("Helvetica", 12, "bold"))
divide_button.grid(row=1, column=1, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg='#f0f0f0')
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()
