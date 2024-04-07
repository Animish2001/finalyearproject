from utils import *
from utils.actions import Actions


class SiteMapPage(Actions):
    sitemap="//li[@class='leaf menu-16841 sitemap']/a[@href='/sitemap']"
    breadcrumb_home="//a[@href='/']/span[text()='Home']"
    home="//li/a[text()='HOME']"
    products="//a[@href='/products' and contains(text(), 'PRODUCTS')]"
    adult="(//a[@href='/products/adult-oral' and contains(text(), 'Adult')])[2]"
    adult_prod_1="//li/a[@href='/products/benadryl-allergy-dye-free-liquigels' and contains(., 'BENADRYL® Allergy Relief Dye-Free LIQUI-GELS®')]"
    adult_prod_2="//li/a[@href='/products/benadryl-allergy-plus-congestion' and contains(., 'BENADRYL® Allergy Plus Congestion')]"
    adult_prod_3="//li/a[@href='/products/benadryl-allergy-ultratabs-tablets' and contains(., 'BENADRYL® Allergy ULTRATABS® Tablets')]"
    adult_prod_4="//li/a[@href='/products/benadryl-extra-strength-allergy-ultratabs' and contains(., 'BENADRYL® Extra Strength Allergy Relief ULTRATABS® Tablets')]"
    kids="//li/a[@href='/products/kids' and contains(., 'Kids')]"
    kids_prod_1="//li/a[@href='/products/childrens-benadryl-dye-free-allergy-liquid' and contains(., 'Children’s BENADRYL® Allergy Relief Liquid Medicine')]"
    kids_prod_2="//li/a[@href='/products/childrens-benadryl-allergy-plus-congestion' and contains(., 'Children’s BENADRYL® Allergy Plus Congestion')]"
    kids_prod_3="//li/a[@href='/products/childrens-benadryl-dye-free-allergy-liquid' and contains(., 'Children’s BENADRYL® Dye-Free Allergy Liquid')]"
    kids_prod_4="//li/a[@href='/products/childrens-benadryl-chewables' and contains(., 'Children’s BENADRYL® Chewables')]"
    accept = "//button[@id='onetrust-accept-btn-handler']"
    pop_up = "//button[@class='close sfmc-careclub-lightbox-close']"
    topical="(//a[contains(text(), 'Topical')])[2]"
    topical_prod_1="//li/a[@href='/products/benadryl-extra-strength-itch-relief-stick' and contains(., 'BENADRYL® Extra Strength Itch Relief Stick')]"
    topical_prod_2="//li/a[@href='/products/benadryl-extra-strength-spray' and contains(., 'BENADRYL® Extra Strength Spray')]"
    topical_prod_3="//li/a[@href='/products/benadryl-itch-stopping-gel-extra-strength' and contains(., 'BENADRYL® Itch Stopping Gel Extra Strength')]"
    topical_prod_4="//li/a[@href='/products/extra-strength-benadryl-itch-stopping-cream' and contains(., 'BENADRYL® Extra Strength Itch Stopping Cream')]"
    topical_prod_5="//li/a[@href='/products/original-strength-benadryl-itch-stopping-cream' and contains(., 'Original Strength BENADRYL® Itch Stopping Cream')]"
    benadryl_diff="//li/a[@href='/benadryl-difference' and contains(., 'BENADRYL DIFFERENCE')]"
    compare_ben="(//li/a[@href='/benadryl-difference/compare-allergy-relief-products' and contains(., 'Compare Benadryl')])[2]"
    ben_use="(//li/a[@href='/benadryl-difference/uses-indications' and contains(., 'Benadryl Uses')])[2]"
    our_ingre="(//li/a[@href='/benadryl-difference/ingredients-transparency' and contains(., 'Our Ingredients')])[2]"
    about="//li/a[@href='/benadryl-difference/diphenhydramine-active-ingredient' and contains(., 'About Diphenhydramine HCl: The Active Ingredient in BENADRYL®')]"
    faq="(//li/a[@href='/faq' and contains(., 'FAQ')])[2]"
    safety="(//li/a[@href='/safety' and contains(., 'Safety Information')])[2]"
    dosing_guide="//li/a[@href='/benadryl-dosing-guide' and contains(., 'DOSING GUIDE')]"
    allergy_1="//li/a[@href='/allergies' and contains(., 'Allergies 101: All About Allergies and How to Treat Them')]"
    allergy_2="//li/a[@href='/allergies/sore-itchy-throat' and contains(., 'Are Allergies Causing Your Itchy, Sore Throat?')]"
    allergy_3="//li/a[@href='/allergies/seasonal-vs-year-round' and contains(., 'When Is Allergy Season? Seasonal vs. Year-Round Allergies')]"
    allergy_4="//li/a[@href='/allergies/pet-allergy-symptoms-relief' and contains(., 'Dog & Cat Allergies: How to Manage Pet Allergy Symptoms')]"
    allergy_5="//li/a[@href='/allergies/treatment-and-prevention' and contains(., 'Tips and Remedies to Treat, Prevent, and Manage Allergy Symptoms')]"
    allergy_6="//li/a[@href='/allergies/outdoor-allergy-tips' and contains(., 'Outdoor Allergy Tips for Symptom Relief')]"
    allergy_7="//li/a[@href='/allergies/indoor-allergy-tips' and contains(., 'Indoor Allergy Tips to Help Relieve Symptoms at Home')]"
    allergy_8="//li/a[@href='/allergies/night-time-allergy-tips' and contains(., 'Allergies at Night and How to Relieve Night Time Symptoms')]"
    allergy_9="//li/a[@href='/allergies/allergy-symptoms-common-causes' and contains(., 'Allergy Symptoms and Common Causes of Allergic Reactions')]"
    itchy_skin="//li/a[@href='/itchy-skin' and contains(., 'Understanding Itchy Skin (Pruritus)')]"
    itchy_skin_1="//li/a[@href='/itchy-skin/relief-prevent-skin-itching-tips' and contains(., 'Itchy Skin Relief: Tips to Stop and Prevent Skin Itching')]"
    itchy_skin_2="//li/a[@href='/itchy-skin/poison-ivy-oak-sumac-rashes-symptoms-relief' and contains(., 'Poison Ivy, Oak, and Sumac Rashes: Symptoms and Treatments')]"
    cold="//li/a[@href='/cold/cold-or-allergies' and contains(., 'Is It a Cold or Allergies? Find Out What’s Causing Your Symptoms')]"
    savings="//li/a[@href='/save-on-benadryl' and contains(., 'SAVINGS')]"
    contact_us="//li/a[@href='/contact-us' and contains(., 'CONTACT US')]"
    legal="//li/a[@href='/legal' and contains(., 'LEGAL NOTICE')]"
    terms="//li/a[@href='/bv_terms_of_use' and contains(., 'TERMS OF USE')]"
    where_to_buy="//li/a[@href='/where-to-buy' and contains(., 'WHERE TO BUY')]"








