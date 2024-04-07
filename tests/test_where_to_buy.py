from page_object.where_to_buy_page import WhereToBuyPage
from utils.actions import Actions


class WhereToBuyTest(WhereToBuyPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_where_to_buy_page(self):
        self.wait(10)
        self.click(WhereToBuyPage.accept)
        self.wait(10)
        self.click(WhereToBuyPage.pop_up)
        self.click(WhereToBuyPage.where_to_buy)
