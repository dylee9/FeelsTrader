"""
webscraper.py
"""
import time
import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":

	DRIVER_PATH = "drivers/chromedriver"
	TARGET_URL = "https://stocktwits.com"
	USERNAME = "runningmanruns"
	PASSWORD = "runningmanruns123"

	# set option parameters
	# options = Options()
	# options.headless = True
	# options.add_argument("--window-size=1920,1200")

	# launch url on chrome
	driver = webdriver.Chrome(executable_path=DRIVER_PATH)
	driver.get(TARGET_URL)

	time.sleep(1)

	# click login button
	login = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/nav/div[3]/div/div/div[1]/button").click()

	# login
	username = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div[2]/div/form/div[1]/div[1]/label/input").send_keys(USERNAME)
	password = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div[2]/div/form/div[1]/div[2]/label/input").send_keys(PASSWORD)
	submit = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div[2]/div/form/div[2]/div[1]/button").click()

	time.sleep(3)

	# move to trending page
	trending = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div/div/div[1]/div/div/div[3]/div[1]/div/div/div[5]/div/div").click()

	# 5-min one-time scanner
	# wait 5 minutes for new posts
	time.sleep(300)

	# find refresh posts button
	try:
		refresh = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div/div/div[1]/div/div/div[2]/div/div/div")
	except:
		refresh = None

	# if new posts exist, load new posts
	if refresh:
		refresh.click()

	h1 = driver.find_elements_by_class_name('st_3SL2gug')

	for elem in h1:
		print(elem.text)

	# h1 = driver.find_elements_by_class_name('st_3SL2gug')
	# h2 = driver.find_elements_by_class_name('st_1H1PshU st_1SuHTwr')

	# for elem in h1:
	# 	print(elem.text)

	# look for new posts
	# while(True):

		# # exit look with x key
		# try:
		# 	if keyboard.is_pressed('x'):
		# 		break
		# except:
		# 	continue

		# find refresh posts button
		# try:
		# 	refresh = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div/div/div[1]/div/div/div[2]/div/div/div")
		# except:
		# 	refresh = None

		# if new posts exist, load new posts
		# if refresh:
		# 	refresh.click()

		# 	h1 = driver.find_elements_by_class_name('st_3SL2gug')

		# 	for elem in h1:
		# 		print(elem.text)

	driver.quit()




