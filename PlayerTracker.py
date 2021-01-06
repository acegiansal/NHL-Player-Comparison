import tkinter as tk
from tkinter import ttk
from PlayerStatTracker import *

sel_player_names = []
current_select_players = []
final_players = []
testInt = 0

def _clear_frame (frame) :
    _list = frame.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    for item in _list:
        item.pack_forget()


def display_players(resultPanel):
    global sel_player_names, current_select_players
    _clear_frame(resultPanel)
    players = { # Place holder for function that finds the resulting players names and IDs
        'quantity': 2, 
        'names': ['Mika Zibanejad', 'Zdeno Chara'],
        'ID': ['1', '2']
    }  
    sel_player_names = players['names']
    if players['quantity'] == 0:
        error_label = tk.Label(resultPanel, text="No players Found!!!")
        error_label.grid(row=0, column=0, sticky = 'nesw')
    else:
        for i in range(players['quantity']):
            current_select_players.append(tk.IntVar())
            player_info = players['names'][i]
            ply_check = tk.Checkbutton(resultPanel, text=player_info, width = 30, variable=current_select_players[i])
            ply_check.grid(row=i, column=0, sticky = 'w')
        accept_button = tk.Button(
            resultPanel, 
            text='Accept',  
            padx=5, pady=5, 
            command=lambda: add_players(current_select_players)
        )
        accept_button.grid(row=players['quantity'], column=0, sticky = 'w')

# adds the players selected to the list of all players selected (if the player
# is not already on the list) and proceeds to search for the stats of the player
def add_players(selected):
    for i in range(len(selected)):
        if selected[i].get() and (final_players.count(sel_player_names[i])==0) and len(final_players)<=3:
            final_players.append(sel_player_names[i])
            # Run stat finding script with parameters of selected players

    print(final_players)

# Creating Root Window
root_window = tk.Tk()
root_window.configure(bg='pink')
root_window.title("NHL Player Tracker")
root_window.geometry("500x500")

tab_control = ttk.Notebook(root_window)

# Adds Search (1st) tab
search_tab = ttk.Frame(tab_control)
tab_control.add(search_tab, text='Search')

srch_inp_frm = tk.Frame(master=search_tab)
player_entry = tk.Entry(master= srch_inp_frm, width='50')
search_button = tk.Button(
    master=srch_inp_frm, 
    text='SUBMIT', 
    command=lambda: display_players(srch_res_frm)
)
player_entry.grid(row=0, column=0, padx=5, pady=5)
search_button.grid(row=0, column=1, padx=5, pady=5)
srch_inp_frm.pack(fill='both')

srch_res_frm = tk.Frame(master=search_tab, bg= 'white', height=200, relief=tk.SUNKEN, borderwidth=2)
#srch_res_frm.pack_propagate(False)
srch_res_frm.pack(fill='both')

tab_control.pack(fill='both')

# Running main window
root_window.mainloop()