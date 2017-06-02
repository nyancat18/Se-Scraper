from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.Chrome()
	browser.implicitly_wait(10)
	browser.get('https://www.bithumb.com/EN/')
	time.sleep(5) 
	print ("crawling")

	
	btckp=browser.find_element_by_css_selector('.real_krw')
	print (btckp.text)

	print ("reading")

	a = open("kp.txt", "w")
	a.write(btckp.text)


fa_login()
