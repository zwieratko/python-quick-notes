from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Options
options = Options()

# # Option for using a custom Firefox profile
profile_path = 'D:\\0media\\Pictures\\zwieratko.sk\\random_person_firefox\\xxx007.default'
options.set_preference('profile', profile_path)

# # Enable headless
options.headless = False

# Specify custom geckodriver path
service = Service(r"C:\Users\Radovan\Development\geckodriver_win64\geckodriver.exe")

# Test
browser = webdriver.Firefox(options=options, service=service)
browser.get('https://backup.zwerimex.com/testMap21')
print(browser.title)

# time.sleep(2)
# browser.get("https://zwieratko.sk")
# print(browser.title)
