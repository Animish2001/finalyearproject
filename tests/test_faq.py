from page_object.faq_page import FAQPage
from utils.actions import Actions


class FAQTest(FAQPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_contact_us_page(self):
        self.wait(10)
        self.click(FAQPage.accept)
        self.wait(10)
        self.click(FAQPage.pop_up)
        self.click(FAQPage.faq)
