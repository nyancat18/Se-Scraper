from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('http://localhost:7658/site/')
	time.sleep(5) 
	print ("crawling")

	
	test=browser.find_element_by_css_selector('#math')
	mad=test.text
	mat=float(mad)

	print (mat)
	
	if (mat > 20) : os.system('python m20.py')
	if (mat > 20) : os.system("python m30.py")
	if (mat > 20) : os.system("python m40.py")

	

fa_login()
