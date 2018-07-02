#<input type="email" class="inputtext" name="email" id="email" tabindex="1" data-testid="royal_email">



from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# browser.get("https://en-gb.facebook.com/login.php?login_attempt=1&lwv=100")
browser.get("http://10.217.55.151")
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys("admin")
print "username entered"
password.send_keys("password")
print "password entered"
login_attempt = browser.find_element_by_xpath("//span[@id='button-1016-btnInnerEl']")
login_attempt.click()
print "login done "
print "welcome to sandbox "
time.sleep(10)
browser.find_element_by_xpath("//*[@id='gridview-1049-record-9']/tbody/tr/td[2]/div").click()
print " clicked ui policy "
time.sleep(10)

# browser.find_element_by_xpath("//*[@id=gridview-1084-record-159']/tbody/tr/td[7]/div/img").click()
# print " clicked check button"
# time.sleep(2)

browser.find_elements_by_xpath(".//*[@class='x-grid-item-container']/table/tbody/tr/td[2]/div")[2].click()
print " clicked 1"
browser.find_elements_by_xpath(".//*[@class='x-grid-item-container']/table/tbody/tr/td[2]/div")[2].click()
print " clicked 2"

browser.quit()



