from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ChromeDriverManager:
    pass

"""Part 1: Front-End Automation Testing:"""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('Stack Overflow - Where Developers Learn, Share, & Build Careers')
driver.find_element(By.XPATH("//div[contains(text(),'Users')]")).click()
driver.find_element(By.XPATH("//a[contains(text(),'Editors')]")).click()
driver.find_element(By.XPATH("//a[contains(text(),' Next')]")).click()
userName = driver.find_element(By.XPATH("//span[text()='212']//parent::div//parent::div//child::a")).text()
