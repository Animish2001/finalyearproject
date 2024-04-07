from utils import *
from utils.actions import Actions


class FooterPage(Actions):
    benadryl_advan="//a[text()='The Benadryl Advantage']"
    contact_us="//a[text()='Contact Us']"
    products="(//a[@href='/products'])[4]"
    dosing_guide="(//a[@href='/benadryl-dosing-guide'])[3]"
    faqs="//li[@class='leaf menu-15081 faqs']/a[@href='/faq']"
    savings="//li[@class='last leaf menu-15086 savings']/a[@href='/save-on-benadryl']"
    allergies="//li[@class='first leaf menu-3016 allergies']/a[@href='/allergies']"
    kids_allergies="//li[@class='leaf menu-15096 kidsallergies']/a[@href='/childrens-allergies']"
    cold_or_allergies="//li[@class='last leaf menu-18466 coldorallergies']/a[@href='/cold/cold-or-allergies']"
    terms_of_use="//li[@class='leaf menu-3031 termsofuse']/a[@href='/bv_terms_of_use']"
    legal_notice="//li[@class='leaf menu-16826 legalnotice']/a[@href='/legal']"
    cookie_policy="//li[@class='leaf menu-16991 cookiepolicy']/a[@href='/cookie-policy']"
    customize_cookie_settings="//span[@class='optanon-show-settings nolink']"
    confirm_cookie="//button[@class='save-preference-btn-handler onetrust-close-btn-handler']"
    sitemap="//li[@class='leaf menu-16841 sitemap']/a[@href='/sitemap']"
    paragraph="//p[.='© J&JCI 2023. All rights reserved. This site is published by Johnson & Johnson Consumer Inc., which is solely responsible for its contents. This website is intended for visitors from the U.S. This site contains links to websites to which our Privacy Policy does not apply. We encourage you to read the privacy policy of every website you visit. The third-party trademarks used herein are trademarks of their respective owners.']"
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"



