from selenium import webdriver
import time
import math
 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector(".btn-primary")
    element1.click()
    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("#input_value").text

    element2 = browser.find_element_by_css_selector("#answer")
    element2.send_keys(calc(x))

         
    element3 = browser.find_element_by_css_selector("button[type = 'submit']")
    element3.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

