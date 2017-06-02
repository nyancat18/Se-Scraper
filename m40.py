from selenium import webdriver
import time
import pyinotify
import os
def fa_login():
	browser=webdriver.Chrome()
	browser.implicitly_wait(3)
	browser.get('https://mail.cock.li/')
	time.sleep(3) 

	user=browser.find_element_by_css_selector('#rcmloginuser')
	user.send_keys('cryptonumbers@memeware.net')
	time.sleep(0)
	user1=browser.find_element_by_css_selector('#rcmloginpwd')
	user1.send_keys('card late toad angus brown volt')		
	signinButton=browser.find_element_by_css_selector("#rcmloginsubmit")
	signinButton.click()
	print ("PASS LOGGED")
	time.sleep(30)
	comp=browser.find_element_by_css_selector('#rcmbtn108')
	comp.click()
	print("MAKING")
	time.sleep(5)
	camp=browser.find_element_by_css_selector('#_to')
	camp.send_keys('mrtybll@gmail.com')
	su=browser.find_element_by_css_selector('#compose-subject')
	su.send_keys('BTC +40% difference alert')
	canta=browser.find_element_by_css_selector('#composebody')
	canta.send_keys('The difference between US and Korean markets its +40%')
	cag=browser.find_element_by_css_selector('#rcmbtn108')
	cag.click()
	print("MAKING")








	
	links=browser.find_elements_by_css_selector("a.ProfileCard-bg")
	print("test")
	for link in links:
		print (link.get_attribute('href'))
		a = open("GuaranyBrazil.txt", "a")
		a.write(";"+link.get_attribute('href'))
		a.close()
	os.system('sh NA.sh')
		


fa_login()