import pytest


from selenium.webdriver.common.by import By

def test_open_api(browser):
 
    url = "https://reqres.in"
    browser.get(url=url)
    
    element = browser.find_element(by=By.CSS_SELECTOR, value="[data-id='unknown-single']")
    element.click()
    
    x_path_single_resource = '//*[@id="console"]/div[2]/div[1]/p/strong/a/span'
    element = browser.find_element(By.XPATH, value= x_path_single_resource)
    element.click()
    

    assert True, ""