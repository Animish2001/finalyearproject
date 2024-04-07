from utils import *
from utils.actions import Actions


class WhereToBuyPage(Actions):
    where_to_buy="//a[@class='wtb-btn no-arrow-hover']"
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
