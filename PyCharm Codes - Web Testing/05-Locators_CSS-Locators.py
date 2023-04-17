# Import the service class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://facebook.com")

driver.maximize_window()

# CSS SELECTOR -----> Tag & Id Combination
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("rohaandas212@gamil.com")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("rohaandas212@gamil.com")      #Tag is Optional

# CSS SELECTOR -----> Tag & Class Combination
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Mohit.Singh@yahoo.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("Mohit.Singh@yahoo.com")     #Tag is Optional

# CSS SELECTOR -----> Tag & Attribute Combination
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("Priya.dogra.7777@hotmail.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("Priya.dogra.7777@hotmail.com")      #Tag Optional

# CSS SELECTOR -----> Tag, Class & Attribute Combination
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass").send_keys("458494894894988")
