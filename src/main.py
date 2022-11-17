import os
from bot import FacebookBot
from decouple import config, UndefinedValueError
from getpass import getpass
import time

class App():
    def __init__(self):
        try:
            self.email = config("FB_EMAIL")
            self.password = config("FB_PASSWORD")
        except UndefinedValueError:
            print("No env variables defined\n")
            self.email = input("\n\tEmail: ")
            self.password = getpass("\n\tPassword: ")
            with open(".env", "w") as f:
                f.write(f"FB_EMAIL={self.email}\nFB_PASSWORD={self.password}")
    
        self.fb_login = FacebookBot(email=self.email, password=self.password, browser='Firefox')
        self.fb_login.login()
        if not os.path.exists("./src/text.txt"):
            input("Write the text to post in a file called [text.txt] at the src route\nPress Enter to continue ")
        with open("./src/text.txt", "r") as f:
            self.text = f.read()
            print(self.text)
        print("\n","="*30, "\n\n\nClick on firefox/chrome window\n", sep="")
        time.sleep(5)

    def post(self):
        groups = []
        with open("./src/urls.txt", "r") as f:
            groups = [x for x in f.readlines() if x not in ("", "\n") and x[0]!="#"]
        print(groups)
        for group in groups:
            self.fb_login.post_group(group, self.text)

    
if __name__ == '__main__':
    # Enter your login credentials here
    try:
        app = App()
        app.post()
    except Exception as ex:
        print(ex)
    os.remove("geckodriver.log")