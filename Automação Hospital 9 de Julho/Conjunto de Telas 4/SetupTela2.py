from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx') #Add extension downloaded in format .crx
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #Install chrome driver and apply options
driver.maximize_window() #maximize window
action = ActionChains(driver)

class SetupTela2:
    def __init__(self):
        pass

    def AccessG5(self):
        driver.get('https://g5.oxyn.com.br/')

    def DeviationAccess(self):
        driver.get('https://g5.oxyn.com.br/deviation')

    def loginG5(self):
        login = driver.find_element_by_id('user_email')
        password = driver.find_element_by_id('user_senha')
        entrar = driver.find_element_by_xpath('//button[@type="submit"]')
        login.clear()
        login.send_keys('')  # Input a valid e-mail address
        password.clear()
        password.send_keys('')  # Input you password
        entrar.click()

    def AccessNetvMi(self):
        driver.get('http://netvmi.com.br/')
        driver.find_element_by_xpath("//div[@class='menu-main-container']//ul[@id='menu-main']//li[@id='menu-item-49']").click()
        iframe = driver.find_element_by_xpath("//iframe")
        driver.switch_to.frame(iframe)

    def loginNetvMi(self):
        login = driver.find_element_by_xpath("//input[@id='usuario']")
        login.send_keys('')  # Input a valid e-mail address
        time.sleep(1)
        password = driver.find_element_by_xpath("//input[@id='senha']")
        password.send_keys('')  # Input you password
        time.sleep(1)
        pyautogui.press('enter')

    def NewTab(self, i):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(2)

    def LogEventos(self):
        driver.get('https://g5.oxyn.com.br/event/log')
        driver.find_element_by_xpath("//button[contains(text(),'Buscar')]").click()

    def Hosp9Julho(self):
        siteSelect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        Hosp9Julho = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='select2-sites-results']//li[contains(text(),'Hospital 9 de Julho')]")))
        Hosp9Julho.click()

    def Marcador(self):
        markButton = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='marker']//a[contains(text(),'Marcadores')]")))
        markButton.click()
        marcador = driver.find_element_by_xpath("//ul[@id='labels']//li[contains(text(),'Status de porta')]")
        filterBox = driver.find_element_by_id('filter')
        action.drag_and_drop(marcador, filterBox).perform()
        aplicar = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(), 'Aplicar')]")
        aplicar.click()

    def run(self):
        for i in range(3):
            if i == 0:
                self.AccessG5()
                self.loginG5()
                self.LogEventos()
            elif i == 1:
                self.NewTab(i)
                self.DeviationAccess()
                self.Hosp9Julho()
                self.Marcador()
            else:
                self.NewTab(i)
                self.AccessNetvMi()
                self.loginNetvMi()
                driver.switch_to.default_content()

ST2 = SetupTela2()
ST2.run()
