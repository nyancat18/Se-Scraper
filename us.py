from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('https://www.lykke.com/exchange')
	time.sleep(5) 
	print ("crawling")

	
	sam=browser.find_element_by_css_selector('.bid_BTCUSD')
	print (sam.text)

	print ("reading")

	a = open("us.txt", "w")
	a.write(sam.text)
	a.close()

	

fa_login()
