class loginPage():
    # Locators of all the elements
    userName_id = "Email"
    textbox_password_id = "Password"
    button_login = "//button[@type='submit']"
    logout_xpath = "//a[normalize-space()='Logout']"
    # logout_linkText = "Logout"

    # Create a constructor

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.userName_id).clear()
        self.driver.find_element_by_id(self.userName_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()