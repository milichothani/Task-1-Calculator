import tkinter as tk
from tkinter import messagebox
import sys

def evaluate_expression(expr):
    try:
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Invalid characters in expression.")
        return eval(expr)
    except Exception:
        return "Error"

if len(sys.argv) > 1:
    expr = " ".join(sys.argv[1:])
    print(evaluate_expression(expr))
    sys.exit(0)

def on_click(char):
    if char == 'C':
        entry.delete(0, tk.END)
    elif char == '=':
        result = evaluate_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.resizable(False, False)

entry = tk.Entry(root, font=('Arial', 18), justify='right', bd=8, relief='ridge')
entry.pack(fill='both', padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

frame = tk.Frame(root)
frame.pack()

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(
            frame, text=char, font=('Arial', 16), width=5, height=2,
            command=lambda ch=char: on_click(ch)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)

root.mainloop()
