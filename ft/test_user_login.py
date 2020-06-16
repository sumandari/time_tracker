from selenium import webdriver

from django.test import LiveServerTestCase


class UserLoginTest(LiveServerTestCase):
    """
    create test for login page
    - create fixture from Terminal:
    $ python manage.py dumpdata auth.User --indent=2> ft/fixtures/admin.json
    $ python manage.py dumpdata user_details.Profile --indent=2> ft/fixtures/userprofile.json
    """
    fixtures = ['ft/fixtures/admin.json', 'ft/fixtures/userprofile.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login_page(self):
        # user  go to login page
        self.browser.get(self.live_server_url + '/accounts/login')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Login', body.text)
        # user entry username and password
        self.browser.find_element_by_name('username').send_keys('admin')
        self.browser.find_element_by_name('password').send_keys('admin')
        self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        # login credential is correct, redirected to main admin page
        # body = self.browser.find_element_by_tag_name('body')
        # self.assertIn(u'Home', body.text)