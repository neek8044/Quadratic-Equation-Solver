
import tkinter as tk
from tkinter import messagebox as msg
from math import sqrt
from matplotlib.animation import FuncAnimation
from pylab import *

WIDTH = 350
HEIGHT = 275


def calculate():

    a = int(entry_1.get())
    b = int(entry_2.get())
    c = int(entry_3.get())

    if a != 0:
        D = b ** 2 - 4 * a * c

        if D < 0:
            msg.showinfo("Solution", "This equation is unsolvable. Try again...")
        else:
            def roots_placement(x, y, z):
                delta = y ** 2 - 4 * x * z
                root1 = (-y + np.sqrt(delta)) / (2 * x)
                root2 = (-y - np.sqrt(delta)) / (2 * x)

                return root1, root2

            def quadratic_formula(x, a, b, c):
                return a * x ** 2 + b * x + c


            def update(frame):
                x_vals = np.linspace(-10, frame, 100)
                y_vals = quadratic_formula(x_vals, a, b, c)

                line.set_data(x_vals, y_vals)

                return line,


            fig, ax = plt.subplots()
            fig.patch.set_facecolor('silver')

            roots = roots_placement(a, b, c)


            x_vals_init = np.linspace(-10, 10, 2)
            y_vals_init = quadratic_formula(x_vals_init, a, b, c)
            line, = ax.plot(x_vals_init, y_vals_init, color='black', lw=2)

            ax.scatter(roots, [0, 0], color='red', marker='o', label='Roots')
            # ax.legend()

            ani = FuncAnimation(fig, update, frames=np.arange(-10, 11, 0.1), interval=1)

            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 50)

            gca().set_position((.1, .3, .8, .6))
            ax.set_xlabel('X-Axis')
            ax.set_ylabel('Y-Axis')
            ax.set_title('Live Graphing of the equation')
            if D == 0:
                figtext(.02, .1,
                        "Solution --->" + " " + " Following equation has 1 solution ::" + "  " + str(-b / (2 * a)))
                figtext(.02, .05, "[ Please close this window to proccess next task ]",color="black",backgroundcolor="royalblue")
            elif D > 0:
                figtext(.02, .1,
                        "Solution --->" + " " + " Following equation has 2 solution ::" + " " + str((-b + sqrt(D)) / (2 * a)) + " and " + str((-b - sqrt(D)) / (2 * a)))
                figtext(.02, .05, "[ Please close this window to proccess next task ]", color="black",backgroundcolor="royalblue")

            plt.show()

    else:
        msg.showerror("ERROR", "Value of [a] cannot be 0")


win = tk.Tk()
win.title("Quadratic Reimaginer [BETA]")
win.resizable(0, 0)
win.configure(bg="#3B3B3B")


xis = int((win.winfo_screenwidth() / 2) - (WIDTH / 2))
yis = int((win.winfo_screenheight() / 2) - (HEIGHT / 2))

win.geometry(f"{WIDTH}x{HEIGHT}+{xis}+{yis}")



label_1 = tk.Label(win, text = "Enter [a]", fg="white", bg="#636363")
label_1.config(font=("System", 11))
label_1.pack(pady = (10, 2))
entry_1 = tk.Entry(win)
entry_1.pack()


label_2 = tk.Label(win, text = "Enter [b]", fg="white", bg="#636363")
label_2.config(font=("System", 11))
label_2.pack(pady = (10, 2))
entry_2 = tk.Entry(win)
entry_2.pack()


label_3 = tk.Label(win, text = "Enter [c]", fg="white", bg="#636363")
label_3.config(font=("System", 11))
label_3.pack(pady = (10, 2))
entry_3 = tk.Entry(win)
entry_3.pack()


button_1 = tk.Button(win, text = "Calculate", bg="#1C86EE",command = calculate, padx = 6, pady = 4)
button_1.config(font=("System", 11))
button_1.pack(pady = (16, 0))


label_4 = tk.Label(win, text = "Tkinter - Neek8044\nMatplotlib - mpsk", fg = "#FFFFFF", bg="#3B3B3B")
label_4.config(font=("Lucida Handwriting", 11, "bold"))
label_4.pack(pady = (10, 2))


win.mainloop()
