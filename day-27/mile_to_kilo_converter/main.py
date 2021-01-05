from tkinter import *


def calculate():
    miles = float(input.get())
    km = round(miles * 1.609)
    converted_km_label.config(text=f"{km}")


window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

converted_km_label = Label(text="0")
converted_km_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()  # keeps on the screen, always need to be at the end of the program
