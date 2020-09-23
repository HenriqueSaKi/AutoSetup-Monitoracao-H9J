import pyautogui

class ScreenPosition():
    def __init__(self):
         pass

    def EnableExtension(self):
        pyautogui.click(x=1802, y=51, duration=2.0)  # Enable chrome extension


    def moveUntil(self, screen):
        if screen == 4:
            pyautogui.moveTo(x=1755, y=15, duration=1.0)
            pyautogui.dragTo(x=4800, y=100, duration=3.0)

        if screen == 6:
            pyautogui.moveTo(x=1755, y=15, duration=1.0)
            pyautogui.dragTo(x=4800, y=1620, duration=3.0)

        if screen == 7:
            pyautogui.moveTo(x=1755, y=15, duration=1.0)
            pyautogui.dragTo(x=6720, y=1620, duration=3.0)

        if screen == 8:
            pyautogui.moveTo(x=1755, y=15, duration=1.0)
            pyautogui.dragTo(x=6720, y=100, duration=3.0)
