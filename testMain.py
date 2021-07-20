## This is the executable file with (somewhat poor) UI Support

# Installed default dependencies
from functools import partial
import tkinter as tk
from tkinter import IntVar, StringVar, Text, ttk                 # Used for creating GUI application
from configparser import ConfigParser   # Handles configuration file settings
from time import sleep                  # Async-await

# Required dependencies
import pyautogui                        # Automated tools - Pixel matching not supported in this version
import pygetwindow as gw                # Simplified version for win32gui library

# Helpers
from helpers import woodcutting_bot_helper

def setupApp():
    # Load and Read Existing Settings
    parser = ConfigParser()
    parser.read('dev.ini')

    selectionOne = parser.get('settings','bot_type',fallback='none')
    selectionTwo = parser.getint('settings','woodcutting_find_tree_attempts',fallback=0)
    selectionThree = parser.getint('settings','chop_and_drop_time_seconds',fallback=15)

    # Create RuneLiteBot Application Window
    window = tk.Tk()
    window.geometry('480x320')

    # Create Labels
    ttk.Label(window, text="OSRS RuneLite Bot",
    font = ("Times New Roman", 12)).grid(column=0,row=0)
    ttk.Label(window, text="Select the Bot Type: ",
        font = ("Times New Roman", 12)).grid(column=0,row=1)
    ttk.Label(window, text="Woodcutting: Find Tree Attempts",
        font = ("Times New Roman", 12)).grid(column=0,row=3)
    ttk.Label(window, text="Woodcutting: Chop and Drop Time",
        font = ("Times New Roman", 12)).grid(column=0,row=4)

    v1 = IntVar()
    e1 = ttk.Entry(window, textvariable=v1)
    v1.set(selectionTwo)
    e1.grid(column=1,row=3)

    v2 = IntVar()
    e2 = ttk.Entry(window, textvariable=v2)
    v2.set(selectionThree)
    e2.grid(column=1,row=4)

    # Combobox Creation
    n = tk.StringVar()
    bot_type_selection = ttk.Combobox(window, width=27, textvariable=n)
    # Add combobox dropdown list
    bot_type_selection['values'] = ('woodcutting','surprise','none')
    bot_type_selection.grid(column=1,row=1)
    bot_type_selection.current(0)
    
    # Basic START Button (Needs better support)
    startBtn = ttk.Button(window, text="START", command=partial(onInit,v1.get(),v2.get())).grid(column=0,row=5)
    stopBtn = ttk.Button(window, text="STOP", command=exit).grid(column=0,row=6)

    # Keep window going
    window.mainloop()


def setup():
    parser = ConfigParser()
    parser.read('dev.ini')

    selectionOne = parser.get('settings','bot_type',fallback='none')
    selectionTwo = parser.getint('settings','woodcutting_find_tree_attempts',fallback=20)
    selectionThree = parser.getint('settings','chop_and_drop_time_seconds',fallback=15)
    if (selectionOne == 'woodcutting'):
        if (selectionTwo >= 1 and selectionTwo <= 1000):
            onInit(selectionTwo,selectionThree)
        else:
            print('Please make sure woodcutting_find_tree_attempts is between 1 to 1000')
            exit()
    elif (selectionOne == 'surprise'):
        onInitTest()
    else:
        print('Please check your configuration file again!')
        exit()

def onInit(attempts,timeSeconds):

    print('The program is starting!\nPress Control+C in the console to exit the program anytime.')
    sleep(2.000)

    numberConsecutiveAttempts = 0
    maxConsecutiveNumberAttempts = int(attempts)

    while (numberConsecutiveAttempts < maxConsecutiveNumberAttempts):

        print('Player finding tree!')
        sleep(0.250)
        tree = woodcutting_bot_helper.findRandomTreeAlgorithm()

        if (not tree):
            woodcutting_bot_helper.rotateCamera()
            numberConsecutiveAttempts = numberConsecutiveAttempts + 1
            continue

        print('The tree is located at ' + str(tree['x']) + ',' + str(tree['y']))
        pyautogui.moveTo(tree['x'], tree['y'])

        numberConsecutiveAttempts = 0           # Resets to 0

        sleep(0.300) # Remove possible misclicks
        pyautogui.leftClick()

        sleep(timeSeconds) # Additional time waited
        woodcutting_bot_helper.dropLogs()

def onInitTest():
    print('You got trolled lmao')

# Application running in multiple threads doesn't quite work yet
setupApp()
# setup()