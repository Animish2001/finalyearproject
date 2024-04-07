from utils import *
from utils.actions import Actions


class FAQPage(Actions):
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    faq = "//li[@class='leaf menu-15081 faqs']/a[@href='/faq']"
