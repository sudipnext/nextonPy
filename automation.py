import pyautogui
from time import *
# res = pyautogui.locateOnScreen("./images/submit.png")

# print(res)

# submit_btn = pyautogui.center(res)

# pyautogui.moveTo(submit_btn)
# or
# res = pyautogui.locateCenterOnScreen("./images/submit.png")
# print(res)

# confession_new = pyautogui.prompt(text="", title="Enter the Confession")
# print(confession_new)
# pyautogui.hotkey("ctrl", "shift", "n")
# sleep(1)
# pyautogui.write(
#     "https://docs.google.com/forms/d/1WWMmAQ-szXqbt-8hdMcsKzbCgosMZl-V-Xilz0-RKh0/viewform?edit_requested=true")
# pyautogui.hotkey("enter")
# sleep(1)
# x, y = pyautogui.locateCenterOnScreen("./images/answer.png", confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

# sleep(1)
# pyautogui.write(confession_new)
# pyautogui.moveTo(res)
# pyautogui.hotkey("enter")
res = pyautogui.locateCenterOnScreen("./images/gaming.png")
print(res)
pyautogui.moveTo(res)
pyautogui.click()

pyautogui.write("./images/search.png")
