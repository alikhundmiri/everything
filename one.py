# This is a duplicate answer **Reconnect to a driver in python selenium ** This is applicable on all drivers. 1. open a driver

from selenium import webdriver

driver = webdriver.Chrome()
# 2. extract to session_id and _url from driver object.

url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
# 3. Use these two parameter to connect to your driver.
print(session_id)
print(url)
driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id
# And you are connected to your driver again.

driver.get("http://www.mrsmart.in")