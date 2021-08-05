# NHL-Player-Comparison
A small Python API learning project created by Giancarlo Salvador (https://github.com/acegiansal)

## Synopsis
This is an application that allows for up to 3 NHL players to be selected and comparing their basic stats in another panel. The application uses the undocumented (at least officially) NHL REST API to retrieve all the data, from player names and positions to the amount of penalty minutes they received for a specific year.

## How to Use it
Up to 3 players may be selected using the search bar that appears at the top of the small python frame once the program has commenced. Make sure that the name is spelled correctly (capitalized letters are fine) and a script will run that searches all of the NHL for the player selected. It is important to note that the program searches the entire NHL even if the player has already been found. This is by design, as some players may have the same name (Sebastian Aho and Sebastion Aho). Thus it may take some time for the player to be found and the UI to display the player. Once the 3 players have been selected, enter the desired season at the bottom and press 'Find Stats!'. The stats will be found on the 'stats' page that can be accessed by pressing the 'stats' tab at the top of the frame.

## The NHL REST API
The free NHL REST API does not contain any official documenation from the NHL, however there is some documentation found online here: [NHL API DOCUMENTATION](https://gitlab.com/dword4/nhlapi). When the Python script receives the information from the API, it returns it in the form of lists and dictionaries which were in turn used to gather the data used in this application.