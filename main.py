# Required dependencies
from time import sleep              # Async-await
import pyautogui                    # Automated tools - Pixel matching not supported in this version
import pygetwindow as gw            # Simplified version for win32gui library

# Helpers
from helpers import woodcutting_bot_helper

# Should be renamed to __init__?
def setup():
    while (True):
        print('Please press a number between 1 and 2, and then press Enter on your keyboard')
        print('1 - Woodcutting Bot')
        print('2 - Surprise')
        x = input()
        if (x == '1'):
            print('Type the number of attempts (between 1 to 1000) the bot should try to find a valid tree')
            print('A good number is between 10-20')
            y = input()
            try:
                new_y = int(y)
                if (new_y >= 1 and new_y <= 1000): 
                    onInit(new_y)
                else:
                    print('Please enter an integer between 1 to 1000')
            except ValueError:
                print('Please enter a valid integer')

        elif (x == '2'):
            print('You fool, press one')
            onInitTest()
            break
        else:
            print('Try a different number')

def onInit(attempts):

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

        sleep(15.000) # Additional time waited
        woodcutting_bot_helper.dropLogs()



def onInitTest():
    print('You got trolled lmao')

# Execution LEGOOO
setup()