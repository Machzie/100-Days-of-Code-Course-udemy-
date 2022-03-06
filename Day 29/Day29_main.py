# Day 29 Project - Password Manager

import tkinter
from tkinter import messagebox
from PasswordGenerator import generated_password


def save_to_file():
    """Adds the entry data to a text file and clears the current inputs from the GUI"""
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()

    if len(website) == 0:
        messagebox.showerror(title="Website Error", message="Please enter a website")
    elif len(username) == 0:
        messagebox.showerror(title="Username Error", message="Please enter a username or email")
    elif len(password) == 0:
        messagebox.showerror(title="Password Error", message="Please enter a password")
    else:
        answer = messagebox.askyesno(title=website, message=f"Are the following details correct?\n\n"
                                                            f"Username: {username}\n"
                                                            f"Password: {password}")
        if answer:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")

        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry2.insert(0, '@gmail.com')
        entry3.delete(0, 'end')


def generate_password():
    entry3.delete(0, 'end')
    gpw = generated_password
    entry3.insert(0, gpw)
    pass


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# ---------- Website ---------- #
label1 = tkinter.Label(text="Website:", bg="white")
label1.grid(column=0, row=1)
entry1 = tkinter.Entry()
entry1.grid(column=1, row=1, columnspan=2, sticky="EW")
entry1.focus()
# ---------- Username ---------- #
label2 = tkinter.Label(text="Email / Username:", bg="white")
label2.grid(column=0, row=2)
entry2 = tkinter.Entry()
entry2.grid(column=1, row=2, columnspan=2, sticky="EW")
entry2.insert(0, "@gmail.com")
# ---------- Password ---------- #
label3 = tkinter.Label(text="Password:", bg="white")
label3.grid(column=0, row=3)
entry3 = tkinter.Entry()
entry3.grid(column=1, row=3, sticky="EW")
button1 = tkinter.Button(text="Generate Password", command=generate_password)
button1.grid(column=2, row=3, sticky="EW")
# ---------- Add Button ---------- #
button2 = tkinter.Button(text="Add", command=save_to_file)
button2.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
