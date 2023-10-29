from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://demo.nopcommerce.com/")
driver.get("https://secure.yatra.com")
text = driver.find_element(By.XPATH,'//span[normalize-space()="Villas & Stays"]').text 
print(text)

#find element by id
search_box = driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#find element by linktext and partial link text
# driver.find_element(By.LINK_TEXT,"Register").click()
# find element by partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


driver.get("https://secure.yatra.com/social/common/yatra/register")
driver.maximize_window()
reg_input = driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys("test@test.com")
reg_input = driver.find_element(By.XPATH,'//input[@id="login-input"]').send_keys("test@test.com")

time.sleep(4)
driver.close()

class DemoBrowser:
    def demo_browser_method(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com")
        print(driver.current_url)
        print(driver.title)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH,'//span[normalize-space()="Villas & Stays"]').click() 
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.close()
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.quit()

# demo_browser1 = DemoBrowser()
# demo_browser1.demo_browser_method()