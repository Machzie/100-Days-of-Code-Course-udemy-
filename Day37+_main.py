# Day 37 Project - Habit Tracker
import requests
import webbrowser
import tkinter
from tkcalendar import Calendar
import Day37_config


def fetch_date():
    date = cal.selection_get().strftime("%Y%m%d")
    return date


def add_pixel():
    post_params = {
        "date": fetch_date(),
        "quantity": entry1.get()
    }
    add_response = requests.post(url=f"{Day37_config.pixela_endpoint}/cyclegraph2", json=post_params, headers=header)
    print(add_response.text)


def update_pixel():
    update_params = {
        "quantity": entry1.get()
    }
    update_response = requests.put(url=f"{Day37_config.pixela_endpoint}/cyclegraph2/{fetch_date()}", json=update_params, headers=header)
    print(update_response.text)


def del_pixel():
    del_response = requests.delete(url=f"{Day37_config.pixela_endpoint}/cyclegraph2/{fetch_date()}", headers=header)
    print(del_response.text)


def open_browser():
    webbrowser.open(f"{Day37_config.pixela_endpoint}/cyclegraph2.html")


header = {
    "X-USER-TOKEN": Day37_config.TOKEN
}

window = tkinter.Tk()
window.title("Distance Cycled")

cal = Calendar()
cal.grid(column=0, columnspan=3, row=0, sticky="EW", padx=20, pady=20)
label1 = tkinter.Label(text="Value: ")
label1.grid(column=1, row=1, sticky="e")
entry1 = tkinter.Entry(width=10)
entry1.grid(column=2, row=1, sticky="w")
add_button = tkinter.Button(text="Add", command=add_pixel)
add_button.grid(column=0, row=2, sticky="EW", pady=10)
update_button = tkinter.Button(text="Update", command=update_pixel)
update_button.grid(column=1, row=2, sticky="EW", pady=10)
del_button = tkinter.Button(text="Delete", command=del_pixel)
del_button.grid(column=2, row=2, sticky="EW", pady=10)
open_button = tkinter.Button(text="Open\nGraph", command=open_browser)
open_button.grid(column=1, row=3, sticky="EW", pady=10)

window.mainloop()
