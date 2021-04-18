from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector("[name = 'firstname']")
    element1.send_keys('1')

    element2 = browser.find_element_by_css_selector("[name = 'lastname']")
    element2.send_keys('2')

    element3 = browser.find_element_by_css_selector("[name = 'email']")
    element3.send_keys('3')

    element4 = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
    element4.send_keys(file_path)
    
       
    element5 = browser.find_element_by_css_selector("button[type = 'submit']")
   
    #time.sleep(2)
    element5.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

