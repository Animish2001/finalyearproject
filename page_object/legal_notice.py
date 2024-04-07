from utils import *
from utils.actions import Actions


class LegalNoticePage(Actions):
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    legal_notice = "//li[@class='leaf menu-16826 legalnotice']/a[@href='/legal']"
