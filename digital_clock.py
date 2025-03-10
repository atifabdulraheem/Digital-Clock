from tkinter import *
from time import strftime

# Initialise Root Window
root = Tk()

# Main Code Begins From Here......


def show_time():
    current_time = strftime("%H:%M:%S %p")
    # print(current_time)
    label = Label(root, text=current_time, font=(
        "Arial", 80, 'bold'), fg="black")
    label.after(300, show_time)
    label.grid(row=0, column=1)


# Root Window Configuratiomn
root.resizable(False, False)
root.title("ATIF Digital")
show_time()
root.mainloop()