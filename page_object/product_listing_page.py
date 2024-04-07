from utils import *
from utils.actions import Actions


class ProductListingPage(Actions):
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    product_tab = "//a[@id='tab-menu-8651']"
    product_img_1="(//a[contains(@href, '/products/benadryl-allergy-ultratabs-tablets')])[5]"
    product_title_1="//span[@class='node__title']/a[@id='node-title-url-386']"
    product_ratings_1="//div/a[@id='66ac0f9a-13ce-4f24-9bdc-9ff9d6cdbd80']"
    # product_buy_now_1="//a[@class='ps-widget btn btn-primary btn-full ps-639ce389ebf290000d8c28f8 ps-enabled' and @href='https://www.benadryl.com/products/benadryl-allergy-ultratabs-tablets']"


