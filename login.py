

class LoginForm(object):
    def __init__(self, browser, **kwargs):
        self.browser = browser
        self.login_form = self.browser.find_element_by_id("login-form")
        self.username_field = self.login_form.find_element_by_id("id_username")
        self.password_field = self.login_form.find_element_by_id("id_password")


    def login(self, username, password):

        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_form.submit()


