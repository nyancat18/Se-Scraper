from selenium import webdriver
import time
import os
print ("start")
def fa_login():
	browser=webdriver.PhantomJS()
	browser.implicitly_wait(10)
	browser.get('https://coinmarketcap.com/exchanges/coinone/')
	time.sleep(5) 
	print ("crawling")

	
	btckp=browser.find_element_by_xpath('//*[@id="markets"]/table/tbody/tr[3]/td[5]')
	print (btckp.get_attribute('data-usd'))


	print ("reading")

	a = open("xkp.txt", "w")
	a.write(btckp.get_attribute('data-usd'))


fa_login()
