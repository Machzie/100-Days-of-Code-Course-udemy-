# Day 27 Project - Unit Converter

import tkinter


def calculate_value():
    calc_val = 0
    if radio_state.get() == 1:
        calc_val = float(entry.get()) * 1.609
    elif radio_state.get() == 2:
        calc_val = float(entry.get()) * (9/5) + 32
    num_dp = spinbox.get()
    calc_val_str = f"{calc_val:.{num_dp}f}"
    label4.config(text=calc_val_str)


window = tkinter.Tk()
window.title("Unit Converter")
window.config(padx=10, pady=10)

label1 = tkinter.Label()
label1.grid(column=2, row=0)
label2 = tkinter.Label(text="is equal to ")
label2.grid(column=0, row=1)
label3 = tkinter.Label()
label3.grid(column=2, row=1)
label4 = tkinter.Label(text="0")
label4.grid(column=1, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

button = tkinter.Button(text="Calculate", command=calculate_value)
button.grid(column=1, row=2)

label5 = tkinter.Label(text="Num. of dec. places: ")
label5.grid(column=0, row=3)
spinbox = tkinter.Spinbox(from_=0, to=5)
spinbox.grid(column=1, row=3)


def update_labels():
    if radio_state.get() == 1:
        label1.config(text="miles")
        label3.config(text="km")
    elif radio_state.get() == 2:
        label1.config(text="celcius")
        label3.config(text="farenheit")


radio_state = tkinter.IntVar()
mkm_radiobutton = tkinter.Radiobutton(text="miles / km", value=1, variable=radio_state, command=update_labels)
mkm_radiobutton.grid(column=1, row=4)
mkm_radiobutton.config()
celfar_radiobutton = tkinter.Radiobutton(text="celcius / farenheit", value=2, variable=radio_state, command=update_labels)
celfar_radiobutton.grid(column=1, row=5)

window.mainloop()
