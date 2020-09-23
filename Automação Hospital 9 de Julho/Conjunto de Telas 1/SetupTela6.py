from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()

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
        login.send_keys('') #Add your e-mail
        time.sleep(2)
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.click()
        password.clear()
        password.send_keys('') #Add your password
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def dashboard(self):
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//div[@role='menu']//a[2]")))
        dashboard = driver.find_element_by_xpath("//div[@role='menu']//span[contains(text(), 'Dashboard')]")
        dashboard.click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header[@class='header--1G8Mj']//h4[@title='Consumo']")))

    def DashboarConsumo(self):
        #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='viewPanel--1AH2Z']//div[8]//header//div[@class='toolbar--2pvXp']//button//span[@class='fa fa-download ']")))
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//canvas[1]")))
        time.sleep(5)
        maxDash = driver.find_element_by_xpath("//div[@class='viewPanel--1AH2Z']//div[8]//header//div[@class='toolbar--2pvXp']//button//span[@class='fa fa-window-maximize ']")
        maxDash.click()
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='shortcuts--3iDvL']")))
        anoAtual = driver.find_element_by_xpath("//div[@class='shortcuts--3iDvL']//div[5]")
        anoAtual.click()

    def NewTab(self):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://americaenergia.powerhub.io/america-energia/sites')

    def MaxScreen(self):
        driver.maximize_window()

    def run(self):
        for i in range (2):
            if i == 0:
                self.access()
                self.login()
                self.dashboard()
                time.sleep(4)
            elif i == 1:
                self.NewTab()
                self.dashboard()
                self.DashboarConsumo()
        driver.switch_to.default_content()


ST6 = SetupTela6()
ST6.run()
