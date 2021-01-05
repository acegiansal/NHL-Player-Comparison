from urllib.request import urlopen
import requests
import tkinter as tk
from tkinter import ttk

# Creating Root Window
root_window = tk.Tk()
root_window.configure(bg='pink')
root_window.title("NHL Player Tracker")
root_window.geometry("960x540")

tab_control = ttk.Notebook(root_window)

# Adds Search (1st) tab
search_tab = ttk.Frame(tab_control)
tab_control.add(search_tab, text='Search')

srch_inp_frm = tk.Frame(master=search_tab)
player_entry = tk.Entry(master= srch_inp_frm, width='50')
search_button = tk.Button(master=srch_inp_frm, text='SUBMIT')
player_entry.grid(row=0, column=0, padx=5, pady=5)
search_button.grid(row=0, column=1, padx=5, pady=5)
srch_inp_frm.pack(fill='both')
#srch_inp_frm.grid(row=0,column=0, padx=2, pady=2)

srch_res_frm = tk.Frame(master=search_tab, bg= 'white', height=200, relief=tk.SUNKEN, borderwidth=2)
srch_res_frm.pack_propagate(False)
srch_res_frm.pack(fill='both')
#srch_res_frm.grid(row=1, column=0, padx=2, pady=2)

tab_control.pack(fill='both')


# Running main window
root_window.mainloop()