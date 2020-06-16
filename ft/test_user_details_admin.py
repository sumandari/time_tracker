from selenium import webdriver

from django.test import LiveServerTestCase


class AdminTest(LiveServerTestCase):
    """
    create test for admin page
    - create fixture from Terminal:
    $ python manage.py dumpdata auth.User --indent=2> ft/fixtures/admin.json
    """
    fixtures = ['ft/fixtures/admin.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_admin_site_login(self):
        # user with admin role, go to admin page and entry username and password
        self.browser.get(self.live_server_url + '/admin')
        self.browser.find_element_by_name('username').send_keys('admin')
        self.browser.find_element_by_name('password').send_keys('admin')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        # login credential is correct, redirected to main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Site administration', body.text)
        # user admin can see User link
        self.assertIn(u'User', body.text)
        # Profile link is not seen in main admin page since it's stackedinline
        assert u'Profile' not in body.text


        # admin click link user
        self.browser.find_element_by_link_text('Users').click()
        # admin should able to see all users
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'userstaff', body.text)
        self.assertIn(u'usertest', body.text)

    def test_admin_site_login_staff(self):
        # user with staff role, go to admin page and entry username and password
        self.browser.get(self.live_server_url + '/admin')
        self.browser.find_element_by_name('username').send_keys('userstaff')
        self.browser.find_element_by_name('password').send_keys('admin')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        # login credential is correct, redirected to main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Site administration', body.text)
        self.assertIn(u'You don’t have permission', body.text)

    def test_admin_site_login_non_staff(self):
        # user with non staff role, go to admin page and entry username and password
        self.browser.get(self.live_server_url + '/admin')
        self.browser.find_element_by_name('username').send_keys('usertest')
        self.browser.find_element_by_name('password').send_keys('admin')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()
        # login credential is correct, redirected to main admin page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn(u'Please enter the correct username and password', 
            body.text)
