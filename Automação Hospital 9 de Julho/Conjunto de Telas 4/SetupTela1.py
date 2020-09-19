from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import timedelta
import datetime
import pyautogui
import time

options = Options()
options.add_extension('extension_0_71_0_0.crx') #Add extension downloaded in format .crx
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #Install chrome driver and apply options
driver.maximize_window() #maximize window
action = ActionChains(driver)

class PowerBI:
    def __init__(self):
        pass

    def AccessPwBI(self):
        driver.get('https://login.microsoftonline.com/')

    def loginPwBI(self):
        login = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        login.clear()
        login.send_keys('')  # Input a valid e-mail address
        time.sleep(2)
        avancar = driver.find_element_by_xpath("//input[@value='Avançar']") #Avançar
        avancar.click()
        senha = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']")))
        senha.clear()
        senha.send_keys('')  # Input you password
        time.sleep(2)
        action.reset_actions()
        driver.find_element_by_xpath("//input[@value='Entrar']").click() #Entrar
        driver.find_element_by_xpath("//input[@id='idBtn_Back']").click() #Não continuar conectado

    def IndicadorChamados(self):
        driver.get('https://app.powerbi.com/groups/me/reports/e5382827-0cc8-4bfc-bb06-85a7ad3d8206/ReportSection?noSignUpCheck=1')

    def PressaoLeitos(self):
        driver.get('https://app.powerbi.com/groups/me/reports/0d6cec4d-0248-4344-a698-209ca30daa55/ReportSection?noSignUpCheck=1')

    def NewTab(self, i):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])

    def run(self):
        self.AccessPwBI()
        self.loginPwBI()
        for i in range(2):
            if i == 0:
                self.IndicadorChamados()
            elif i == 1:
                self.NewTab(i)
                self.PressaoLeitos()
        self.NewTab(2)

class G5:
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

    def NewTab(self, i):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(2)

    def Hosp9Julho(self):
        siteSelect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Selecione um site")]')))
        time.sleep(5)
        siteSelect.click()
        Hosp9Julho = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='select2-sites-results']//li[contains(text(),'Hospital 9 de Julho')]")))
        Hosp9Julho.click()

    def Relatorio(self, modelo1, modelo2):
        report = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'report')))
        report.click()
        time.sleep(5)
        for i in range (2):
            reportModel = driver.find_element_by_id('select2-report-model-select2-container')
            reportModel.click()
            findModel = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
            if i == 0:
                findModel.send_keys("{}".format(modelo1))
            elif i == 1:
                findModel.send_keys("{}".format(modelo2))
            pyautogui.press('enter')
            time.sleep(1)
            self.dateCalculator()
            generator = driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']//button[contains(text(),'Gerar')]")
            generator.click()
            driver.switch_to.window(driver.window_handles[2])
        pyautogui.hotkey('ctrl', 'w')

    def maximizePDF(self):
        pyautogui.moveTo(x=1853, y=870, duration=2.0)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1.5)

    def dateCalculator(self):
        currentDate = datetime.datetime.today()
        lastMonthDate = currentDate - timedelta(days=31)
        # Initial date
        initialDateField = driver.find_element_by_id('initial-date')
        initialDateField.click()
        initialDateField.clear()
        time.sleep(1)
        initialDateField.send_keys(lastMonthDate.strftime("%d/%m/%Y"))  # Add last month date
        pyautogui.press('enter')
        # Final date
        finalDateField = driver.find_element_by_id('final-date')
        finalDateField.click()
        finalDateField.clear()
        time.sleep(1)
        finalDateField.send_keys(currentDate.strftime("%d/%m/%Y"))
        pyautogui.press('enter')
        time.sleep(2)

    def reportPosition(self):
        tab = ['4', '3']
        time.sleep(5)
        for i in range(2):
            pyautogui.moveTo(x=960, y=540)  # center of a 1920x1080 screen
            pyautogui.hotkey('ctrl', tab[i])
            time.sleep(2)
            self.maximizePDF()
            time.sleep(1)

    def run(self):
        for i in range(1):
            if i == 0:
                self.AccessG5()
                self.loginG5()
                self.Hosp9Julho()
                self.Relatorio('HL - BL A - 7SS - Hidrometro - Poço Artesiano - Transmissor de Vazão - 01','GS - BL A 7SS - Cozinha Sapore 6SS - 7')
                self.reportPosition()

class SetupTela1:
    def __init__(self):
        self.PB = PowerBI()
        self.G5 = G5()

    def run(self):
        self.PB.run()
        self.G5.run()

ST1 = SetupTela1()
ST1.run()
