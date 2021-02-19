from selenium import webdriver
import time

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:
        cookie_upgrades = {}
        items = driver.find_elements_by_css_selector("#store div")
        for item in items[:-1]:
            item_element = item.text
            item_name_price = item_element.split("\n")[0]
            item_name = item_name_price.split(" - ")[0]
            item_price = int(item_name_price.split(" - ")[1].strip().replace(",", ""))
            cookie_upgrades[item_price] = item_name

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        # print(cookie_count)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, item in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = item
        # print(affordable_upgrades)

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5


#After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break