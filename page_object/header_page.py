# from seleniumbase import BaseCase
from utils.actions import Actions

class HeaderPage(Actions):
    logo=".bi-benadryl-logo"
    product_tab = "//a[@id='tab-menu-8651']"
    product_one="(//a[@id='node-title-url-386'])[5]"
    product_two="(//a[@id='node-title-url-256'])[5]"
    product_three="(//a[@id='node-title-url-371'])[5]"
    benadryl_diff = "//a[@href='/benadryl-difference' and contains(text(), 'Benadryl Difference')]"
    dosing_guide="//a[@href='/benadryl-dosing-guide' and @role='menuitem' and contains(text(), 'Dosing Guide')]"
    savings="//a[@href='/save-on-benadryl' and @role='menuitem' and contains(text(), 'Savings')]"
    where_to_buy="//a[@class='wtb-btn no-arrow-hover']"
    email_rewards="(//a[@href='#' and @style='pointer-events: auto;'])[1]"
    espanol="(//a[@class='no-ext mp-global-switch user-locale ext jquery-once-10-processed'])[1]"
    close="//button[@class='close sfmc-careclub-lightbox-close']"
