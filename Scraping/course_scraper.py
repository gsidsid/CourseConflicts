from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json

url = "https://my.olin.edu/ICS/Course_Schedules.jnz"

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
driver.implicitly_wait(100)
driver.execute_script(
    "document.getElementById('pg0_V_tabSearch_btnSearch').click()")
driver.implicitly_wait(100)
driver.execute_script("document.getElementById('pg0_V_lnkShowAll').click()")
driver.implicitly_wait(100)

a = []
b = driver.find_elements_by_class_name("alt")

course_codes_raw = []
course_times_raw = []

for el in b:
    s = el.find_elements_by_tag_name("td")
    try:
        print(s[1].text.split('-')[0])
        print(s[8].text)
        course_codes_raw.append(s[1].text.split('-')[0])
        course_times_raw.append(s[8].text)
    except BaseException:
        continue

print(str(len(course_codes_raw)))
print(str(len(course_times_raw)))

course_book = dict()

for i in range(len(course_codes_raw)):
    course = course_codes_raw[i]
    slot_raw = course_times_raw[i]
    slot_cln = ""
    slot_split = slot_raw.split(" ")
    slot_cln += slot_split[0]
    if slot_cln != "0:00" and len(slot_split) > 1:
        slot_cln += slot_split[1]
        course_book.setdefault(course, [])
        course_book[course].append(slot_cln.replace('AM', ''))

print(course_book)
with open('../Courses/course_book_scraped.json', 'w') as fp:
    json.dump(course_book, fp)
