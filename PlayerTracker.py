import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PlayerStatTracker import *

sel_basic_info = {}
current_select_players = []
final_player_info = {
    'quantity': 0, 
    'names': [], 
    'id': [],
    'team': [],
    'number': []
    }


def _clear_frame (frame) :
    _list = frame.winfo_children()
    print("Clearing frame")

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    for item in _list:
        item.destroy()


def display_players(resultPanel, name: str):
    global sel_basic_info, cucurrent_select_players
    _clear_frame(resultPanel)
    # Uses API to find player
    players = find_player(name)
    sel_basic_info = players
    current_select_players=[]

    if players['quantity'] == 0:
        error_label = tk.Label(resultPanel, text="No players Found!!!")
        error_label.grid(row=0, column=0, sticky = 'nesw')
    else:
        for i in range(players['quantity']):
            current_select_players.append(tk.IntVar())
            player_info = players['names'][i] + f"\n{players['team'][i]} #{players['number'][i]}"
            ply_check = tk.Checkbutton(resultPanel, text=player_info, variable=current_select_players[i])
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
    global final_player_info
    for i in range(len(selected)):
        if selected[i].get() and (final_player_info['id'].count(sel_basic_info['id'][i])==0) and final_player_info['quantity']<=3:
            print("Adding player!")
            final_player_info['quantity']+=1
            for key in sel_basic_info:
                if type(sel_basic_info[key])==int:
                    continue
                else:
                    final_player_info[key].append(sel_basic_info[key][i])
    display_selected_players()

def display_selected_players():
    _clear_frame(sel_frm)
    sel_label = tk.Label(master=sel_frm, text="Selected Players:", font=('Helvetica', 14, 'bold'))
    sel_label.pack(fill='both')
    for i in range(len(final_player_info['names'])):
        print("Printing player")
        playerString = final_player_info['names'][i] + f"\n{final_player_info['team'][i]} #{final_player_info['number'][i]}"
        player_label = tk.Label(master=sel_frm, text=playerString)
        player_label.pack(fill='both')

def find_stats():
    messagebox.showerror("Invalid Input", "Invalid Year")

# Creating Root Window
root_window = tk.Tk()
root_window.configure(bg='pink')
root_window.title("NHL Player Tracker")
#root_window.geometry("500x500")

tab_control = ttk.Notebook(root_window)

########## Adds Search (1st) tab
search_tab = ttk.Frame(tab_control, borderwidth=3)
tab_control.add(search_tab, text='Search')

# Input Frame
srch_inp_frm = tk.Frame(master=search_tab)
player_entry = tk.Entry(master= srch_inp_frm, width=40)
search_button = tk.Button(
    master=srch_inp_frm, 
    text='Search', 
    command=lambda: display_players(result_frm, player_entry.get())
)
player_entry.grid(row=0, column=0, padx=5, pady=5)
search_button.grid(row=0, column=1, padx=5, pady=5)
srch_inp_frm.pack(fill='both')

# Search Result frame
srch_res_frm = tk.Frame(master=search_tab, bg= 'pink', relief=tk.SUNKEN, borderwidth=2)
srch_res_frm.pack(fill='both')
srch_res_frm.columnconfigure(0, weight=1, minsize=100)
srch_res_frm.columnconfigure(1, weight=1, minsize=100)
srch_res_frm.rowconfigure(0, weight=1, minsize=150)

# Already selected players Frame
result_frm = tk.Frame(master=srch_res_frm, relief=tk.GROOVE, borderwidth=3)
result_frm.grid(row=0, column=0, sticky='nesw')
sel_frm = tk.Frame(master=srch_res_frm, relief=tk.GROOVE, borderwidth=3)
sel_label = tk.Label(master=sel_frm, text="Selected Players:", font=('Helvetica', 14, 'bold'))
sel_label.pack(fill='both')
sel_frm.grid(row=0, column=1, sticky='new')

# Season select frame
season_frm = tk.Frame(master=srch_res_frm, borderwidth = 2, relief=tk.GROOVE)
season_frm.grid(row=1, column=0, columnspan=2, sticky='nesw')
season_label = tk.Label(master=season_frm, text='Season:')
season_label.grid(row=0, column=0, sticky='nes', padx=3, pady=3)
season_entry = tk.Entry(master=season_frm, width = 20)
season_entry.insert(0, "2020/2021")
season_entry.grid(row=0,column=1, sticky='w')
season_but = tk.Button(master=season_frm, text='Find Stats!', command=find_stats)
season_but.grid(row=0,column=2, sticky='nesw')

######### END OF SEARCH TAB ##########
######### START OF ABOUT TAB #########
about_tab = ttk.Frame(tab_control, borderwidth=3)
tab_control.add(about_tab, text='About')
about_label = tk.Label(master=about_tab, text="Made by:\nGiancarlo Salvador and Carmen Lamprecht")
about_label.pack(fill='both')

tab_control.pack(fill='both')


# Running main window
root_window.mainloop()