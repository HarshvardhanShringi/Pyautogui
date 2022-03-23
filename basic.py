import pyautogui
import time
#1920,1080

# for move
pyautogui.moveTo(200, 350, duration=1)

# for drag
pyautogui.dragTo(200, 200, duration=1)

# for click
pyautogui.click(x=200, y=350, clicks=2, interval=0, button='left')

# size of our screen
print(pyautogui.size())

# print position of mouse
print(pyautogui.position())

# time delay (n) for n seconds
time.sleep(3)

# for scrolling
pyautogui.scroll(50)



#program

# Part 1- Opening 'view all'
pyautogui.moveTo(671, 130, duration=0.5)
pyautogui.scroll(-650)
pyautogui.moveTo(672, 591, duration=0.5)
pyautogui.click(x=672, y=591, clicks=1, interval=0, button='left')

# Part 2- Opening shop 1
pyautogui.moveTo(81,355,duration=1)
time.sleep(3)
pyautogui.click(x=81, y=355, clicks=1, interval=0, button='left')












