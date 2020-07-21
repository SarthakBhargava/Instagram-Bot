from selenium import webdriver
from time import sleep


class instagram_bot:

    def __init__(self, username, password, uname):
        self.username = username
        self.password = password
        self.uname = uname

        self.driver = webdriver.Chrome("chromedriver.exe")

        self.base_url = "https://instagram.com"

        self.driver.get(self.base_url)

        sleep(5)
        self.login()

        sleep(1)
        try:
            self.follow_user(self.uname)
        except:
            print("Already Followed")

        sleep(1)
        self.like()

        sleep(1)
        self.user()

    def login(self):
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        sleep(1)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def user(self):
        self.driver.get(self.base_url + '/' + self.username)

    def follow_user(self, user):
        self.driver.get(self.base_url + '/' + user)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()

    def like(self):

        sleep(1)

        self.driver.find_element_by_class_name('v1Nh3').click()

        i = 1
        while i == 1:
            sleep(3)
            try:
                self.driver.find_element_by_class_name('fr66n').click()
            except:
                sleep(2)
                print("Like")
                self.driver.find_element_by_class_name('fr66n').click()

            try:
                sleep(2)
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            except:
                i = 0




if __name__ == '__main__':
    username = input("Enter Your Username")
    password = input("Enter Your Password")
    uname = input("Enter User Name of Other Person\n")
    bot = instagram_bot(username, password, uname)