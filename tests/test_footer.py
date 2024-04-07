# from seleniumbase import BaseCase
import pytest

from page_object.footer_page import FooterPage
from utils.actions import Actions


class FooterTest(FooterPage):

    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_footer_page(self):
        # self.open("https://www.benadryl.com/")

        # company information

        # benadryl advantage
        self.wait_for_element_clickable(FooterPage.benadryl_advan)
        self.click(FooterPage.benadryl_advan)
        self.go_back()

        # contact us
        self.wait_for_element_clickable(FooterPage.contact_us)
        self.click(FooterPage.contact_us)
        self.go_back()

        # self.wait_for_element_clickable("//a[@class='no-ext ext' and contains(text(), 'Johnson & Johnson Brands')]")
        # self.click("//a[@class='no-ext ext' and contains(text(), 'Johnson & Johnson Brands')]")
        # self.go_back()

        # product information

        # products
        self.wait_for_element_clickable(FooterPage.products)
        self.click(FooterPage.products)
        self.go_back()

        # dosing guide
        self.wait_for_element_clickable(FooterPage.dosing_guide)
        self.click(FooterPage.dosing_guide)
        self.go_back()

        # faqs
        self.wait_for_element_clickable(FooterPage.faqs)
        self.click(FooterPage.faqs)
        self.go_back()

        # savings
        self.wait_for_element_clickable(FooterPage.savings)
        self.click(FooterPage.savings)
        self.go_back()

        # allergy & cold guide

        # allergies
        self.wait_for_element_clickable(FooterPage.allergies)
        self.click(FooterPage.allergies)
        self.go_back()

        # kids allergies
        self.wait_for_element_clickable(FooterPage.kids_allergies)
        self.click(FooterPage.kids_allergies)
        self.go_back()

        # cold or allergies?
        self.wait_for_element_clickable(
            FooterPage.cold_or_allergies)
        self.click(FooterPage.cold_or_allergies)
        self.go_back()

        # legal

        # #privacy policy
        # self.wait_for_element_clickable("//li[@class='first leaf menu-3026 privacypolicy']/a[@href='https://www.kenvue.com/privacy-policy/us']")
        # self.click("//li[@class='first leaf menu-3026 privacypolicy']/a[@href='https://www.kenvue.com/privacy-policy/us']")
        # self.close_window()

        # terms of use
        self.wait_for_element_clickable(FooterPage.terms_of_use)
        self.click(FooterPage.terms_of_use)
        self.go_back()

        # legal notice
        self.wait_for_element_clickable(FooterPage.legal_notice)
        self.click(FooterPage.legal_notice)
        self.go_back()

        # cookie policy
        self.wait_for_element_clickable(FooterPage.cookie_policy)
        self.click(FooterPage.cookie_policy)
        self.go_back()

        # customize cookie settings
        self.wait_for_element_clickable(FooterPage.customize_cookie_settings)
        self.click(FooterPage.customize_cookie_settings)
        #confirm_cookie
        self.click(FooterPage.confirm_cookie)

        # Limit the Use of my Sensitive Personal Information
        # self.wait_for_element_clickable("//li[@class='leaf menu-16996 limittheuseofmysensitivepersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        # self.click("//li[@class='leaf menu-16996 limittheuseofmysensitivepersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        # self.go_back()

        # sitemap
        self.wait_for_element_clickable(FooterPage.sitemap)
        self.click(FooterPage.sitemap)
        self.go_back()

        #paragraph
        self.find_elements(FooterPage.paragraph)


        # social media icons

        # facebook
        # self.click("//a[@href='https://www.facebook.com/benadryl']")
        #
        # # twitter
        # self.click("//a[@href='https://twitter.com/benadryl']")
        #
        # # youtube
        # self.click("//a[@href='https://www.youtube.com/user/BenadrylOfficial']")

    def close_window(self):
        # privacy policy
        self.wait_for_element_clickable(
            "//li[@class='first leaf menu-3026 privacypolicy']/a[@href='https://www.kenvue.com/privacy-policy/us']")
        self.click(
            "//li[@class='first leaf menu-3026 privacypolicy']/a[@href='https://www.kenvue.com/privacy-policy/us']")
        self.close_window()

        # Limit the Use of my Sensitive Personal Information
        self.wait_for_element_clickable(
            "//li[@class='leaf menu-16996 limittheuseofmysensitivepersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        self.click(
            "//li[@class='leaf menu-16996 limittheuseofmysensitivepersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        self.close_window()

        # ad choices
        self.wait_for_element_clickable(
            "//li[@class='leaf menu-15106 adchoices']/a[@href='https://www.kenvue.com/privacy-policy/us#internet-based-advertising']")
        self.click(
            "//li[@class='leaf menu-15106 adchoices']/a[@href='https://www.kenvue.com/privacy-policy/us#internet-based-advertising']")
        self.close_window()

        # Do Not Sell or Share My Personal Information
        self.wait_for_element_clickable(
            "//li[@class='leaf menu-15111 donotsellorsharemypersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        self.click(
            "//li[@class='leaf menu-15111 donotsellorsharemypersonalinformation']/a[@href='https://privacyportal-cdn.onetrust.com/dsarwebform/96f23ee1-34e3-41d6-8d5a-07f0d554152b/83bc2fd2-1604-4e64-93e5-2670b01de08b.html?WebsiteName=www.benadryl.com']")
        self.close_window()

        # canadian resident
        self.wait_for_element_clickable(
            "//li[@class='last leaf menu-16821 canadianresidents']/a[@href='https://www.benadryl.ca/?_gl=1*1uveyhs*_ga*MTcxMjI2NzIyMi4xNzEyNDc0NDcz*_ga_13VEM6N66E*MTcxMjQ3NDQ3My4xLjEuMTcxMjQ3Njg2Ni4wLjAuMTM4ODc5ODgwMw..*_fplc*blBpSHp3WHlpT1BtNyUyQkNkTG13UUhENENFMlV4dGU4SlNMT1g3ZW1CNU13N2MwTDdrdlhsOEFqd3F0RHMyYXR6ejNRRFhwRzNGeWp0RndzR3Z1JTJCa21iYUl4OWdlRyUyRkp3b241Q0RhaktvSHNkbE1jUWowZVA3MGFEU1hCMGV3JTNEJTNE']")
        self.click(
            "//li[@class='last leaf menu-16821 canadianresidents']/a[@href='https://www.benadryl.ca/?_gl=1*1uveyhs*_ga*MTcxMjI2NzIyMi4xNzEyNDc0NDcz*_ga_13VEM6N66E*MTcxMjQ3NDQ3My4xLjEuMTcxMjQ3Njg2Ni4wLjAuMTM4ODc5ODgwMw..*_fplc*blBpSHp3WHlpT1BtNyUyQkNkTG13UUhENENFMlV4dGU4SlNMT1g3ZW1CNU13N2MwTDdrdlhsOEFqd3F0RHMyYXR6ejNRRFhwRzNGeWp0RndzR3Z1JTJCa21iYUl4OWdlRyUyRkp3b241Q0RhaktvSHNkbE1jUWowZVA3MGFEU1hCMGV3JTNEJTNE']")
        self.close_window()
