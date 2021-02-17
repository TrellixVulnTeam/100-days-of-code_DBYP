from selenium import webdriver

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

########## AMAZON ##########
# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07WL1XBBD/ref=sr_1_1?qid=1597662463&th=1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

########## PYTHON ##########
driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()
driver.quit()