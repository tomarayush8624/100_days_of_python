from tkinter import *

window = Tk()
window.title = "My Second GUI Program"
window.minsize(width=500, height=300)

# Label
main_label = Label(text="I am a a Label", font=("Arial", 24))
main_label.pack()


# button
def button_clicked():
    main_label.config(text=input1.get())


button = Button(text="click me ", command=button_clicked)
button.pack()

# Input Field
input1 = Entry(width=5)
input1.pack()

window.mainloop()
