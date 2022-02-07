from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
from InstagramAPI import InstagramAPI
from instapy_cli import client
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from random import randint
from time import sleep

EmailList = pd.read_excel('Marketplacesellingdata.xlsx', sheet_name = 'Item1', engine='openpyxl')
EmailList1 = pd.read_excel('Marketplacesellingdata.xlsx', sheet_name = 'Item2', engine='openpyxl')
EmailList2 = pd.read_excel('Marketplacesellingdata.xlsx', sheet_name = 'Item3', engine='openpyxl')



def optionpicker(browser, choose_option):

    if choose_option == '1':
        print('You choosed 1')
        productitem1(browser)

    elif choose_option == '2':
        print('You choosed 2')
        productitem2(browser)

    elif choose_option == '3':
        print('You choosed 3')

        productitem3(browser)

    elif choose_option == 'all':
        print('You choosed all')
        productitem1(browser)
        time.sleep(3)
        productitem2(browser)
        time.sleep(3)
        productitem3(browser)
        time.sleep(20)




def productitem3(browser):
    for login in EmailList2.index:

        creatlist = browser.find_element_by_link_text('Create new listing')
        creatlist.click()
        sleep(randint(1, 3))

        print('creating a new post of products...........')
        time.sleep(1)

        browser.find_element_by_xpath('//a[@href="/marketplace/create/item/"]').click()
        time.sleep(2)





        image = browser.find_element_by_xpath('// input[ @ accept = "image/*,image/heif,image/heic"]')
        sleep(randint(1, 3))
        image.send_keys(EmailList2.loc[login]['Image-Path'])
        sleep(randint(1, 3))

        Title = browser.find_element_by_xpath('//label[@aria-label="Title"]')
        sleep(randint(1, 3))
        Title.send_keys(EmailList2.loc[login]['Title'])
        sleep(randint(1, 3))

        Price = browser.find_element_by_xpath('//label[@aria-label="Price"]')
        sleep(randint(1, 3))
        Price.send_keys(EmailList2.loc[login]['Price'])
        time.sleep(2)
        catgorymain = browser.find_element_by_xpath('//label[@aria-label="Category"]').click()
        sleep(randint(1, 3))
        catagory = browser.find_elements_by_xpath('//div[@class="jxo0map8"]')
        for i in catagory:
            namelist = i.text
            browser.implicitly_wait(20)
            print(namelist)
            if namelist == EmailList2.loc[login]['Category']:
                time.sleep(1)
                i.click()
                time.sleep(3)
                break


        time.sleep(2)

        conditionmain = browser.find_element_by_xpath('//label[@aria-label="Condition"]').click()
        time.sleep(2)
        condition = browser.find_elements_by_xpath('//div[@role="option"]')
        for n in condition:
            namecond = n.text
            print(namecond)
            if namecond == EmailList2.loc[login]['Condition']:
                time.sleep(1)
                n.click()
                time.sleep(3)
                break
            time.sleep(2)

        description = browser.find_element_by_xpath('//label[@aria-label="Description"]')
        description.send_keys(EmailList2.loc[login]['Description'])
        time.sleep(2)
        location = browser.find_element_by_xpath('//label[@aria-label="Location"]')
        sleep(randint(1, 3))
        location.send_keys(EmailList2.loc[login]['Location'])
        time.sleep(2)
        webdriver.ActionChains(browser).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        webdriver.ActionChains(browser).key_up(Keys.ARROW_DOWN).key_up(Keys.ENTER).perform()
        time.sleep(1)
        next = browser.find_element_by_xpath('//div[@aria-label="Next"]').click()
        sleep(randint(2, 5))
        publish = browser.find_element_by_xpath('//div[@aria-label="Publish"]').click()
        time.sleep(2)
        time.sleep(3)
        browser.implicitly_wait(30)

    print('All product uploaded Excel 3')

def productitem2(browser):
    for login in EmailList1.index:

        creatlist = browser.find_element_by_link_text('Create new listing')
        creatlist.click()
        sleep(randint(1, 3))

        print('creating a new post of products...........')
        time.sleep(1)

        browser.find_element_by_xpath('//a[@href="/marketplace/create/item/"]').click()
        time.sleep(2)





        image = browser.find_element_by_xpath('// input[ @ accept = "image/*,image/heif,image/heic"]')
        sleep(randint(1, 3))
        image.send_keys(EmailList1.loc[login]['Image-Path'])
        sleep(randint(1, 3))

        Title = browser.find_element_by_xpath('//label[@aria-label="Title"]')
        sleep(randint(1, 3))
        Title.send_keys(EmailList1.loc[login]['Title'])
        sleep(randint(1, 3))

        Price = browser.find_element_by_xpath('//label[@aria-label="Price"]')
        sleep(randint(1, 3))
        Price.send_keys(EmailList1.loc[login]['Price'])
        time.sleep(2)
        catgorymain = browser.find_element_by_xpath('//label[@aria-label="Category"]').click()
        sleep(randint(1, 3))
        catagory = browser.find_elements_by_xpath('//div[@class="jxo0map8"]')
        for i in catagory:
            namelist = i.text
            browser.implicitly_wait(20)
            print(namelist)
            if namelist == EmailList1.loc[login]['Category']:
                time.sleep(1)
                i.click()
                time.sleep(3)
                break


        time.sleep(2)

        conditionmain = browser.find_element_by_xpath('//label[@aria-label="Condition"]').click()
        time.sleep(2)
        condition = browser.find_elements_by_xpath('//div[@role="option"')
        for n in condition:
            namecond = n.text
            print(namecond)
            if namecond == EmailList1.loc[login]['Condition']:
                time.sleep(1)
                n.click()
                time.sleep(3)
                break
            time.sleep(2)

        description = browser.find_element_by_xpath('//label[@aria-label="Description"]')
        description.send_keys(EmailList1.loc[login]['Description'])
        time.sleep(2)
        location = browser.find_element_by_xpath('//label[@aria-label="Location"]')
        sleep(randint(1, 3))
        location.send_keys(EmailList1.loc[login]['Location'])
        time.sleep(2)
        webdriver.ActionChains(browser).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        webdriver.ActionChains(browser).key_up(Keys.ARROW_DOWN).key_up(Keys.ENTER).perform()
        time.sleep(1)
        next = browser.find_element_by_xpath('//div[@aria-label="Next"]').click()
        sleep(randint(2, 5))
        publish = browser.find_element_by_xpath('//div[@aria-label="Publish"]').click()
        time.sleep(2)
        time.sleep(3)
        browser.implicitly_wait(30)

    print('All product uploaded Excel 2')


def productitem1(browser):
    for login in EmailList.index:

        creatlist = browser.find_element_by_link_text('Create new listing')
        time.sleep(1)
        creatlist.click()
        time.sleep(2)

        print('creating a new post of products...........')
        time.sleep(2)

        browser.find_element_by_xpath('//a[@href="/marketplace/create/item/"]').click()
        time.sleep(2)

        image = browser.find_element_by_xpath('// input[ @ accept = "image/*,image/heif,image/heic"]')
        image.send_keys(EmailList.loc[login]['Image-Path'])
        time.sleep(3)

        Title = browser.find_element_by_xpath('//label[@aria-label="Title"]')
        Title.send_keys(EmailList.loc[login]['Title'])
        time.sleep(2)

        Price = browser.find_element_by_xpath('//label[@aria-label="Price"]')
        Price.send_keys(EmailList.loc[login]['Price'])
        time.sleep(2)
        catgorymain = browser.find_element_by_xpath('//label[@aria-label="Category"]').click()
        time.sleep(3)
        catagory = browser.find_elements_by_xpath('//div[@class="jxo0map8"]')
        for i in catagory:
            namelist = i.text
            time.sleep(1)
            browser.implicitly_wait(20)
            print(namelist)
            if namelist == EmailList.loc[login]['Category']:
                sleep(randint(2, 4))
                i.click()
                time.sleep(3)
                break



        time.sleep(2)

        conditionmain = browser.find_element_by_xpath('//label[@aria-label="Condition"]').click()
        time.sleep(2)
        condition = browser.find_elements_by_xpath('//div[@role="option"]')
        for n in condition:
            namecond = n.text
            print(namecond)
            if namecond == EmailList.loc[login]['Condition']:
                time.sleep(1)
                n.click()
                time.sleep(3)
                break

        time.sleep(2)

        description = browser.find_element_by_xpath('//label[@aria-label="Description"]')
        description.send_keys(EmailList.loc[login]['Description'])
        time.sleep(2)
        location = browser.find_element_by_xpath('//label[@aria-label="Location"]')
        location.send_keys(EmailList.loc[login]['Location'])
        time.sleep(2)
        webdriver.ActionChains(browser).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        webdriver.ActionChains(browser).key_up(Keys.ARROW_DOWN).key_up(Keys.ENTER).perform()
        time.sleep(1)
        next = browser.find_element_by_xpath('//div[@aria-label="Next"]').click()
        time.sleep(2)
        publish = browser.find_element_by_xpath('//div[@aria-label="Publish"]').click()
        time.sleep(2)
        time.sleep(3)
        browser.implicitly_wait(30)

    print('All product uploaded Excel 1')


def facbookautopost(browser, choose_option):

    for login in EmailList.index:

        browser.get('https://www.facebook.com/')

        time.sleep(3)

        try:
            browser.find_element_by_xpath('//button[@title="Accept All"]').click()
            print('button found')

        except NoSuchElementException:
            print('no button found')

        emailbtn = browser.find_element_by_id('email')
        emailbtn.send_keys(EmailList.loc[login]['Facebook-user'])
        time.sleep(1)
        passwrd = browser.find_element_by_id('pass')
        passwrd.send_keys(EmailList.loc[login]['Facebook-pass'])
        time.sleep(1)
        login_btn = browser.find_element_by_name('login').click()
        browser.implicitly_wait(50)
        time.sleep(6)
        sleep(randint(2,5))
        '''webdriver.ActionChains(browser).key_down(Keys.ESCAPE).perform()
        time.sleep(1)
        webdriver.ActionChains(browser).key_up(Keys.ESCAPE).perform()
        time.sleep(2)'''
        #Marketplace = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Marketplace"]'))).click()
        #Marketplace = browser.find_element_by_link_text('Marketplace')
        #Marketplace.click()
        browser.get('https://www.facebook.com/marketplace')
        time.sleep(6)
        webdriver.ActionChains(browser).key_down(Keys.ESCAPE).perform()
        time.sleep(1)
        webdriver.ActionChains(browser).key_up(Keys.ESCAPE).perform()
        time.sleep(2)


        optionpicker(browser, choose_option)



def start():
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    #options.add_argument("--headless")
    options.headless = False
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    choose_option = input('Type All or any digit: ')
    browser = webdriver.Chrome (chrome_options=options , executable_path=r'C:\\Users\\sajja\\PycharmProjects\\Lead Gorila GMB AND FB\Datascrap\chromedriver.exe')
    #browser = uc.Chrome('C:\\Users\\sajja\\PycharmProjects\\Lead Gorila GMB AND FB\Datascrap\chromedriver.exe')




    browser.maximize_window()
    facbookautopost(browser, choose_option)



def main():
    start()


if __name__ == "__main__":
    main()