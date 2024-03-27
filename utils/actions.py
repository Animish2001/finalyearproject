from seleniumbase import BaseCase


class Actions(BaseCase):
    base_url = "https://www.benadryl.com/"

    def access_app(self):
        self.open(self.base_url)
        print('accessed url : ' + self.base_url)
