# importing selenium

from page_object.home_page import HomePage
from utils.actions import Actions


class HomeTest(HomePage):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

        HomePage.open_page(self)

    def test_home_page(self):
        # for loading the page
        # self.page_load_strategy()

        # self.open("https://www.benadryl.com/")
        # self.wait(30)

        # assert page title
        # self.assert_title("Allergy & Itch Relief Medicine for Adults & Children | BENADRYL®")

        # assert logo(optional)
        self.assert_element(HomePage.logo_icon)

        # homepage text

        #
        # click on get started button and assert the url
        self.click(HomePage.learn_more_about_benadryl)  # x-path locator"//a[@class='btn btn-secondary-inverted']"
        # $$("a[class='btn btn-secondary-inverted']") css selector
        # learn_more_about_benadryl_url=self.get_current_url() # it will store the value as string in learn_more_url variable
        # self.assert_equal(learn_more_about_benadryl_url,"https://www.benadryl.com/benadryl-difference")
        # self.assert_true("benadryl-difference" in learn_more_about_benadryl_url) #verifying if the get-started is working properly(partial verification)
        # self.go_back()

        # self.wait_for_text_not_visible("//a[@href='/products' and contains(text(), 'VIEW ALL BENADRYL® PRODUCTS'")
        # self.click("//a[@href='/products' and contains(text(), 'VIEW ALL BENADRYL® PRODUCTS'")
        # self.go_back()

        #######
        # xpath for view all products link
        # $x("//a[@href='/products']")
        #######

        # under view all benadryl products
        # expected_url=['Adult Oral','Adult Topical','Kid’s Products']
        # product_link=self.find_elements("//*[starts-with(@class, 'field-item even')]")
        #
        # for idx, link_el in enumerate(product_link):
        #     self.assertEqual(expected_url[idx],link_el.text)
        # node - title - url - 256

        # VIEW ALL BENADRYL® PRODUCTS
        # self.wait_for_element_clickable("//a[@href='/childrens-allergies' and contains(text(), 'VIEW ALL BENADRYL® PRODUCTS')]")
        # self.click("//a[@href='/childrens-allergies' and contains(text(), 'VIEW ALL BENADRYL® PRODUCTS')]")
        # self.go_back()

        # Adult Oral
        self.wait_for_element_clickable(HomePage.adult_oral_link)
        self.click(HomePage.adult_oral_link)
        self.go_back()

        # Adult Topical
        self.wait_for_element_clickable(HomePage.adult_oral_link)
        self.click(HomePage.adult_topical_link)
        self.go_back()

        # Kid’s Products
        self.wait_for_element_clickable(HomePage.kids_product_link)
        self.click(HomePage.kids_product_link)
        self.go_back()
        #
        #
        #
        # best seller
        ids_to_click = ['node-title-url-251', 'node-title-url-246', 'node-title-url-351']

        for id_to_click in ids_to_click:
            self.click(f"//a[@id='{id_to_click}']")
            self.go_back()
        #
        # # self.click("//li[@class='slick-active']")
        # slick_dots
        self.wait_for_element_clickable(HomePage.slick_dots)
        self.click(HomePage.slick_dots)

        # last product from best seller
        self.click(HomePage.best_seller_product_fourth)
        self.go_back()
        #
        #
        #
        #
        # RELATED CONTENT
        self.click(HomePage.related_content_1)
        self.go_back()

        self.click(HomePage.related_content_2)
        self.go_back()
        #
        self.wait_for_element_clickable(HomePage.related_content_3)
        self.click(HomePage.related_content_3)
        self.go_back()

        self.wait_for_element_clickable(HomePage.related_content_4)
        self.click(HomePage.related_content_4)
        self.go_back()

        self.wait_for_element_clickable(HomePage.related_content_5)
        self.click(HomePage.related_content_5)
        self.go_back()
        # # links = [
        # #     "//a[@class='arrow-link']",
        # #     "//a[@class='arrow-link' and @href='/cold/cold-or-allergies' and contains(text(), 'READ MORE')]",
        # #     "//a[@href='/allergies' and contains(text(), 'LEARN MORE')]",
        # #     "//a[@href='/childrens-allergies' and contains(text(), 'LEARN MORE')]",
        # #     "//a[@href='/itchy-skin' and contains(text(), 'LEARN MORE')]"
        # # ]
        # #
        # # for link in links:
        # #     self.wait_for_element_clickable(link)
        # #     self.click(link)
        # #     self.go_back()
        #
        # More on BENADRYL®
        self.click(HomePage.more_on_benadryl_1)
        self.go_back()

        self.click(HomePage.more_on_benadryl_2)
        self.go_back()
        #
        #
        #
        # FOOTER
        self.click(HomePage.footer)

        # title
        # self.click("//a[@id='node-title-url-251']")
        # self.go_back()

        # #ratings
        # self.click("//div[@class='bv-hosted-inline_v2']")
        # self.go_back()

        # #cta
        # self.click("//a[@class='ps-widget btn btn-primary btn-full ps-639ce389ebf290000d8c28f8 ps-enabled']")
        # self.go_back()

        # self.click("//a[@id='node-title-url-246']")
        # self.go_back()
        #
        #
        # self.click("//a[@id='node-title-url-351']")
        # self.go_back()
        #
        # self.click("//a[@id='node-title-url-256']")
        # self.go_back()

        # header present
        # self.click("//div[@class='header-flex']")

        # self.assert_title("Our Products")

        # wait for the element to be present
        # self.wait_for_element_present("link_text: VIEW ALL BENADRYL® PRODUCTS")

        # self.click('xpath://a[@href="/products"]')
        # self.click('//a[contains(@href, "/products") and contains("VIEW ALL BENADRYL® PRODUCTS")]')

        # pending view all benadrylproducts
        # self.click("//div[@class='our-products-title']/h2/p/a[@href='/products']")
        # view_all_benadryl_url=self.get_current_url()
        # self.assert_equal(view_all_benadryl_url,"https://www.benadryl.com/products")
        # self.assert_true("products" in view_all_benadryl_url)

        # code for view all benadryl products
        # self.click_link_text(link_text="VIEW ALL BENADRYL® PRODUCTS")

    def tearDown(self):
        print("running after each steps")
        super().tearDown()

    #
    #     #get the text of the header and assert the value
    #     self.assert_text(" Relief You Can Trust","h1")
    #
    #     #exercise: scroll to bottom and assert the copyright text
    #     # self.assert_text("Copyright © 2020" ,"p")
    #     # self.assert_link_text("SDET Unicorns") tried myself
    #
    # self.scroll_to_bottom()
    # self.assert_text("Copyright © 2020 SDET Unicorns",".zak-footer-bar__1")
    #
    # def test_menu_links(self):
    #
    #     expected_links=['Home','About','Shop','Blog','Contact','My account','Home','About','Blog','Contact','Support Form']
    #     #open url
    #     self.open("https://practice.sdetunicorns.com/")
    #
    #     # find menu links elements
    #     menu_links_el=self.find_elements("//*[starts-with(@id,'menu-item')]")#finding multiple elements
    #     # li[id *= menu - item] -> css selector
    #     # //*[starts-with(@id, 'menu-item')] -> xpath
    #     # -k means running only the selected function
    #     # -s means running only elements
    #
    #     # loop through our menu links
    #     for idx,link_el in enumerate(menu_links_el):
    #         # print(idx,link_el.text)#we are using .text to get text value from the element
    #         #printing out only text from the <li> tag
    #         self.assertEqual(expected_links[idx], link_el.text)
    #

    # header of benadryl
    # self.click("//a[@id='tab-menu-8651']")
