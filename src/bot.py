import time
import pyautogui
import pyperclip as pc

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


LOGIN_URL = 'https://www.facebook.com/login.php'
 
class FacebookBot():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(.1) # Wait for some time to load
 
 
 
    def login(self):
        self.driver.find_element("xpath", '//button[contains(text(), "Only allow essential cookies")]').click()
        time.sleep(.1)
        self.driver.find_element('id','email').send_keys(self.email) # Give keyboard input
        self.driver.find_element('id', 'pass').send_keys(self.password) # Give password as input too
        self.driver.find_element('id','loginbutton').click() # Send mouse click
        time.sleep(.1) 

    def post_group(self, group, text):
        text.replace("\\n", "\n")
        self.driver.get(group)
        time.sleep(1)
        self.driver.find_element("xpath", '//span[contains(text(), "Write something...")]').click()
        time.sleep(2)
        pc.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        n = 12 if "http" in text else 9
        for _ in range(n):
            pyautogui.press('tab')
            time.sleep(.1)
        pyautogui.press('enter')
        time.sleep(5)
 