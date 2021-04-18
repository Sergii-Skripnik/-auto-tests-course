from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return (int (x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#num1").text
    #z = int(x)
    y = browser.find_element_by_css_selector("#num2").text
    c = int(y) + int (x)
    
   
    select = Select(browser.find_element_by_tag_name("select"))
    #time.sleep(2)
    select.select_by_value(str(c))
    
   

    element5 = browser.find_element_by_css_selector("button[type = 'submit']")
    element5.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

