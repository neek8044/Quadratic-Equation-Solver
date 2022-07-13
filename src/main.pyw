# Nick Roussis - Neek8044
# https://github.com/Neek8044/Quadratic-Equation-Solver

import tkinter as tk
from tkinter import messagebox as msg
from math import sqrt

WIDTH = 350
HEIGHT = 250


# Calculating the equation and displaying outputs on the screen as popup windows
def calculate():
    # Receives values from entry fields
    a = int(entry_1.get())
    b = int(entry_2.get())
    c = int(entry_3.get())

    # Solving the equation
    if a != 0:
        D = b ** 2 - 4 * a * c

        if D < 0:
            msg.showinfo("Output", "The equation is unsolvable.")
        elif D == 0:
            msg.showinfo("Output", "The equation has 1 double solution: " + str(-b / (2 * a)))
        elif D > 0:
            msg.showinfo("Output", "The equation has 2 solutions: " + str((-b + sqrt(D)) / (2 * a)) + " and " + str((-b - sqrt(D)) / (2 * a)))

    else:
        msg.showerror("Error", "Value a must not be 0")


win = tk.Tk()                           # Initialize
win.title("Quadratic Equation Solver")  # Set title
win.resizable(0, 0)                     # Configure window to not resizable
win.configure(bg="#505050")             # Set background color to darkgrey


# Finds where the window should be centered based on screen resolution
x = int((win.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((win.winfo_screenheight() / 2) - (HEIGHT / 2))

win.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")


# Value a
label_1 = tk.Label(win, text = "Value a:", fg="white", bg="#505050")
label_1.config(font=("helvetica", 11))
label_1.pack(pady = (10, 2))
entry_1 = tk.Entry(win)
entry_1.pack()

# Value b
label_2 = tk.Label(win, text = "Value b:", fg="white", bg="#505050")
label_2.config(font=("helvetica", 11))
label_2.pack(pady = (10, 2))
entry_2 = tk.Entry(win)
entry_2.pack()

# Value c
label_3 = tk.Label(win, text = "Value c:", fg="white", bg="#505050")
label_3.config(font=("helvetica", 11))
label_3.pack(pady = (10, 2))
entry_3 = tk.Entry(win)
entry_3.pack()

# Calculation
button_1 = tk.Button(win, text = "Calculate", command = calculate, padx = 6, pady = 4)
button_1.config(font=("helvetica", 11))
button_1.pack(pady = (16, 0))

# Watermark
label_4 = tk.Label(win, text = "by Neek8044", fg = "#c0c0c0", bg="#505050")
label_4.config(font=("helvetica", 11, "bold"))
label_4.pack(pady = (10, 2))

"""
Explanation of the above scripts:

# Set label text to "Value x:", text color to white, background color to darkgrey
label = tk.Label(win, text="Value x:", fg="white", bg="#505050")

# Configure text font of label to "Helvetica" with font size 11
label.config(font=("helvetica", 11))

# Display the label in the window with margin (outer padding) of 10px on top, 2px on bottom
label.pack(pady = (10, 2))

# Set entry field so the user can enter a value
entry = tk.Entry(win)

# Display the entry field in the window
entry.pack()

"""

win.mainloop()
