from page_object.product_listing_page import ProductListingPage
from utils.actions import Actions

class ProductListingPageTest(ProductListingPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_product_listing_page(self):
        self.wait(10)
        self.click(ProductListingPage.accept)
        self.wait(10)
        self.click(ProductListingPage.pop_up)
        self.click(ProductListingPage.product_tab)
        self.wait(10)
        self.click(ProductListingPage.product_img_1)
        self.go_back()
        self.click(ProductListingPage.product_title_1)
        self.go_back()
        self.click(ProductListingPage.product_ratings_1)
        self.go_back()
        # self.click(ProductListingPage.product_buy_now_1)
        self.go_back()

