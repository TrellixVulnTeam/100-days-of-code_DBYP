from tkinter import *


def button_clicked():
    # print("I got clicked")
    new_text = input.get()#hold the value that came from the entry
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()#place the label into the screen, it's going to automatically center it on the screen
#my_label.pack(side="left")#it doesn't have any layout specified
#my_label.pack(expand=True)
#my_label.place(x=100, y=200)#the downside of place is that we have to work out in our head the coordinate
my_label.grid(column= 0, row=0)#the grids system is relative to other components.
'''So the easiest way of working with the grid is starting with the things that you want it to be at the top left, 
defining a starting column and rows (0, 0), and then for the next and subsequent widgents to just keep going through 
it and define its position on the grid.'''
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
# print(input.get())
# input.pack()
input.grid(column=3, row=2)

'''grid() is a preferred way of working with the layout for tkinter. However, you can't mix up grid and pack in the same program.'''





window.mainloop()  # keeps on the screen, always need to be at the end of the program
