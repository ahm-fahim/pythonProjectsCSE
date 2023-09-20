import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an Entry widget to display the input and results
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in a grid
row_val = 1
col_val = 0
for label in button_labels:
    if label == '=':
        tk.Button(root, text=label, padx=50, pady=50, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=label, padx=50, pady=50, command=lambda l=label: button_click(l)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
root.mainloop()
