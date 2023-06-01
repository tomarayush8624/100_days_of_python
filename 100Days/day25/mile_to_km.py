import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer Convertor")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def button_press():
    # print(input_txt.get())
    conversion = int(input_txt.get()) * 1.609
    output_label.config(text=conversion)


#inut text

input_txt = tkinter.Entry(width=10)
input_txt.insert(tkinter.END, string="0")
miles = input_txt.get()
input_txt.grid(row=0, column=1)
# input_txt.pack()

# labels

first_label = tkinter.Label(text="is equal to", font=("Aerial", 20))
first_label.grid(row=1, column=0)

second_label = tkinter.Label(text="Miles", font=("Aerial", 20))
second_label.grid(row=0, column=2)

output_label = tkinter.Label(text="0", font=("Aerial", 20))
output_label.grid(row=1, column=1)
output_label.config(padx=10, pady=10)

third_label = tkinter.Label(text="Km", font=("Aerial", 20))
third_label.grid(row=1, column=2)

# Calculate Button

button = tkinter.Button(text="Calculate", command=button_press)

button.grid(row=2, column=1)

window.mainloop()