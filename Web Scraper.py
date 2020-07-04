# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:59:43 2020

@author: User
"""
from selenium import webdriver
browser=webdriver.Chrome()

browser.get('https://www.pmar.in/my-page.php?cname=About%20Us&subname=PMAR%20Member&sname=Life%20Member')
#these are the lists access them by indexing
company="//div[@class='main']/div[@class='content full']/div[@class='container']/div[@class='page']/div[@class='row']/div[@class='col-md-12 col-sm-12']/table[@class='table  ']/tbody/tr/td/h5[@style='color:rgb(1, 40, 95);']"
names="//div[@class='main']/div[@class='content full']/div[@class='container']/div[@class='page']/div[@class='row']/div[@class='col-md-12 col-sm-12']/table[@class='table  ']/tbody/tr/td/h5[@style='font-size:14px; font-weight:100;']"
mobile_no="//div[@class='main']/div[@class='content full']/div[@class='container']/div[@class='page']/div[@class='row']/div[@class='col-md-12 col-sm-12']/table[@class='table  ']/tbody/tr/td/p"
add_email_id="//div[@class='main']/div[@class='content full']/div[@class='container']/div[@class='page']/div[@class='row']/div[@class='col-md-12 col-sm-12']/table[@class='table  ']/tbody/tr/td/p[@style='font-size:15px;']"

company_selector=browser.find_elements_by_xpath(company)
array1=[company_selector[i].text for i in range(1000)]
#company_array.append(array1)

names_selector=browser.find_elements_by_xpath(names)
array2=[names_selector[i].text for i in range(1000)]
#names_array.append(array2)

mobile_no_selector=browser.find_elements_by_xpath(mobile_no)
array4=[mobile_no_selector[i].text for i in range(1000)]
#mobile_no_array.append(array4)

email_id_selector=browser.find_elements_by_xpath(add_email_id)
array5=[email_id_selector[i].text for i in range(1000)]
#email_id_array.append(array5)


