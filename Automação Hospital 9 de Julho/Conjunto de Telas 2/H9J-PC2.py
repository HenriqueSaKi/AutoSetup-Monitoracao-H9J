from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time, pyautogui

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(ChromeDriverManager().install()) #Install chrome driver
driver.maximize_window() #maximize window

class SetupPC2:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://g5.oxyn.com.br/')

    def login(self):
        self.access()
        login = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_senha')
        entrar = driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('')  # Input a valid e-mail address
        password.clear()
        password.send_keys('')  # Input you password
        entrar.click()

    def filter(self):
        siteSelect = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        HospSantaPaula = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[@id='select2-sites-results']//li[contains(text(),'Hospital Santa Paula')]")))
        HospSantaPaula.click()
        
    def SendTo2nd(self):
        pyautogui.moveTo(x=930,y=15,duration=1.0) #Move until a position near minimize button
        pyautogui.dragTo(x=2040,y=540,duration=3.0) #Drag to middle of 2nd screen
        driver.maximize_window()

    def run(self):
        self.login()
        self.filter()
        self.SendTo2nd()

SP = SetupPC2()
SP.run()
