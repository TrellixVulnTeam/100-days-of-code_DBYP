from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

########## WIKIPEDIA ##########
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


########## SIGNING UP FOR APP BREWERY NEWSLETTER ##########
driver.get("http://secure-retreat-92358.herokuapp.com/")
firstname = driver.find_element_by_name("fName")
firstname.send_keys("Christina")
lastname = driver.find_element_by_name("lName")
lastname.send_keys("KANG")
email = driver.find_element_by_name("email")
email.send_keys("emailtome@email.com")
sendbtn = driver.find_element_by_css_selector("form button")
sendbtn.send_keys(Keys.ENTER)

# driver.close()
# driver.quit()

