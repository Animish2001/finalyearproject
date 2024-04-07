from page_object.legal_notice import LegalNoticePage
from utils.actions import Actions


class LegalNoticeTest(LegalNoticePage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_legal_notice_page(self):
        self.wait(10)
        self.click(LegalNoticePage.accept)
        self.wait(10)
        self.click(LegalNoticePage.pop_up)
        self.click(LegalNoticePage.legal_notice)
