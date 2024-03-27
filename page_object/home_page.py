
from utils import *
from utils.actions import Actions


class HomePage(Actions):
    logo_icon = '.bi-benadryl-logo'
    learn_more_about_benadryl='benadryl-difference'
    adult_oral_link="//a[@href='https://www.benadryl.com/products/adult-oral' and contains(text(), 'Adult Oral')]"
    adult_topical_link="//a[@href='https://www.benadryl.com/products/adult-topical' and contains(text(), 'Adult Topical')]"
    kids_product_link="//a[@href='https://www.benadryl.com/products/kids' and contains(text(), 'Kid’s Products')]"
    best_seller_product_one="//a[@id=node-title-url-251]"
    best_seller_product_second = "//a[@id=node-title-url-246]"
    best_seller_product_third = "//a[@id=node-title-url-351]"
    best_seller_product_fourth="//a[@id='node-title-url-256']"
    slick_dots="//button[@id='slick-slide-control01']"
    related_content_1="//a[@class='arrow-link']"
    related_content_2="//a[@class='arrow-link' and @href='/cold/cold-or-allergies' and contains(text(), 'READ MORE')]"
    related_content_3="//a[@href='/allergies' and contains(text(), 'LEARN MORE')]"
    related_content_4 = "//a[@href='/childrens-allergies' and contains(text(), 'LEARN MORE')]"
    related_content_5 = "//a[@href='/itchy-skin' and contains(text(), 'LEARN MORE')]"
    more_on_benadryl_1="//a[@class='arrow-link' and @href='/faq' and contains(text(), 'VIEW ALL FAQS')]"
    more_on_benadryl_2 = "//a[@class='arrow-link' and @href='/safety' and contains(text(), 'VIEW OUR COMMITMENT TO SAFETY')]"
    footer="//div[@class='section-outer-wrapper']"





    def open_page(self):
        self.open("https://www.benadryl.com/")