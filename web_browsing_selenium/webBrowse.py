
from selenium import webdriver
from selenium.webdriver.option import Options

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", )
##driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
