import pyautogui, time

class ScreenPosition():
    def __init__(self):
         pass

    def EnableExtension(self):
        pyautogui.click(x=1802, y=51, duration=2.0)  # Enable chrome extension


    def MoveTo4(self):
        self.EnableExtension()
        pyautogui.moveTo(x=1755, y=15, duration=1.0)  # Select windows bar near minimize button
        pyautogui.dragTo(x=4800, y=540, duration=4.0)  # Take window until middle of screen number 4
        time.sleep(2)


    def MoveTo6(self):
        self.EnableExtension()
        pyautogui.moveTo(x=1755, y=15, duration=1.0)  # Select windows bar near minimize button
        pyautogui.dragTo(x=2880, y=1085, duration=4.0)  # Take window until middle of screen number 6
        time.sleep(2)


    def MoveTo7(self):
        pyautogui.moveTo(x=1755, y=15, duration=1.0)  # Select windows bar near minimize button
        pyautogui.dragTo(x=6720, y=1085, duration=4.0)  # Take window until middle of screen number 7
        time.sleep(2)


    def MoveTo8(self):
        self.EnableExtension()
        pyautogui.moveTo(x=1755, y=15, duration=1.0)  # Select windows bar near minimize button
        pyautogui.dragTo(x=6720, y=540, duration=4.0)  # Take window until middle of screen number 8
        time.sleep(2)


