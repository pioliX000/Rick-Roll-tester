from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys
import time
import requests

def rrt(x):
	output = requests.get(x, headers={"User-Agent":"curl/7.44.0"}).text.lower()
	if "never gonna give you up" in output or "dQw4w9WgXcQ" in output:
		y = "RUN BRUV"
	else:
		y ="u good bruv go ahead"
	print("check1:", y)

def selenium(x):
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	html_source = driver.execute_script("return document.body.innerHTML;")
	driver.get(x)
	time.sleep(5)
	title = driver.title
	print(html_source)
	if title == "Rick Astley - Never Gonna Give You Up (Official Music Video) - YouTube":
		driver.close()
		print("check2: RUN BRUV")
	else:
		try:
			elem = driver.find_element_by_class_name("mwButton")
			time.sleep(10)
			output = elem.get_attribute('outerHTML')
			if "never gonna give you up" in output or "dQw4w9WgXcQ" in output:
				y = "RUN BRUV"	
			elif "never gonna give you up" in title or "rick ansley" in title:
				y = "RUN BRUV"
			else:
				y = "u good bruv go ahead"
			print("check2:", y)
			driver.close()
		except:
			pass
			print("check2: u good bruv... I think")

rrt(sys.argv[1])
selenium(sys.argv[1])