import pyautogui
import time

time.sleep(3)

def mesaj():
    pyautogui.write("Girilecek Mesaj")
    pyautogui.press('enter')

while True:
        mesaj()
        time.sleep(0)

