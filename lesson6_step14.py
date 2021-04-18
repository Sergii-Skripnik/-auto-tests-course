from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector("#treasure")
    x = element1.get_attribute("valuex")
    print("value of people radio: ", x)

    element2 = browser.find_element_by_css_selector("#answer")
    element2.send_keys(calc(x))

    element3 = browser.find_element_by_css_selector("#robotCheckbox")
    element3.click()


    element4 = browser.find_element_by_css_selector("#robotsRule")
    element4.click()
    time.sleep(2)


    element5 = browser.find_element_by_css_selector("button[type = 'submit']")
    element5.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
