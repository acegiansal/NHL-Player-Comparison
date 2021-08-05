import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PlayerStatTracker import *
import datetime

sel_basic_info = {}
current_select_players = []
final_player_info = {
    'quantity': 0, 
    'names': [], 
    'id': [],
    'team': [],
    'number': []
    }
CURRENT_SEASON = "2020/2021"

def _clear_frame (frame) :
    """
    Clears the passed on frame of every widget while keeping
    the frame intact
    """
    _list = frame.winfo_children()
    print("Clearing entire frame")

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    for item in _list:
        item.destroy()


def display_players(resultPanel, name: str):
    """
    Searches for a specific player using the NHL REST API
    and displays the discovered players in a checkbox
    """
    global sel_basic_info, cucurrent_select_players
    _clear_frame(resultPanel)
    # Uses API to find player
    players = find_player(name)
    sel_basic_info = players
    current_select_players=[]

    if players['quantity'] == 0:
        error_label = tk.Label(resultPanel, text="No players Found!\nEnsure names are spelt correctly")
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
        if selected[i].get() and (final_player_info['id'].count(sel_basic_info['id'][i])==0) and final_player_info['quantity']<3:
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

def _find_latest_season():
    now = datetime.datetime.now()
    if now.month >= 10:
        print (f"Currnet Season: {now.month}")
        return now.year + 1
    else:
        return now.year

def find_stats(comparePanel, seasonStr: str):
    season_clean = seasonStr.replace('/','')
    if (
        not season_clean.isdecimal() or 
        len(season_clean) != 8 or
        season_clean[-4:] > str(_find_latest_season()) or
        int(season_clean[-4:]) - int(season_clean[:4]) != 1):

        messagebox.showerror("Invalid Input", "Invalid Year")
    else:
        #messagebox.showerror("It works", season_clean)
        stats = find_player_stats(final_player_info['id'], CURRENT_SEASON)
        display_stats(comparePanel, stats)

def display_stats(comparePanel, stats: dict):
    '''
    stats = {
        'quantity': 3, 
        'names': ['Thomas Chabot', 'Cale Makar', 'Quinn Hughes'],
        'age': [24, 21, 22],
        'num': ['72', '8', '43'],
        'team': ['OTT', 'COL', 'VAN'],
        'pos': ['D', 'D', 'D'],
        'gp': [71, 57, 68],
        'g': [6, 12, 8],
        'a': [33, 38, 45],
        'p': [39, 50, 53],
        'pm': [-18,12,-10],
        'pim': [42,12,22]
    }
    '''
    _clear_frame(comparePanel)
    comparePanel.rowconfigure(0, weight=1, minsize=100)

    for i in range(stats['quantity']):
        comparePanel.columnconfigure(i, weight=1, minsize=100)
        player_tab = tk.Frame(master=comparePanel, relief=tk.RIDGE, borderwidth=3)
        player_tab.grid(row=0, column=i, sticky='nesw')
        player_name = tk.Label(master=player_tab, text=f"{stats['names'][i]}\n{stats['team'][i]} #{stats['num'][i]}")
        player_name.pack(fill='both')
        for key in stats:
            if type(stats[key])==int or key == 'names' or key == 'num' or key == 'team':
                continue
            else:
                stat_frm = tk.Frame(master=player_tab)
                stat_frm.grid_columnconfigure((0,1,2), weight=1, minsize=0.5)

                stat_name = tk.Label(master=stat_frm, text=f"{key.upper()}:", font=('Helvetica', 8, 'bold'))
                stat_name.grid(row=0,column=0, sticky='w')
                stat_num = tk.Label(master=stat_frm, text=f"{stats[key][i]}", font=('Helvetica', 8))
                stat_num.grid(row=0,column=1, sticky='w')
                stat_compare = tk.Frame(master=stat_frm, bg=compare_stat(stats[key], i), width=5, height=5)
                stat_compare.grid(row=0, column=2, sticky='w')
                stat_frm.pack(fill='both')
                
        #position = tk.Label(master=player_tab, text=f"Position: {stats['pos'][i]}", )
        #position.pack(fill='both')

def compare_stat(stats: list, index: int) -> str:
    COLOUR = {'high': 'green', 'mid': 'blue', 'low': 'red'}
    for p in stats:
        if type(p) != int:
            return ('grey')
    if stats[0] == stats[1] and stats[1] == stats[2]:
        return(COLOUR['mid'])
    elif stats.count(stats[index]) > 1:
        return(COLOUR['mid'])
    elif stats[index] == max(stats):
        return(COLOUR['high'])
    elif stats[index] != max(stats) and stats[index] != min(stats):
        return(COLOUR['mid'])
    else:
        return(COLOUR['low'])

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
season_entry.insert(0, CURRENT_SEASON)
season_entry.grid(row=0,column=1, sticky='w')
season_but = tk.Button(master=season_frm, text='Find Stats!', command=lambda: find_stats(compare_tab, season_entry.get()))
season_but.grid(row=0,column=2, sticky='nesw', padx=5, pady=5)

######### END OF SEARCH TAB ##########
######### START OF COMPARISON TAB #########
compare_tab = ttk.Frame(tab_control, borderwidth=3)
tab_control.add(compare_tab, text='Compare')
comp_inst = tk.Label(master=compare_tab, text='Search for players to see their stats here')
comp_inst.pack(fill='both')

######### START OF ABOUT TAB #########
about_tab = ttk.Frame(tab_control, borderwidth=3)
tab_control.add(about_tab, text='About')

about_str = """Made by:
    Giancarlo Salvador (https://github.com/acegiansal)\n
    1/6/2021"""

about_label = tk.Label(
    master=about_tab, 
    text=about_str
    )
about_label.grid(row=0, column=0, sticky='nesw')

###### END OF ABOUT TAB

tab_control.pack(fill='both')


# Running main window
root_window.mainloop()