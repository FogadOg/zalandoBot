from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains






class Bot():
    def __init__(self, url: str, loginSite: str = None):
        driver_path = r'C:\Users\Admin\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe'
        service = Service(driver_path, log_path='geckodriver.log')  

        while True:
            self.driver = webdriver.Firefox(service=service)
            if loginSite!=None:
                self.driver.get(loginSite)

            self.driver.get(url)

            self.botInstructions()
        self.driver.quit()
        

    def botInstructions(self):
        self.clickOnButton('button._ZDS_REF_SCOPE_._4HcdR8.DJxzzA.u9KIT8.uEg2FS.U_OhzR.ZkIJC-.Vn-7c-.FCIprz.heWLCX.LyRfpJ.Md_Vex.NN8L-8.EmWJce.EvwuKo.VWL_Ot._13ipK_.gcK-9K.EKabf7.aX2-iv.r9BRio._2wi8M3.mo6ZnF.Wy3rmK', "shop nå")
    
    def clickOnButton(self, buttonToClick, checkElementText=None):
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, buttonToClick)

            self.clickElement(button, checkElementText)

        except Exception as e:
            print("Button not found or couldn't be clicked:", e)

    def clickElement(self, button, textToCheckAfter):            
        if textToCheckAfter!=None:
            if button.text.lower()==textToCheckAfter.lower():
                actions = ActionChains(self.driver)
                actions.move_to_element(button).perform()

                button.click()
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(button).perform()

            button.click()




Bot(
    'https://www.zalando.no/nike-sportswear-air-force-1-07-joggesko-white-ni112n022-a11.html',
    'https://accounts.zalando.com/authenticate?redirect_uri=https://www.zalando.no/sso/callback&client_id=fashion-store-web&response_type=code&scope=openid&request_id=yO5t6T8mGa2NgkOg:b5c30442-1fcd-4e4d-a963-c10a6912df69:8ikwUTfiXW3kF2xn&nonce=962074fa-f998-4435-8eda-bfa134dbdb7e&state=eyJvcmlnaW5hbF9yZXF1ZXN0X3VyaSI6Imh0dHBzOi8vZXhjbHVzaXZlLnphbGFuZG8ubm8vZXhjbHVzaXZlL2NoZWNrb3V0L3ZhbGlkYXRlLWJyb3dzZXI_c2t1PU5JMTEyTjAyMi1BMTEwMDk1MDAwIiwidHMiOiIyMDIzLTEyLTAyVDE2OjUzOjE0WiJ9&ui_locales=no-NO&zalando_client_id=b5c30442-1fcd-4e4d-a963-c10a6912df69&cid=GA1.2.584526696.1701535993&sales_channel=ef064ea7-1d91-442c-bcbb-9d20749af19b&client_country=false&client_category=fs'
    
    )