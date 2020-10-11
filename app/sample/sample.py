from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
selenium_server = 'http://172.16.3.3:4444/wd/hub' 
 

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor=selenium_server,
    desired_capabilities=DesiredCapabilities.CHROME,
    options=options
)
 
driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')
driver.quit()
