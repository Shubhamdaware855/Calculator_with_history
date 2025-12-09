import tkinter as tk
from tkinter import messagebox

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    if len(lines) == 0:
        messagebox.showinfo("History", "No history found")
    else:
        history_text = "".join(reversed(lines))
        messagebox.showinfo("History", history_text)

def clear_history():
    open(HISTORY_FILE, 'w').close()
    messagebox.showinfo("History", "History cleared...")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate():
    user_input = entry.get()
    parts = user_input.split()
    if len(parts) != 3:
        messagebox.showerror("Error", "Invalid Input")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        messagebox.showerror("Error", "Invalid number input")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Invalid input: division by zero")
            return
        result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid Operator")
        return

    if result.is_integer():
        result = int(result)

    result_label.config(text=f"Result: {result}")
    save_to_history(user_input, result)

root = tk.Tk()
root.title("Simple Calculator App")
root.geometry("350x300")

title = tk.Label(root, text="Simple Calculator", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate)
calc_button.pack(pady=5)

result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.pack(pady=10)

history_button = tk.Button(root, text="Show History", font=("Arial", 12), command=show_history)
history_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear History", font=("Arial", 12), command=clear_history)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
