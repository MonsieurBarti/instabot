from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(3)
        bot.find_element_by_xpath("//button[contains(text(), 'Plus tard')]")\
            .click()
        sleep(2)

    def get_followers(self):
        bot = self.bot
        bot.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[4]/nav/ul/li[11]/span/select/option[6]")\
            .click()
        sleep(1.5)
        bot.find_element_by_xpath("//a[@href = '/explore/']")\
            .click()
        sleep(1)
        bot.find_element_by_xpath("//a[@href = '/explore/people/']")\
            .click()
        sleep(1)
        self.follow()

    def follow(self):
        bot = self.bot
        sleep(2)
        sugs = bot.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        bot.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = bot.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_xpath("//button[text()='Follow']")
        for link in links:
            link.click()
            sleep(.5)
        # close button
        bot.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()

bot = InstaBot('devbybart', 'poiuytre63&*')
bot.login()
sleep(1)
bot.get_followers()