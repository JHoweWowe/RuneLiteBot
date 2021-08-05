# Installed default dependencies
from configparser import ConfigParser   # Handles configuration file settings
from time import sleep                  # Async-await

# Required dependencies
import pyautogui                        # Automated tools - Pixel matching not supported in this version
import pygetwindow as gw                # Simplified version for win32gui library

# Helpers
from helpers import woodcutting_bot_helper

class Main:

    def setup(self):
        parser = ConfigParser()
        parser.read('dev.ini')

        selectionOne = parser.get('settings','bot_type',fallback='none')
        selectionTwo = parser.getint('settings','woodcutting_find_tree_attempts',fallback=20)
        selectionThree = parser.getint('settings','chop_and_drop_time_seconds',fallback=15)
        if (selectionOne == 'woodcutting'):
            if (selectionTwo >= 1 and selectionTwo <= 1000):
                self.onInit(selectionTwo,selectionThree)
            else:
                print('Please make sure woodcutting_find_tree_attempts is between 1 to 1000')
                exit()
        elif (selectionOne == 'surprise'):
            self.onInitTest()
        else:
            print('Please check your configuration file again!')
            exit()

    def onInit(self,attempts,timeSeconds):

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

    def onInitTest(self):
        print('You got trolled lmao')

# Main Class Execution
main = Main()
main.setup()