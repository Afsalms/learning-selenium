

class ListingPage(object):
    
    def __init__(self, browser, **kwargs):
        self.browser = browser


    def redirect_to_listing_page(self, x_path):
        model_link = self.browser.find_elements_by_xpath(x_path)
        model_link[0].click()


