from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from login import LoginForm

opts = Options()
# opts.set_headless()
# assert opts.headless
browser = Firefox(options=opts)
browser.get('https://dhowberbackend.qburst.build/admin')

# login_form = browser.find_element_by_id('login-form')
# username_field = login_form.find_element_by_id("id_username")
# password_field = login_form.find_element_by_id("id_password")

# username_field.send_keys("+971-1234567890")
# password_field.send_keys("qburst123")
# login_form.submit()



# print(browser)
# print(dir(browser))

# print(browser.current_url)
# print("*****************************")
login_form = LoginForm(browser)
login_form.login("+971-1234567890", "qburst123")

import time
time.sleep(5)


account_status = browser.find_elements_by_xpath('/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[1]/th/a')

# print(dir(account_status[0]))
# print(account_status)
account_status[0].click()


time.sleep(5)

disabled_status = browser.find_elements_by_xpath('/html/body/div/div[3]/div/div/form/div/table/tbody/tr[1]/th/a')
disabled_status[0].click()


time.sleep(5)
text_input_form = browser.find_element_by_id('id_accountstatusl_set-3-text')
text_input_form.send_keys("automation text")

language_drop_down =browser.find_element_by_id('id_accountstatusl_set-3-language')
language_drop_down.location_once_scrolled_into_view

options = language_drop_down.find_elements_by_xpath('/html/body/div/div[3]/div/form/div/div[1]/div/fieldset/table/tbody/tr[4]/td[3]/div/select/option[4]')
options[0].click()



print(dir(language_drop_down))


submit_button_row = browser.find_elements_by_xpath('/html/body/div/div[3]/div/form/div/div[2]/input[1]')

submit_button_row[0].submit()




# print(dir(login_form))
# login_form.send_keys('real python')
# login_form.submit()

# results = browser.find_elements_by_class_name('result')

# print(results)
# print(dir(results))