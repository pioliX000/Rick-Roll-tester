from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys
import time
import requests

def rrt(x):
	output = requests.get(x, headers={"User-Agent":"curl/7.44.0"}).text.lower()
	if "never gonna give you up" in output or "dQw4w9WgXcQ".lower() in output:
		y = "RUN BRUV"
	else:
		y ="u good bruv go ahead"
	print("check1:", y)

def selenium(x):
	options = Options()
	options.add_argument('-headless')
	driver = webdriver.Firefox(options=options)
	driver.get(x)
	html_source = driver.execute_script("return document.body.innerHTML;").lower()		
	title = driver.title
	if "rick" in title.lower() :
		driver.close()
		print("check2: RUN BRUV")
	else:
		try:
			if "never gonna give you up" in html_source or "dQw4w9WgXcQ".lower() in html_source or "rick astley" in html_source:
				y = "RUN BRUV"	
			else:
				y = "u good bruv go ahead"
			print("check2:", y)
			driver.close()
		except:
			pass
			print("check2: u good bruv... I think")

try:
	rrt(sys.argv[1])
	try:
		selenium(sys.argv[1])
	except: 
		print("check2: error!")

except IndexError:
	print("Supply a link!")
