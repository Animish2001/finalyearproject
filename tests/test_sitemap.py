from page_object.sitemap_page import SiteMapPage
from utils.actions import Actions


class SiteMaptest(SiteMapPage):
    def setUp(self, masterqa_mode=False):
        super().setUp()
        print("running before each steps")

        # opening homepage
        Actions.access_app(self)

    def test_site_map_page(self):

        self.wait(10)
        self.click(SiteMapPage.accept)
        self.wait(10)
        self.click(SiteMapPage.pop_up)
        #sitemap from footer
        self.wait_for_element_clickable(SiteMapPage.sitemap)
        self.click(SiteMapPage.sitemap)

        #breadcrumb
        self.click(SiteMapPage.breadcrumb_home)
        self.go_back()

        #home
        self.wait_for_element_clickable(SiteMapPage.home)
        self.click(SiteMapPage.home)
        self.go_back()

        #products
        self.wait_for_element_clickable(SiteMapPage.products)
        self.click(SiteMapPage.products)
        self.go_back()

        #adult
        self.wait_for_element_clickable(SiteMapPage.adult)
        self.click(SiteMapPage.adult)
        self.go_back()

        #adult_prod_1
        self.wait_for_element_clickable(SiteMapPage.adult_prod_1)
        self.click(SiteMapPage.adult_prod_1)
        self.go_back()

        #adult_prod_2
        self.wait_for_element_clickable(SiteMapPage.adult_prod_2)
        self.click(SiteMapPage.adult_prod_2)
        self.go_back()

        #adult_prod_3
        self.wait_for_element_clickable(SiteMapPage.adult_prod_3)
        self.click(SiteMapPage.adult_prod_3)
        self.go_back()

        #adult_prod_3
        self.wait_for_element_clickable(SiteMapPage.adult_prod_4)
        self.click(SiteMapPage.adult_prod_4)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.kids)
        self.click(SiteMapPage.kids)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.kids_prod_1)
        self.click(SiteMapPage.kids_prod_1)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.kids_prod_2)
        self.click(SiteMapPage.kids_prod_2)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.kids_prod_3)
        self.click(SiteMapPage.kids_prod_3)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.kids_prod_4)
        self.click(SiteMapPage.kids_prod_4)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical)
        self.click(SiteMapPage.topical)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical_prod_1)
        self.click(SiteMapPage.topical_prod_1)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical_prod_2)
        self.click(SiteMapPage.topical_prod_2)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical_prod_3)
        self.click(SiteMapPage.topical_prod_3)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical_prod_4)
        self.click(SiteMapPage.topical_prod_4)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.topical_prod_5)
        self.click(SiteMapPage.topical_prod_5)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.benadryl_diff)
        self.click(SiteMapPage.benadryl_diff)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.compare_ben)
        self.click(SiteMapPage.compare_ben)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.ben_use)
        self.click(SiteMapPage.ben_use)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.our_ingre)
        self.click(SiteMapPage.our_ingre)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.about)
        self.click(SiteMapPage.about)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.faq)
        self.click(SiteMapPage.faq)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.safety)
        self.click(SiteMapPage.safety)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.dosing_guide)
        self.click(SiteMapPage.dosing_guide)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_1)
        self.click(SiteMapPage.allergy_1)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_2)
        self.click(SiteMapPage.allergy_2)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_3)
        self.click(SiteMapPage.allergy_3)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_4)
        self.click(SiteMapPage.allergy_4)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_5)
        self.click(SiteMapPage.allergy_5)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_6)
        self.click(SiteMapPage.allergy_6)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_7)
        self.click(SiteMapPage.allergy_7)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_8)
        self.click(SiteMapPage.allergy_8)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.allergy_9)
        self.click(SiteMapPage.allergy_9)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.itchy_skin)
        self.click(SiteMapPage.itchy_skin)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.itchy_skin_1)
        self.click(SiteMapPage.itchy_skin_1)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.itchy_skin_2)
        self.click(SiteMapPage.itchy_skin_2)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.cold)
        self.click(SiteMapPage.cold)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.savings)
        self.click(SiteMapPage.savings)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.contact_us)
        self.click(SiteMapPage.contact_us)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.legal)
        self.click(SiteMapPage.legal)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.terms)
        self.click(SiteMapPage.terms)
        self.go_back()

        self.wait_for_element_clickable(SiteMapPage.where_to_buy)
        self.click(SiteMapPage.where_to_buy)
        self.go_back()






