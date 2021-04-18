from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#input_value").text
   
    element2 = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element2)
    element2.send_keys(calc(x))

    element3 = browser.find_element_by_css_selector("#robotCheckbox")
    element3.click()


    element4 = browser.find_element_by_css_selector("#robotsRule")
    element4.click()
    
    
   
    element5 = browser.find_element_by_css_selector("button[type = 'submit']")
   
    #time.sleep(2)
    element5.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
