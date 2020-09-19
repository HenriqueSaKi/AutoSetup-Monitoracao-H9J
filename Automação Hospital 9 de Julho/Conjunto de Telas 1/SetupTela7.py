from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install()) #Install chrome driver
driver.maximize_window() #maximize window

class SetupTela7:
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
        HospSaoLucas = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[@id='select2-sites-results']//li[contains(text(),'Hospital São Lucas')]")))
        HospSaoLucas.click()

    def run(self):
        self.login()
        self.filter()

ST7 = SetupTela7()
ST7.run()