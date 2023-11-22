import pyautogui
import time

# Replace (x, y) with the coordinates of the app's icon
x, y = (293, 501)

# Move the mouse to the app's icon
pyautogui.moveTo(x, y)

# Click the app's icon
pyautogui.doubleClick()

time.sleep(20)

pyautogui.moveTo(338, 993)

pyautogui.click()



time.sleep(20)  

pyautogui.moveTo(832, 508)

pyautogui.click()