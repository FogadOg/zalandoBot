from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from secret import email, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# C:\Users\Fogad\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python3.11

class Bot:
    def __init__(self, url: str):
        driver_path = "C:/Users/Fogad/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe"
        service = Service(driver_path, log_output='geckodriver.log')  

        # self.driver = webdriver.Firefox(service=service)
        self.driver = uc.Chrome(headless=False,use_subprocess=False)
        options = uc.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36")

        self.driver.get(url)

        self.botInstructions()



    def botInstructions(self):
        self.clickOnButton('button._ZDS_REF_SCOPE_._4HcdR8.DJxzzA.u9KIT8.uEg2FS.U_OhzR.ZkIJC-.Vn-7c-.FCIprz.heWLCX.LyRfpJ.Md_Vex.NN8L-8.EmWJce.EvwuKo.VWL_Ot._13ipK_.gcK-9K.EKabf7.aX2-iv.r9BRio._2wi8M3.mo6ZnF.Wy3rmK', "shop nå")
        self.clickOnButton('button.uc-btn.uc-btn-primary', "Det er OK")
        
        self.clickOnButton("div.YuYw-E.JT3_zV._0xLoFW._78xIQ-.EJ4MLB", "44")

        self.waitForPageToLoad("Logg inn", 10)
        self.fillOutField(email, 'login.email')
        self.fillOutField(password, 'login.secret')
        self.clickOnButton('DJxzzA.u9KIT8.uEg2FS.U_OhzR.ZkIJC-.Vn-7c-.FCIprz.heWLCX._9K5FC9.LyRfpJ.R7mUGT.Md_Vex.NN8L-8.h14nQ_.tiE3Mh._5PMpaO.EKabf7.aX2-iv.r9BRio.mo6ZnF.Wy3rmK')
        
        self.waitForPageToLoad("Adresse", 10)         
        self.clickOnButton('a.z-coast-fjord_deliveryDestinationTab_option.z-coast-fjord_deliveryDestinationTab_option-selected.z-coast-fjord_deliveryDestinationTab_option_PICKUP_POINT', "shop nå")


    def waitForPageToLoad(self, pageTitle:str, idk: int):
        wait = WebDriverWait(self.driver, idk)
        wait.until(EC.title_contains(pageTitle))

    def clickOnButton(self, buttonToClick: str, checkElementText=None):
        buttonToClick = buttonToClick.replace(" ", ".")
        try:
            buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, buttonToClick))
            )
            self.clickElement(buttons, checkElementText)
        except Exception as e:
            print("Button not found or couldn't be clicked:", e)

    def clickElement(self, buttons: str, textToCheckAfter):          
        for button in buttons:    
            if textToCheckAfter is not None:
                if textToCheckAfter.lower() in button.text.lower():
                    actions = ActionChains(self.driver)
                    actions.move_to_element(button).perform()
                    button.click()
                    break
            else:
                actions = ActionChains(self.driver)
                actions.move_to_element(button).perform()
                button.click()
                break

    def fillOutField(self, text:str, fieldId:str):
        emailField = self.driver.find_element(By.ID, fieldId)

        emailField.send_keys(text)



if __name__ == "__main__":

    bot = Bot(
    'https://www.zalando.no/nike-sportswear-air-force-1-07-joggesko-white-ni112n022-a11.html',
    )