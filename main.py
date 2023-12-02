from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from secret import email, password

class Bot:
    def __init__(self, url: str, loginSite: str = None):
        driver_path = r'C:\Users\Admin\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe'
        service = Service(driver_path, log_output='geckodriver.log')  

        self.driver = webdriver.Firefox(service=service)
            
            

        self.driver.get(url)
        # self.login(email, password)

        self.botInstructions()

    def botInstructions(self):
        
        self.clickOnButton('button._ZDS_REF_SCOPE_._4HcdR8.DJxzzA.u9KIT8.uEg2FS.U_OhzR.ZkIJC-.Vn-7c-.FCIprz.heWLCX.LyRfpJ.Md_Vex.NN8L-8.EmWJce.EvwuKo.VWL_Ot._13ipK_.gcK-9K.EKabf7.aX2-iv.r9BRio._2wi8M3.mo6ZnF.Wy3rmK', "shop nå")
        self.findChildElement("div.MU8FaS._0xLoFW._8sTSoF.parent._78xIQ-", "44")

        


    def clickOnButton(self, buttonToClick: str, checkElementText=None):
        buttonToClick=buttonToClick.replace(" ",".")
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, buttonToClick)


            self.clickElement(button, checkElementText)

        except Exception as e:
            print("Button not found or couldn't be clicked:", e)

    def clickElement(self, button: str, textToCheckAfter):            
        if textToCheckAfter is not None:
            if button.text.lower() == textToCheckAfter.lower():
                print("button.text: ",button.text)
                actions = ActionChains(self.driver)
                actions.move_to_element(button).perform()
                button.click()
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(button).perform()
            button.click()

    def scroll(self, elementToScrollOn: str, amountToScroll):
        elementToScrollOn=elementToScrollOn.replace(" ",".")

        element=self.driver.find_element(By.CSS_SELECTOR, elementToScrollOn)
        self.driver.execute_script(f"arguments[0].scrollTop += {amountToScroll}", element)

    def findChildElement(self, parentElement: str, textToCheckAfter):
        parentElement=parentElement.replace(" ",".")
        parentElement=self.driver.find_elements(By.CSS_SELECTOR, parentElement)

        for childElement in parentElement:
            print(childElement)
            self.clickElement(childElement, textToCheckAfter)

    def login(self, email, password):
        emailField = self.driver.find_element(By.ID, 'login.email')
        passwordField = self.driver.find_element(By.ID, 'login.secret')
        login_button = self.driver.find_element(By.CLASS_NAME, 'DJxzzA.u9KIT8.uEg2FS.U_OhzR.ZkIJC-.Vn-7c-.FCIprz.heWLCX._9K5FC9.LyRfpJ.R7mUGT.Md_Vex.NN8L-8.h14nQ_.tiE3Mh._5PMpaO.EKabf7.aX2-iv.r9BRio.mo6ZnF.Wy3rmK')

        emailField.send_keys(email)
        passwordField.send_keys(password)

        login_button.click()



bot = Bot('https://www.zalando.no/nike-sportswear-air-force-1-07-joggesko-white-ni112n022-a11.html',
          'https://accounts.zalando.com/authenticate?redirect_uri=https://www.zalando.no/sso/callback&client_id=fashion-store-web&response_type=code&scope=openid&request_id=yO5t6T8mGa2NgkOg:b5c30442-1fcd-4e4d-a963-c10a6912df69:8ikwUTfiXW3kF2xn&nonce=962074fa-f998-4435-8eda-bfa134dbdb7e&state=eyJvcmlnaW5hbF9yZXF1ZXN0X3VyaSI6Imh0dHBzOi8vZXhjbHVzaXZlLnphbGFuZG8ubm8vZXhjbHVzaXZlL2NoZWNrb3V0L3ZhbGlkYXRlLWJyb3dzZXI_c2t1PU5JMTEyTjAyMi1BMTEwMDk1MDAwIiwidHMiOiIyMDIzLTEyLTAyVDE2OjUzOjE0WiJ9&ui_locales=no-NO&zalando_client_id=b5c30442-1fcd-4e4d-a963-c10a6912df69&cid=GA1.2.584526696.1701535993&sales_channel=ef064ea7-1d91-442c-bcbb-9d20749af19b&client_country=false&client_category=fs',
          
          )


