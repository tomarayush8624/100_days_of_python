import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=200, pady=200)

# Label

my_label = tkinter.Label(text="I am a Label", font=("Aerial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.grid(column=0, row=0)

# button

def button_clicked():
    # print("Button got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=user_input.get())


button = tkinter.Button(text="Press", command=button_clicked)
button.grid(row=1,column=1)
# button.pack()

#another button

another_button = tkinter.Button(text="Press Me", command=button_clicked)
another_button.grid(row=0,column=2)

# Entry

user_input = tkinter.Entry(width=10)
user_input.grid(row=2,column=3)
# print(user_input.get())




window.mainloop()
