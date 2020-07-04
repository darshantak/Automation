# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:59:43 2020

@author: User
"""

from selenium import webdriver
import pandas as pd
browser=webdriver.Chrome()

company_array=[]
names_array=[]
address_array=[]
mobile_no_array=[]
email_id_array=[]


browser.delete_all_cookies()
browser.get('http://www.vkiassociation.com/associationmember.php')
    #these are the lists access them by indexing

company="//td[@class='sorting_1']/div/div/h4"
names="//td[@class='sorting_1']/div/div[@class='col-md-12']"
address="//i[@class='fa fa-map-marker']/.."
mobile_no="//i[@class='fa fa-mobile']/.."
email_id="//i[@class='fa fa-envelope']/.."

    
entries="//select[@name='example3_length']/option[@value='100']"
browser.find_element_by_xpath(entries).click()

for _ in range(1):
    
    company_selector=browser.find_elements_by_xpath(company)
    array1=[company_selector[i].text for i in range(14)]
    company_array.append(array1)
    
    names_selector=browser.find_elements_by_xpath(names)
    array2=[names_selector[i].text for i in range(14)]
    names_array.append(array2)
    
    address_selector=browser.find_elements_by_xpath(address)
    array3=[address_selector[i].text for i in range(14)]
    address_array.append(array3)
    
    mobile_no_selector=browser.find_elements_by_xpath(mobile_no)
    array4=[mobile_no_selector[i].text for i in range(14)]
    mobile_no_array.append(array4)
    
    email_id_selector=browser.find_elements_by_xpath(email_id)
    array5=[email_id_selector[i].text for i in range(14)]
    email_id_array.append(array5)
        
    next_page="//div[@class='dataTables_paginate paging_simple_numbers']/a[@id='example3_next']"
    browser.find_element_by_xpath(next_page).click()


company_array_final=[]
names_array_final=[]
address_array_final=[]
mobile_no_array_final=[]
email_id_array_final=[]

for i in company_array:
    for j in i:
        company_array_final.append(j)
        
        
for i in names_array:
    for j in i:
        names_array_final.append(j)
        
        
for i in address_array:
    for j in i:
        address_array_final.append(j)
        
for i in mobile_no_array:
    for j in i:
        mobile_no_array_final.append(j)
        
        
for i in email_id_array:
    for j in i:
        email_id_array_final.append(j)
        
len(set(mobile_no_array_final))
    
data={'Company Name':company_array_final,'Name':names_array_final,
      'Address':address_array_final,
      'Mobile No':mobile_no_array_final,'Email-Id':email_id_array_final}

df=pd.DataFrame(data)
df.to_excel('New3.xlsx')

