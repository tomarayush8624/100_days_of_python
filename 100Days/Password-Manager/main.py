import tkinter

FONT = ("sans-serif", 15)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(window, width=200, height=200)
logo_ing = tkinter.PhotoImage(file="logo.png")
logo_instance = canvas.create_image(100, 100, image=logo_ing)
# canvas.config( padding=10)
canvas.grid(row=0, column=1)

#Labels / texts

tkinter.Label(text="Website:", font=FONT).grid(row=1, column=0)
tkinter.Label(text="Email/Username:", font=FONT).grid(row=2, column=0)
tkinter.Label(text="Password:", font=FONT).grid(row=3, column=0)


# Entery Fields

website_input = tkinter.Entry(width=39)
website_input.grid(row=1, column=1, columnspan=2)
email_input = tkinter.Entry(width=39)
email_input.grid(row=2, column=1, columnspan=2)
password_input = tkinter.Entry(width=20)
password_input.grid(row=3, column=1)

#buttons
generate_pass_button = tkinter.Button(text="Generate Password")
generate_pass_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)




tkinter.mainloop()
