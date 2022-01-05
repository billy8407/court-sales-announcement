import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        chrome_options=chrome_options
    )

driver.implicitly_wait(3)
driver.get("https://aomp109.judicial.gov.tw/judbp/wkw/WHD1A02.htm")

time.sleep(5)

# Need to switch to iframe.
driver.switch_to.frame(0)

# Click serach button.
driver.find_element_by_id('btn_ok').click()

time.sleep(3)

# Switch to new iframe
driver.switch_to.default_content()
driver.switch_to.frame(1)

buttons = driver.find_elements_by_tag_name('button')

# Click save button.
buttons[1].click()

time.sleep(30)
