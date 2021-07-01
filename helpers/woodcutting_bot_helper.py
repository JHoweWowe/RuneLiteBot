# Required dependencies
from time import sleep              # Async-await
import pyautogui                    # Automated tools - Pixel matching not supported in this version
import pygetwindow as gw            # Simplified version for win32gui library
from PIL import ImageGrab    # Image dev tools
import random
from helpers import helper

def confirmTree(screen_x,screen_y):

    OSRSWindow = gw.getWindowsWithTitle('RuneLite')[0]

    x = OSRSWindow.topleft[0]
    y = OSRSWindow.topleft[1]
    width = OSRSWindow.width
    height = OSRSWindow.height # Values to be passed as arguments; used for debugging only

    pyautogui.moveTo(screen_x,screen_y)
    img = ImageGrab.grab(bbox=(x,y,width,height))

    cyan_color = (0,200,200)

    # Coordinates may slightly differ
    for y_coord in range(41,43,1):
        for x_coord in range(105,112,1):
            pixel_color = img.getpixel((x_coord,y_coord))
            print('At x ' + str(x_coord) + ' and at y ' + str(y_coord) + ' color: ' + str(pixel_color))
            if (helper.is_similar(pixel_color, cyan_color, 20)):
                return True

    return False

def findRandomTreeAlgorithm():

    OSRSWindow = gw.getWindowsWithTitle('RuneLite')[0]

    x = OSRSWindow.topleft[0]
    y = OSRSWindow.topleft[1]
    width = OSRSWindow.width
    height = OSRSWindow.height # Values to be passed as arguments; used for debugging only

    img = ImageGrab.grab(bbox=(x,y,width,height)) # Doesn't save image produced

    # Sample list of color tuples with form of RGB 
    tree_trunk_colors = [(74,50,23),(91,61,28),(94,64,29),(93,63,29)]

    inventory_size = {'x': 320, 'y': 422} # Inventory size by default should remain same

    for i in range(0,1000,1):
        random_x = random.randrange(0, img.width - inventory_size['x'] - 1) # Ignore detection of inventory logs
        random_y = random.randrange(0, img.height - inventory_size['y'] - 1) # This ultimately reduces search space
        #print(str(random_x) + ',' + str(random_y))

        sample_color = img.getpixel((random_x,random_y))

        if (sample_color in tree_trunk_colors):
            screen_x = random_x + x
            screen_y = random_y + y

            img = ImageGrab.grab(bbox=(x,y,width,height))
            if (confirmTree(screen_x,screen_y)):
                print('Confirmed tree at following coords: ' + str(screen_x) + ',' + str(screen_y) + ' and its color value is ' + str(sample_color))
                print('The tree has not been cut down yet! Cutting down the tree...')
                return { "x": screen_x, "y": screen_y }
            else:
                print('Unconfirmed tree at following coords: ' + str(screen_x) + ',' + str(screen_y) + ' color ' + str(sample_color))

    return False

# Additional feature to add additional waiting time
def dropLogs():

    OSRSWindow = gw.getWindowsWithTitle('RuneLite')[0]

    inventory_x = OSRSWindow.bottomright[0] - 285
    inventory_y = OSRSWindow.bottomright[1] - 350

    logs_color = [(93,63,29)] # Can be refactored

    times = 0
    while (times < 4):

        pyautogui.moveTo(inventory_x,inventory_y)
        pyautogui.rightClick()
        pyautogui.moveTo(inventory_x,inventory_y + 48)
        pyautogui.leftClick()

        if (times < 3):
            inventory_x = inventory_x + 52 # Movement a bit high
            sleep(0.5)

        times = times + 1

# This function can technically be classified in another class for future development
def rotateCamera():
    pyautogui.keyDown("right")
    sleep(1)
    pyautogui.keyUp("right")
