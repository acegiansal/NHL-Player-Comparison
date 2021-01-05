import tkinter as tk
from tkinter import ttk

input_list = [
    "First Name:", 
    "Last Name:", 
    "Address Line 1:", 
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:"
]
label_list = []
entry_list = []

window = tk.Tk()
window.configure(bg='pink')
window.title("TEST for ENTRY")

input_frame = tk.Frame(relief=tk.SUNKEN, borderwidth = 4)
counter = 0

for text_label in input_list:
    label = tk.Label(master=input_frame, text = text_label)
    label_list.append(label)
    entry = tk.Entry(master=input_frame, width=50)
    entry_list.append(entry)

    label.grid(row=counter, column=0, sticky="e")
    entry.grid(row=counter, column =1)
    counter += 1

input_frame.pack()

button_frame = tk.Frame(borderwidth = 4)
clear_button = tk.Button(master= button_frame, text="Clear")
clear_button.pack(side=tk.RIGHT, ipadx=10)
sub_button = tk.Button(master=button_frame, text="Submit")
sub_button.pack(side=tk.RIGHT, padx=10, ipadx=10)
button_frame.pack(fill=tk.X, ipadx=5, ipady=5)



window.mainloop()