from seleniumbase import HeaderPage

class HeaderTest(HeaderPage):



    def test_header_page(self):
        self.open("https://www.benadryl.com/")

        #assert logo
        self.assert_element(".bi-benadryl-logo")

        #verifying the header


    def product_tab(self):
        self.click("//a[@id='tab-menu-8651']")
        self.go_back()

        #submenus of header
        # self.wait_for_element_clickable("//a[@href='/products/adult-oral' and contains(text(), 'Adult')]")
        # self.click("//a[@href='/products/adult-oral' and contains(text(), 'Adult')]")
        # self.go_back()




