from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def login_composedrafts(email, password, clients):
	browser = webdriver.Chrome("driver/chromedriver.exe")
	browser.get("http://gmail.com")

	# login
	elem = driver.find_element_by_css_selector("input[type='email']")
	elemn.send_keys(email)
	time.sleep(3)
	elem = driver.find_element_by_css_selector("input[type='password']")
	elemn.send_keys(password)
	time.sleep(3)
	elem = driver.find_element_by_css_selector('div[id=passwordNext]')
	elem.click()
	time.sleep(10)

	# compose drafts
	for client in clients:
		# compose button
		elem = driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3")
		elem.click()
		time.sleep(3)
		# enable cc
		elem = driver.find_element_by_xpath("//span[@class='aB gQ pE']")	
		elem.click()
		time.sleep(3)
		# enter email
		elem = driver.find_element_by_xpath("//form[1]//textarea[1]")	
		elem.send_keys(client[1])
		time.sleep(3)
		# enter cc
		elem = driver.find_element_by_xpath("//textarea[@name='cc']")	
		elem.send_keys(client[2])
		time.sleep(3)
		# enter subject
		elem = driver.find_element_by_xpath("//div[@class='aoD az6']//input[@class='aoT']")	
		elem.send_keys(client[3])
		time.sleep(3)
		# enter body
		elem = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")	
		elem.send_keys(client[4])
		time.sleep(3)
		# close draft
		elem = driver.find_element_by_xpath("//img[@class='Ha']")	
		elem.click()
		time.sleep(3)
	browser.quit()