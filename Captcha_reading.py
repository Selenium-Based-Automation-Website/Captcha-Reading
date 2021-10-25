#USING PYTHON WE READ CAPCHA
from selenium import webdriver
from PIL import Image
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome('chromedriver.exe',options = chrome_options )
driver.get('https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html')
driver.maximize_window()

capcha = driver.find_element_by_id('captchaImg1')
capcha.screenshot('capcha_.png')
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
reader = easyocr.Reader(['en'])
Image("capcha_.png")
output = reader.readtext('capcha_.png')
cord = output[-1][1]

capcha_fill = driver.find_element_by_id('captcha1')
capcha_fill.send_keys(cord)
time.sleep(1000)
driver.quit()
