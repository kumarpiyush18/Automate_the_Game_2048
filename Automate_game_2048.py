import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
driver.get('https://gabrielecirulli.github.io/2048/')

elem = driver.find_element_by_tag_name('body')
while True:
	elem.send_keys(Keys.DOWN)   # replace the (Arrow key) with your logic to score better:)
	elem.send_keys(Keys.LEFT)
	elem.send_keys(Keys.DOWN)    
	elem.send_keys(Keys.RIGHT)
	
