from selenium import webdriver
import pandas as pd 

browser=webdriver.Chrome()

browser.delete_all_cookies()
browser.get("https://www.justdial.com/Jaipur/Architects/nct-10020039")

# dic={
#     "icon-dc":"+",
#     "icon-fe":"("
#     "icon-ji":""
# }

content="//span[@class='mobilesv icon-ji']"
test=browser.find_element_by_xpath(content)
content_selector=browser.find_elements_by_xpath(content)
test.value_of_css_property('margin')
x="return window.getComputedStyle(document.querySelector('.icon-ji'), ':before').getPropertyValue('content')"

y=browser.execute_script(x)

companies="//div[@class=' col-sm-5 col-xs-8 store-details sp-detail paddingR0']"
company_name="//p[@class='contact-info ']/span/a/b/../../../../h2/span/a/span"

companies_selector=browser.find_elements_by_xpath(companies)
company_name_list=[]

company_name_selector=browser.find_elements_by_xpath(company_name)
array1=[company_name_selector[i].text for i in range(len(company_name_selector))]

phone="//div[@class=' col-sm-5 col-xs-8 store-details sp-detail paddingR0']/p[@class='contact-info ']/span/a/b"

phone_selector=browser.find_elements_by_xpath(phone)

child_no="return document.getElementByClassName('contact-info ').childNodes"
yz=browser.execute_script(child_no)

import re
dic={"mobilesv icon-dc":"+",
"mobilesv icon-ji":"(",
"mobilesv icon-hg":")",
"mobilesv icon-acb":"0",
"mobilesv icon-yz":"1",
"mobilesv icon-wx":"2",
"mobilesv icon-vu":"3",
"mobilesv icon-ts":"4",
"mobilesv icon-rq":"5",
"mobilesv icon-po":"6",
"mobilesv icon-nm":"7",
"mobilesv icon-lk":"8",
"mobilesv icon-ji":"9",
"mobilesv icon-ba":"-"
}
number_list=[]
for i in range(len(array1)):
    get_attr=phone_selector[i].get_attribute("innerHTML")
    test_list=re.findall(r'"(.*?)"',get_attr)
    temp=""
    for j in test_list:
        temp=temp+dic[j]
    number_list.append(temp)





data={'Company Name':array1,"Contact No.":number_list}
df=pd.DataFrame(data)
df.to_excel('JustDial.xlsx')