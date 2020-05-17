from selenium import webdriver

URL = 'https://github.com/login'

driver = webdriver.Chrome()

def github_login():

    driver.get(URL)
    username = driver.find_element_by_id("login_field")
    username.clear()
    username.send_keys("doradodev")

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("pass")

    driver.find_element_by_name("commit").click()
