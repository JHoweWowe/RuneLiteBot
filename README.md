# RuneLiteBot
Disclaimer: I do not condone cheating. I simply wanted to improve my Python skills, 
and apply my software development knowledge to a game I used to love growing up as a kid.


## Description
Programmed in Python and used in many desktop applications, I decided to create a bot script for the RuneLite client in Old School Runescape without the user having to control the mouse and keyboard to level up the user's woodcutting skill. More functionality to be added soon.


## Installation Requirements
Only supported for Windows OS. First Google and download Python 3.9.5.

Once installed, go to your favorite terminal (Command Prompt):
Python 3.9.5 - Python3 by default should have `pip` already installed.
`pip install pyautogui`
`pip install pygetwindow`
`pip install Pillow`

The following libraries install PyAutoGui, PyGetWindow, and Pillow (Image Capture) respectively.


## How it Works
This is currently a woodcutting bot - perfect for someone whose level is between 1-30 for cutting regular and oak trees.

1. Login to RuneLite (Make sure your game window is not fullscreen)
2. Your Game client layout should be: `Resizable - Classic Layout`
3. Your top 4 slots in your inventory should be free. Weapons should be at bottom of inventory.

Make sure your brightness level is set at 2nd knotch.
The following screenshot will display the optimal settings.

Please refer to the following screenshots below for Settings and Inventory.

![Display Settings](/images/DisplaySettings.png) ![Inventory](/images/Inventory.png)

Note: Don't expand the RuneLite sidebar. 

Once Python and its required libraries are installed, start your favorite console and type: `py main.py`

Changing the Settings for running the script is easy. Refer to the `dev.ini` file.


## Development Settings
Please refer to the following file `dev.ini`
drop_number_of_logs_per_cycle value should between 1 - 4 to follow algorithm cycle


## Tested Settings
- Windows 10, Python 3.9.5, 
- Screen Resolution: 1920 x 1080
Only supported with 100% scaling for Windows.


## Known Bugs:
- [ ] When screen size is classic and too small, program doesn't execute likely due to failure of image capture attempting to find a random tree algorithm


## Resources
https://realpython.com/python-gui-tkinter/
https://docs.python.org/3/library/configparser.html