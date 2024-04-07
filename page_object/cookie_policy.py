from utils import *
from utils.actions import Actions


class CookiePolicyPage(Actions):
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    cookie_policy = "//li[@class='leaf menu-16991 cookiepolicy']/a[@href='/cookie-policy']"
