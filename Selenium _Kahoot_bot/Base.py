from selenium import webdriver
import time
from unicodedata import name
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Global variables
# TODO: change every time the code of the kahoot'a game
code = 330096


def kahootbot():
    # MACOS path
    PATH = "/Users/marcovinciguerra/Github/Python/Selenium _Kahoot_bot/ChromeDriver/chromedriver"

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com/")

    driver.get("https://kahoot.com/")
    driver.set_window_size(1229, 898)
    driver.find_element_by_css_selector(
        "#menu-item-92364 .menu-item-text").click()
    driver.find_element_by_id("game-input").click()
    driver.find_element_by_id("game-input").send_keys(code)
    driver.find_element_by_css_selector(".sc-jJEJSO").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@id='nickname']"))).send_keys("vinci0000")
    driver.find_element_by_css_selector(".sc-jJEJSO").click()
    actions = ActionChains(driver)

    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    kahootbot()
