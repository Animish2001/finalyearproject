import pytest

from page_object.header_page import HeaderPage
from utils.actions import Actions


class HeaderTest(HeaderPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_header_page(self):
        # self.open("https://www.benadryl.com/")

        # assert logo
        self.click(HeaderPage.logo)

        self.click(HeaderPage.product_tab)

        # PLP
        self.click(HeaderPage.product_one)
        # self.click("//button[contains(@aria-label, 'Write a Review')]")
        # button
        # self.click("//button[@class='ps-widget btn btn-primary btn-full ps-639ce389ebf290000d8c28f8 ps-enabled']")
        # see all ingredients
        # self.click("//button[@class='pdp-see-full-ingredients btn btn-primary btn-full']")
        # # used for tab
        # self.click("//a[@id='tab_used-for']")
        # # warnings
        # self.click("//a[@id='tab_warnings']")
        # # additional
        # self.click("//a[@id='tab_additional-information']")
        #
        # self.click("(//button[@class='bv_button_buttonMinimalist bv_war_button '])")
        #
        # self.click("(//div[@class='bv_avgRating_component_container notranslate'])")
        self.go_back()

        self.click(HeaderPage.product_two)
        self.go_back()

        self.click(HeaderPage.product_three)
        self.go_back()

        # benadryl-difference
        self.click(HeaderPage.benadryl_diff)
        self.go_back()

        # dosing guide
        self.wait_for_element_clickable(
            HeaderPage.dosing_guide)
        self.click(HeaderPage.dosing_guide)
        self.go_back()

        # search
        # self.wait_for_element_present("//span[@class='header-search-btn nolink active' and contains(text(), 'Search')")
        # self.click("//span[@class='header-search-btn nolink active' and contains(text(), 'Search')']")
        # self.go_back()


        # savings
        self.wait_for_element_clickable(
            HeaderPage.savings)
        self.click(HeaderPage.savings)
        self.go_back()

        # where_to_buy
        self.wait_for_element_clickable(HeaderPage.where_to_buy)
        self.click(HeaderPage.where_to_buy)
        self.go_back()

        # email_rewards
        # self.wait_for_element_clickable("//a[contains(text(), 'Email Sign Up & Rewards') and @style='pointer-events: auto;']")
        # self.click("//a[contains(text(), 'Email Sign Up & Rewards') and @style='pointer-events: auto;']")
        # self.click("//button[@class='close sfmc-careclub-lightbox-close']")

        self.wait_for_element_clickable(HeaderPage.email_rewards)
        self.click(HeaderPage.email_rewards)
        # close
        self.click(HeaderPage.close)

        #

        # espanol
        self.click(HeaderPage.espanol)
        self.go_back()

        # verifying the header

    # def product_tab(self):
    #     self.click("//a[@id='tab-menu-8651']")
    #     self.go_back()

    # def benadryl_diff(self):
    #     self.click("//a[@href='https://www.benadryl.com/benadryl-difference' and contains(text(), 'Benadryl Difference')]")
    #     self.go_back()

    # submenus of header
    # self.wait_for_element_clickable("//a[@href='/products/adult-oral' and contains(text(), 'Adult')]")
    # self.click("//a[@href='/products/adult-oral' and contains(text(), 'Adult')]")
    # self.go_back()

    def benadryl_diff(self):
        self.click("")
