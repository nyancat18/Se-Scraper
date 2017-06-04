from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('https://coinmarketcap.com/currencies/ripple/')
	time.sleep(5) 
	print ("crawling")

	
	sam=browser.find_element_by_css_selector('#quote_price')
	print (sam.text)

	print ("reading")

	a = open("xus.txt", "w")
	a.write(sam.text)
	a.close()

	

fa_login()
