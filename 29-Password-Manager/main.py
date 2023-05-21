from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password1 = [choice(letters) for _ in range(randint(8, 10))]
    password2 = [choice(symbols) for _ in range(randint(2, 4))]
    password3 = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password1 + password2 + password3
    shuffle(password_list)

    # print(password_list)

    password_final = ''.join(str(x) for x in password_list)
    # pyperclip.copy(password_final)
    password.insert(0, string=f"{password_final}")


# ----------------------------GET PASSWORD-----------------------------------#
def get_pass():
    try:
        with open("data.json", "r") as x:
            dict1 = json.load(x)
    except FileNotFoundError:
        messagebox.showinfo("Error", f"No Passwords saved yet")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo("Error", f"No Passwords saved yet")
    else:
        if website.get() in dict1:
            messagebox.showinfo("Password", f"The password for {website.get()} is {dict1[website.get()]['password']}")
        else:
            messagebox.showinfo("Error", f"Password not found for {website.get()}")
    finally:
        website.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_info():
    if len(website.get()) != 0 and len(password.get()) != 0:

        new_data = {
            website.get(): {
                "email": email.get(),
                "password": password.get(),
            }
        }
        try:
            with open("data.json", "r") as x:
                data = json.load(x)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as x:
                json.dump(new_data, x, indent=4)
        else:
            with open("data.json", "w") as x:
                json.dump(data, x, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)
    else:
        messagebox.showinfo("Error", "Please Fill all the Input Fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)

label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)

label3 = Label(text="Password:")
label3.grid(row=3, column=0)

website = Entry(width=42)
website.grid(row=1, column=1, columnspan=2)
website.focus()

email = Entry(width=42)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, string="ayushrajput1708@gmail.com")

password = Entry(width=24)
password.grid(row=3, column=1)

# buttons
b1 = Button(text="Generate Password", width=14, command=gen_password)
b1.grid(row=3, column=2)

b2 = Button(text="Add", width=40, command=write_info)
b2.grid(row=4, column=1, columnspan=2)

b3 = Button(text="search", width=14, command=get_pass)
b3.grid(row=1, column=2)

window.mainloop()
