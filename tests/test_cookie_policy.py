from page_object.cookie_policy import CookiePolicyPage
from utils.actions import Actions


class CookiePolicyTest(CookiePolicyPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_cookie_policy_page(self):
        self.wait(10)
        self.click(CookiePolicyPage.accept)
        self.wait(10)
        self.click(CookiePolicyPage.pop_up)
        self.click(CookiePolicyPage.cookie_policy)
