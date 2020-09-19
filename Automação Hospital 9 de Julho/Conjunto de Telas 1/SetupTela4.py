from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx') #Add extension downloaded in format .crx
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #Install chrome driver and apply options
driver.maximize_window() #maximize window
action = ActionChains(driver)

class SetupTela4:
    def __init__(self):
        pass

    def access(self):
        driver.get('https://g5.oxyn.com.br/')

    def DeviationAccess(self):
        driver.get('https://g5.oxyn.com.br/deviation')

    def login(self):
        login = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_senha')
        entrar = driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('') #Input a valid e-mail address
        password.clear()
        password.send_keys('') #Input you password
        entrar.click()

    def NewTab(self, i):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])
        self.DeviationAccess()
        time.sleep(2)

    def Hosp9Julho(self):
        siteSelect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        HospSaoLucas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='select2-sites-results']//li[contains(text(),'Hospital 9 de Julho')]")))
        HospSaoLucas.click()

    def Marcador(self):
        markButton = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='marker']//a[contains(text(),'Marcadores')]")))
        markButton.click()
        marcador = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'HD - Reservatórios')]")
        filterBox = driver.find_element_by_id('filter')
        action.drag_and_drop(marcador, filterBox).perform()
        aplicar = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(), 'Aplicar')]")
        aplicar.click()

    def run(self):
        for i in range(2):
            if i == 0:
                self.access()
                self.login()
            else:
                self.NewTab(i)
                self.Hosp9Julho()
                self.Marcador()


ST4 = SetupTela4()
ST4.run()

