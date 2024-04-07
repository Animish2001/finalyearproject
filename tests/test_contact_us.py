from page_object.contact_us import ContactUsPage
from utils.actions import Actions


class ContactUsTest(ContactUsPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_contact_us_page(self):
        self.wait(10)
        self.click(ContactUsPage.accept)
        self.wait(10)
        self.click(ContactUsPage.pop_up)
        self.click(ContactUsPage.contact_us)
