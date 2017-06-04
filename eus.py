from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('https://ethereumprice.org/')
	time.sleep(5) 
	print ("crawling")

	
	sam=browser.find_element_by_css_selector('.rp')
	print (sam.text)

	print ("reading")

	a = open("eus.txt", "w")
	a.write(sam.text)
	a.close()

	

fa_login()
