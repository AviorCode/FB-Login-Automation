```python
import selenium
import pyautogui as pg
from selenium import webdriver


#path of the driver

driver = webdriver.Chrome('C:/Users/Avior/Desktop/chromedriver')
driver.get('https://www.facebook.com/')

#credentials
user = 'Your user' 
pw = 'Your password'
#HTML Login locator
fb_username = driver.find_element_by_css_selector('#email')
fb_pw = driver.find_element_by_css_selector('#pass')   

#sleep for a sec    
pg.sleep(1)
#injecting user credentials  
fb_username.send_keys(user)
pg.sleep(1)
fb_pw.send_keys(pw)

#maximizing the window
driver.maximize_window()
#sleeping for a sec
pg.sleep(1)
#performing login.
login_buton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
login_buton.click()

print('Login Succesfull')
```
