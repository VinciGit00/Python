from selenium import webdriver
import time

def kahootbot():
    # MACOS path
    PATH = "/Users/marcovinciguerra/Github/Python/Selenium _Kahoot_bot/ChromeDriver/chromedriver"    

    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com/")

    driver.get("https://kahoot.com/")
    driver.set_window_size(1229, 898)
    driver.find_element_by_css_selector("#menu-item-92364 .menu-item-text").click()
    driver.find_element_by_id("game-input").click()
    driver.find_element_by_id("game-input").send_keys("14988")
    driver.find_element_by_css_selector(".sc-jJEJSO").click()
    driver.find_element_by_class_name("nickname").click()
    driver.find_element_by_id("nickname").send_keys("vinci00")
    driver.find_element_by_css_selector(".sc-jJEJSO").click()   
    actions = ActionChains(driver)

    actions.move_to_element(element).perform()

    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    kahootbot()
