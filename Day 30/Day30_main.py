# Day 30 Project - Improved Password Manager

import tkinter
from tkinter import messagebox
from PasswordGenerator import generated_password
import json


def save_to_file():
    """Adds the entry data to a JSON file and clears the current inputs from the GUI"""
    website = entry1.get().title()
    username = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

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
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    # Test to see if website already exists in file
                    if website in data:
                        update = messagebox.askyesno(title="Warning", message=f"Details already exist for {website}\n"
                                                                              f"Do you want to overwrite?")
                        if update:
                            pass
                        else:
                            return
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry2.insert(0, '@gmail.com')
        entry3.delete(0, 'end')


def generate_password():
    """Generates a password of random letters, numbers and characters"""
    entry3.delete(0, 'end')
    gpw = generated_password
    entry3.insert(0, gpw)
    pass


def find_details():
    """Finds the username and password for a given website, based on the saved JSON data"""
    ws_to_find = entry1.get().title()
    try:
        with open("data.json", "r") as file:
            found_data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No data file found")
    else:
        if ws_to_find in found_data:
            found_username = found_data[ws_to_find].get("username")
            found_password = found_data[ws_to_find].get("password")
            messagebox.showinfo(title="Retrieved Details", message=f"Username: {found_username}\n"
                                                                   f"Password: {found_password}")
        else:
            messagebox.showwarning(title="Warning", message="No details were found for that website")


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
entry1.grid(column=1, row=1, sticky="EW")
# Cursor in this field by default
entry1.focus()
button3 = tkinter.Button(text="Search", command=find_details)
button3.grid(column=2, row=1, sticky="EW")
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
button2 = tkinter.Button(text="Add", command=save_to_file, fg="white", bg="firebrick")
button2.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
