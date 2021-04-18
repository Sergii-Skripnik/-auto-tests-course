from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(13)
    browser.get(link)

    element2 = browser.find_element_by_css_selector("#book")
    element1 = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100" ))
    element2.click()
    #alert = browser.switch_to.alert
    #time.sleep(2)
    #alert.accept()
    #alert = WebDriverWait.until(EC.alertIsPresent());
    #alert.accept();
   
    element4 = browser.find_element_by_css_selector("button[type = 'submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element4) 
    element3 = browser.find_element_by_css_selector("#answer")
    x = browser.find_element_by_css_selector("#input_value").text
    print(x)    
    element3.send_keys(calc(x))

    
    #element4 = browser.find_element_by_css_selector("button[type = 'submit']")
    element4.click()

    

    

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

