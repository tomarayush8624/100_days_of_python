from tkinter import *


def miles_to_km():
    label3.config(text=f"{float(input_miles.get())*1.60934}")

window = Tk()
window.title(string="Miles to Km")
# window.minsize(width=400, height=200)
window.config(padx=50, pady=30)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to ")
label2.grid(row=1, column=0)

label3 = Label(text="0", font=("Arial", 24, "bold"))
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)

button1 = Button(text="Calculate", command=miles_to_km)
button1.grid(row=2, column=1)

window.mainloop()
