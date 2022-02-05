from selenium import webdriver
#dirver = webdriver.Firefox()
#driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:5555',
   desired_capabilities=DesiredCapabilities.OPERA)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
