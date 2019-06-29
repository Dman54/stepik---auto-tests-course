from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:\\Users\\Dmitriy\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(
    executable_path=r'C:\\chromedriver\\chromedriver.exe', options=chrome_options)
browser.get(link)

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)
browser.find_element_by_id('book').click()
browser.find_element_by_id('answer').send_keys(
    calc(browser.find_element_by_id('input_value').text))
browser.find_element_by_xpath('//button[@type="submit"]').click()

alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]
browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
time.sleep(3)

answer_input = browser.find_element_by_css_selector('textarea')
browser.execute_script(
    "return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)
time.sleep(1)
button = browser.find_element_by_class_name('submit-submission')
browser.execute_script("return arguments[0].scrollIntoView(false);", button)
time.sleep(1)
button.click()
