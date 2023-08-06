from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project\

def generate_password():
    print("error")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password_letter = [random.choice(letters) for item in range(nr_letters)]
    password_number = [random.choice(numbers) for item in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]

    password_list = password_letter + password_symbols + password_number

    random.shuffle(password_list)

    # output = ""
    # for i in password_list:
    #     output += i

    password = "".join(password_list)

    # generate text into entry
    password_entry.insert(0, password)
    # copy the password ready to paste
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("save_passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=155, height=200)
lock_png = PhotoImage(file="logo.png")
# 100 and 1000 in argument are location of picture which are center of the windows
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "arrarose@gmail.com")

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
