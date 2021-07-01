# OSBSBotPy
This is adapted for RuneLite client. 
Client runs script while OSRS window is left alone.

This is done for educational purposes. I do not condone cheating in-game.
I simply wanted to improve my Python skills, and apply it to a game I used to love growing up as a kid.

## Installation Requirements
This program is only supported for Windows OS.

On your favorite terminal (Command Prompt):
Python 3.9.5 - Python3 by default should have `pip` already installed.
`pip install pyautogui`
`pip install pygetwindow`
`pip install Pillow`

## How it Works
This is currently a woodcutting bot - this is perfect for someone whose level is between 1-30 for cutting regular and oak trees.

1. Login to RuneLite
2. Your Game client layout should be: `Resizable - Classic Layout`
3. Your inventory should be open. Weapons should be at bottom of inventory.

Your RuneLite client can be either in fullscreen or windowed.

Note: Don't expand the RuneLite sidebar. 
My algorithm doesn't yet use Computer Vision technology, I don't have time to implement such as of now.

Start your favorite console and type: `py main.py`

## Tested Settings
- Windows 10, Python 3.9.5, 

## Dependencies Required
- Python3
- PyAutoGui and PyGetWindow
- Pillow for Image Capture

## Implementation of Future Libraries
- OpenCV-Python
- Win32Gui

## TODO Features for Version 1:
- [x] Improve findRandomTree() algorithm where bot may accidently mistake a log for a tree
    - Implemented confirmTree() algorithm
    - Pixel color detection for finding tree outside of inventory - this approach speeds up algorithm slightly 
- [x] Create Python script for additional support
- [x] Create time variable if user isn't able to detect tree within max number of attempts
- [ ] Make dropLogs() algorithm more advanced
- [ ] Refactor code and design!
- [ ] OSRS main client support?

## Rough RoadMap for OSRSBot
Phase 1: Color botting
Phase 2: Implementing more advanced algorithm
    - [ ] Avoid obstacles

## Q&A