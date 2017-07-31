from selenium import webdriver
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/nazmiye/Desktop/ab2017/eBrandValue/seleniumTest/chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://qnbfinansbank-crm.ebrandvalue.com/"
    #     before to be login
    def test_login_page(self):
        driver = self.driver
        driver.get(self.base_url)
        # control login page with page title
        if self.driver.title == 'eBrandValue':
            Test.printhandle(self, str("Crm page"), str(1))
        else:
            Test.printhandle(self, str("Crm page"), str(0))
        username = self.driver.find_element_by_id("id_username")
        username.send_keys("***")
        password = self.driver.find_element_by_id("id_password")
        password.send_keys("***")
        login_attempt = self.driver.find_element_by_xpath("//*[@type='submit']")
        login_attempt.click()
        # control home page after the login
        if self.driver.title == 'eBrandValue Social CRM':
            Test.printhandle(self, "login", str(1))
        else:
            Test.printhandle(self, "login", str(0))
        driver = self.driver
        # call another control functions and they are tested
        Test.headsOnHomePages(self, driver)
        Test.filterBrandStream(self, driver)
        Test.postNumAtLive(self, driver)
        Test.savedContents(self, driver)
        driver = self.driver
        Test.twitter(self, driver)
        Test.twitterDm(self, driver)
        Test.facebookDm(self, driver)
        Test.instagram(self, driver)
        driver = self.driver
        Test.stat(self, driver)
        Test.logoutControl(self, driver)

    def headsOnHomePages(self, driver):
        qnb_finansbank = driver.find_element_by_xpath("//ul[@id='items']/li[1]/a")
        stats = driver.find_element_by_xpath("//ul[@id='items']/li[2]/a")
        brand_stream = driver.find_element_by_xpath("//ul[@id='items']/li[3]/a")
        if qnb_finansbank.text == 'QNB Finansbank' and stats.text == ' Stats' and brand_stream.text == ' Brand Stream':
            Test.printhandle(self, 'items of menu', str(1))
        else:
            Test.printhandle(self, 'items of menu', str(0))
    # control choices of filter
    def filterBrandStream(self, driver):
        filter_names = driver.find_elements_by_xpath("//span[@class='box-title']")
        x = len(filter_names)
        word_select = driver.find_element_by_xpath(
            "//div[@class='box']/div[@class='box-header']/span[@class='box-title']")
        word_select.click()
        word_selected = driver.find_element_by_xpath(
            "//div[@class='box active']/div[@class='box-header']/span[@class='box-title']")
        self.assertIn(word_select.text, word_selected.text)
        word_select.click()
        word_textbox = driver.find_element_by_xpath("//div[@class='box']/div[@class='box-content']/input")
        word_text = word_textbox.get_attribute("type")
        media_boxes = driver.find_elements_by_xpath("//div[@class='box sources']//ul[@class='icon-set clearfix']")
        if x > 0 and word_text == 'text' and len(media_boxes) > 0:
            Test.printhandle(self, 'filterforhomepage', str(1))
        else:
            Test.printhandle(self, 'filterforhomepage', str(0))
    #          post number of live feed calculate and test
    def postNumAtLive(self, driver):
        mentions = driver.find_elements_by_xpath("//div[@class='mention zebra']/div[@class='post']")
        x = len(mentions)

        if x >= 0:
            Test.printhandle(self, 'post', str(1))
        else:
            Test.printhandle(self, 'post', str(0))
    # just to be click saved contents page and to filter
    def savedContents(self, driver):
        saved_contents = driver.find_element_by_xpath("//ul[@class='tab clearfix']//span[@data-rel='stats']")
        saved_contents.click()
    # twitter filter is test . all posts have twit
    def twitter(self, driver):
        twitter_filter = driver.find_element_by_id("media-twitter")
        twitter_filter.click()
        filter_button = driver.find_element_by_xpath("//a[@class='search-by-query button']")
        filter_button.click()
        for page in range(0, 2):
            posts = driver.find_elements_by_xpath("//div[@class='post-icons clearfix']/div[@class='post-icon'][1]/span")
            for post in posts:
                classname=post.get_attribute("class")
            nextpage = driver.find_element_by_xpath("//div[@id='pagination']//a[@class='page-link next']")
            nextpage.click()
            if 'source-icon icon-twitter' in classname:
                twit = 1
            else:
                twit = 0
                break

        Test.printhandle(self, "twitter", str(twit))

    def twitterDm(self, driver):
        twitter_dm_filter = driver.find_element_by_id("media-twitter-dm")
        twitter_dm_filter.click()
        filtrele_button = driver.find_element_by_xpath("//a[@class='search-by-query button']")
        filtrele_button.click()
        for page in range(0, 2):
            posts = driver.find_elements_by_xpath("//div[@class='post-icons clearfix']/div[@class='post-icon'][1]/span")
            for post in posts:
                classname=post.get_attribute("class")
            nextpage = driver.find_element_by_xpath("//div[@id='pagination']//a[@class='page-link next']")
            nextpage.click()
            if 'source-icon icon-twitter' in classname:
                twit = 1
            else:
                twit = 0
                break

        Test.printhandle(self, "twitter Dm", str(twit))

    def facebookDm(self, driver):
        facebook_dm_filter = driver.find_element_by_id("media-facebook-dm")
        facebook_dm_filter.click()
        filtrele_button = driver.find_element_by_xpath("//a[@class='search-by-query button']")
        filtrele_button.click()
        for page in range(0, 2):
            posts = driver.find_elements_by_xpath("//div[@class='post-icons clearfix']/div[@class='post-icon'][1]/span")
            for post in posts:
                classname=post.get_attribute("class")
            nextpage = driver.find_element_by_xpath("//div[@id='pagination']//a[@class='page-link next']")
            nextpage.click()
            if 'source-icon icon-facebook' or 'source-icon icon-facebook_page_comment' in classname:
                face = 1
            else:
                face = 0
                break
        Test.printhandle(self, "facebook Dm", str(face))

    def instagram(self, driver):
        instagram_filter = driver.find_element_by_id("media-instagram")
        instagram_filter.click()
        filtrele_button = driver.find_element_by_xpath("//a[@class='search-by-query button']")
        filtrele_button.click()
        for page in range(0, 2):
            posts = driver.find_elements_by_xpath("//div[@class='post-icons clearfix']/div[@class='post-icon'][1]/span")
            for post in posts:
                classname=post.get_attribute("class")
            nextpage = driver.find_element_by_xpath("//div[@id='pagination']//a[@class='page-link next']")
            nextpage.click()
            if 'source-icon icon-instagram' or 'source-icon icon-instagram_comment' in classname:
                insta = 1
            else:
                insta = 0
                break

        Test.printhandle(self, "instagram", str(insta))


    def logoutControl(self, driver):
        logoutButton = driver.find_element_by_xpath("//div[@id='header-logout']/a")
        print(driver.title)
        logoutButton.click()



    def stat(self, driver):
        stats = driver.find_element_by_xpath("//ul[@id='items']/li[2]/a")
        stats.click()
        stats_page = driver.find_elements_by_class_name("box-header")
        if stats_page[0].text == 'SUMMARY' and stats_page[1].text == 'STATS' and stats_page[2].text == 'MOST TRENDING CATEGORIES AND ATTRIBUTES':
            Test.printhandle(self, "stat page", str(1))
        else:
            Test.printhandle(self, "stat page", str(0))

    # this function take test name and show right working or not .if it is error metric is 0 or is not 1
    def printhandle(self, name, metric):
        print (name+" : "+metric)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
