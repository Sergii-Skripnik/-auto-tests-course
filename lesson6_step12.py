from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("#input_value").text
    #x = get_element_text(element1)

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