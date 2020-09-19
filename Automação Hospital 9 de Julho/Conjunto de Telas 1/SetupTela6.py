from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx') #Add extension downloaded in format .crx
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #Install chrome driver and apply options
driver.maximize_window() #maximize window

class SetupTela6:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://americaenergia.powerhub.io/america-energia/usuarios/criar')

    def accessIframe(self):
        driver.switch_to.parent_frame()

    def login(self):
        self.accessIframe()
        login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        login.click()
        login.clear()
        login.send_keys('') #Input a valid e-mail address
        time.sleep(2)
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.click()
        password.clear()
        password.send_keys('') #Input you password
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def dashboard(self):
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//div[@role='menu']//a[2]")))
        dashboard = driver.find_element_by_xpath("//div[@role='menu']//span[contains(text(), 'Dashboard')]")
        dashboard.click()

    def DashboarConsumo(self):
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//header[@class='header--1G8Mj']//h4[@title='Consumo']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='viewPanel--1AH2Z']//div[8]//header//div[@class='toolbar--2pvXp']//button//span[@class='fa fa-download ']")))
        maxDash = driver.find_element_by_xpath("//div[@class='viewPanel--1AH2Z']//div[8]//header//div[@class='toolbar--2pvXp']//button//span[@class='fa fa-window-maximize ']")
        maxDash.click()
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='shortcuts--3iDvL']")))
        anoAtual = driver.find_element_by_xpath("//div[@class='shortcuts--3iDvL']//div[5]")
        anoAtual.click()

    def NewTab(self):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

    def run(self):
        for i in range (2):
            if i == 0:
                self.access()
                self.login()
                self.dashboard()
            elif i == 1:
                self.NewTab()
                self.access()
                self.dashboard()
                self.DashboarConsumo()
        driver.switch_to.default_content()

ST6 = SetupTela6()
ST6.run()