from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Service = Service('C:\\Users\IsmartSiva\Downloads\chromedriver-win64\chromedriver.exe')
# Web driver is tool allow us to control the browser.

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars") # disable the info bars
  options.add_argument("start-maximized") # start the browser in maximized mode
  options.add_argument("disable-dev-shm-usage") # disable the use of the dev shm where we try to use from linux. some issues may occur. to avoid that.
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable the automation
  options.add_argument("disable-blink-features=AutomationControlled") 
  
  driver = webdriver.Chrome(service=Service,options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())

