from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()

class Brasilia:
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
        login.send_keys('') #Add your e-mail
        password.clear()
        password.send_keys('') #Add your password
        entrar.click()

    def filter(self):
        siteSelect = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        HospBrasilia = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[@id='select2-sites-results']//li[contains(text(),'Hospital Brasília')]")))
        HospBrasilia.click()

    def run(self):
        self.login()
        self.filter()


class HospMatBrasilia:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://g5.oxyn.com.br/deviation')

    def filter(self):
        siteSelect = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        HospBrasilia = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//ul[@id='select2-sites-results']//li[contains(text(),'Hospital Maternidade Brasília')]")))
        HospBrasilia.click()

    def run(self):
        self.access()
        self.filter()

class SetupTela8:
    def __init__(self):
        self.BR = Brasilia()
        self.HMB = HospMatBrasilia()

    def NewTab(self, i):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])

    def MaxScreen(self):
        driver.maximize_window()

    def run(self):
        for i in range (2):
            if i == 0:
                self.BR.run()
            else:
                self.NewTab(i)
                self.HMB.run()

ST8 = SetupTela8()
ST8.run()
