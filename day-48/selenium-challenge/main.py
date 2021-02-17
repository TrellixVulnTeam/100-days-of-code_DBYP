from selenium import webdriver

chrome_driver_path = "/Users/admin/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_time = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_time:
#     print(time.text)

event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}
for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()
driver.quit()

