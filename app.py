from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(4)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(4)
        posts = bot.find_element_by_css_selector('img.FFVAD')
        print(posts)


bot = InstaBot('pierre.lecorff3@gmail.com', 'poiuytre63&*')
bot.login()
time.sleep(1)
bot.like_tweet('tesla')