from utils import *
from utils.actions import Actions


class ContactUsPage(Actions):
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    contact_us = "//a[text()='Contact Us']"
