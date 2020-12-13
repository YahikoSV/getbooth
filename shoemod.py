# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:20:00 2020

@author: YahikoSV
"""

import datetime as dt
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import time
import sys
from enum import Enum

class Consts(Enum):
    MINUTE_LAG = 1
    SECOND_LAG = 59
    RELOAD_LAG = 1
    LOADING_LAG = 5 
    COUNTDOWN_TIMER = 30 #mins
    TIME_STEP = 1
    
class ShoeMod:
    def __init__(self, Pixiv_ID, Pixiv_Password, webdriver_type, webdriver_path, latency = 1):
        self.Pixiv_ID = Pixiv_ID
        self.Pixiv_Password = Pixiv_Password
        self.webdriver_type = webdriver_type
        self.webdriver_path = webdriver_path
        self.latency = latency
        self.driver = None
        self.market_URL = None

    def LogInBooth(self):
        url = "https://booth.pm/en" #force cache into EN
        if self.webdriver_type == "Chrome":
            self.driver = webdriver.Chrome(executable_path = self.webdriver_path)
            self.driver.get(url)
        elif self.webdriver_type == "Edge":
            self.driver = webdriver.Edge(executable_path = self.webdriver_path)
            self.driver.get(url)
        elif self.webdriver_type == "Firefox":
            self.driver = webdriver.Firefox(executable_path = self.webdriver_path)
            self.driver.get(url)
        else:
            print("Invalid Webdriver")
            sys.exit()

        self.LoadingBuffertoClick('//a[@href="/users/sign_in"]','Waiting...','2/3 Pixiv SignIn Opened')
        print("1/3 Booth SignIn Opened")

        self.LoadingBuffertoClick('//a[@class="btn pixiv-oauth signin full-length"]','Waiting...','2/3 Pixiv SignIn Opened')

        self.LoadingBuffertoType('//input[@autocomplete="username"]','Typing...','ID Typed Sucessfully', self.Pixiv_ID)
        self.LoadingBuffertoType('//input[@autocomplete="current-password"]','Typing...','Password Typed Sucessfully', self.Pixiv_Password)

        #for the Privacy Policy Update March 2020
        try:
            self.driver.find_element_by_xpath('//button[@class="styled-button"]').click()
        except:
            pass

        SignUp = self.driver.find_elements_by_xpath('//button[@class="signup-form__submit"]')[1]
        self.LoadingBuffertoClickSimple(SignUp,'Loading or need manual guidance','3/3 SignIn Successful')

    def LogOutBooth(self):
        url = "https://booth.pm/"
        self.driver.get(url)
        self.LoadingBuffertoClick('//span[@class="cmd-label"]','Waiting...','1/2 Tab Opened')
        self.LoadingBuffertoClick('//a[@href="/users/sign_out"]','Waiting...','2/2 Logged-Out Successfully')

    def Preparation(self, URL, PrePurchase, Time_Available):
        self.driver.get(URL)
        Time = [int(t) for t in Time_Available.split(':')]
        if PrePurchase == True:
            Current_Time = None
            print("waiting...")
            print (Time_Available)
            CT = [dt.datetime.now().hour,  dt.datetime.now().minute]
            if CT[1] + Consts.COUNTDOWN_TIMER.value >= 60:
                CT[0] = CT[0] + int((CT[1] + Consts.COUNTDOWN_TIMER.value)/60)
                CT[1] = (CT[1] + Consts.COUNTDOWN_TIMER.value)%60
                
            while [Time[0], Time[1]] >= [CT[0],  CT[1] + Consts.COUNTDOWN_TIMER.value]:
                CT = [dt.datetime.now().hour,  dt.datetime.now().minute]
        
            print("countdown!")
            while(Current_Time := dt.datetime.now()).strftime('%H:%M') != Time_Available:
                time.sleep(Consts.TIME_STEP.value)
                print("{:02d}:{:02d}".format(int(Time[0] - Current_Time.hour)*60 + Time[1] - Current_Time.minute - Consts.MINUTE_LAG.value, Consts.SECOND_LAG.value - Current_Time.second), end='\r')         
        
        print("VIVA HOLOLIVE RESISTANCE")

    def AddToCart(self, Button_Rank, Digital_Only):
        self.driver.refresh() #this is where it might take a while

        while True:
            try:
                self.driver.find_elements_by_xpath('//button')[Button_Rank].click()
                print('1/5 Item Selected')
                break
            except:
                print('loading...')
                time.sleep(self.latency)

        self.market_URL = self.driver.current_url

        self.LoadingBuffertoClick('//a[@class="btn btn--primary u-w-sp-100"]','Checkout Loading...', '2/5 Checkout Selected')

        if Digital_Only == True:
            self.LoadingBuffertoClick('//input[@value="Order Confirmation"]','Payment Type Loading...','3/5 Payment Type Selected')
            print('4/5 Shipping Type Skipped')
        else:
            self.LoadingBuffertoClick('//input[@value="Next Step"]','Payment Type Loading...','3/5 Payment Type Selected')
            self.LoadingBuffertoClick('//button[@class="btn primary-color mobile-full-length"]','Shipping Loading...','4/5 Shipping Type Selected')

    def PurchaseItem(self, Ready_to_Purchase):
        if Ready_to_Purchase == True:
            #Failsafe
            self.LoadingBuffertoClick('//input[@value="Place Order"]','Placing Order...', '5/5 Order Completed')
            now = dt.datetime.now()
            print(f' Order Completed: {now.strftime("%H:%M:%S")}')
            logout = input("log-out? (type 'y' and Enter):")
            if logout == 'y':
                self.LogOutBooth()
            print('Logged-out')
        else:
            now = dt.datetime.now()
            print(f' Time Completed: {now.strftime("%H:%M:%S")}')
            clearpurchase = input("Clear purchase and log-out? (type 'y' and Enter):")
            if clearpurchase == 'y':
                self.ClearPurchase()
                self.LogOutBooth()
                print('Purchase Cleared and Logged-out')

    def ClearPurchase(self):
        self.driver.get(self.market_URL)
        self.LoadingBuffertoClick('//i[@class="icon-cancel bigger no-margin"]','Manually Approve Removal...','1/1 Purchase Cleared')
        input("Press Enter if you removed the confirmation message. ")

    def LoadingBuffertoClick(self, elementname, fail_msg, success_msg):
        while True:
            try:
                self.driver.find_element_by_xpath(elementname).click()
                print(success_msg)
                break
            except TimeoutError:
                print(str(sys.exc_info()[0]))
                self.driver.refresh()
            except Exception:
                print(fail_msg)
                #print(f"Error: {str(e)}") #if you want to show error msg 
                print(str(sys.exc_info()[0]))
                time.sleep(self.latency)
                continue

    def LoadingBuffertoClickSimple(self, element, fail_msg, success_msg):
        while True:
            try:
                element.click()
                print(success_msg)
                break
            except TimeoutError:
                print(str(sys.exc_info()[0]))
                self.driver.refresh()                    
            except Exception:
                print(fail_msg)
                #print(f"Error: {str(e)}") #if you want to show error msg 
                print(str(sys.exc_info()[0]))
                time.sleep(self.latency)
                continue

    def LoadingBuffertoType(self, elementname, fail_msg, success_msg, credentials):
        while True:
            try:
                self.driver.find_element_by_xpath(elementname).send_keys(credentials)
                print(success_msg)
                break
            except Exception:
                print(fail_msg)
                #print(f"Error: {str(e)}") #if you want to show error msg 
                print(str(sys.exc_info()[0]))
                time.sleep(self.latency)
                continue

    def FindProductVariation(self, URL, PrePurchase):
        source = requests.get(URL).text
        soup = bs(source, 'lxml')

        info = soup.find_all('li', class_="variation-item")
        print(' Available Items:')
        print('')

        rank = 0
        if PrePurchase == True:
            for variation in info:
                rank = self.InputasAvailable(variation,rank)
        elif PrePurchase == False:
            for variation in info:
                if bool(variation.find('form')) == True:
                    rank = self.InputasAvailable(variation,rank)
        else:
            print('Invalid Prepurchase Value')
            sys.exit()

    def InputasAvailable(self, variation, rank):
        if name_exists := (variation.find('div', class_="variation-name").contents != []):
            variation_name = variation.find('div', class_="name").text
        variation_price = variation.find('div', class_="variation-price").text
        variation_type = variation.find('span', class_="type").text

        rank += 1

        print(f' Button Rank = {rank}')
        if variation_type == 'ダウンロード商品':
            print(f' Type of Product = {variation_type}  (Digital Only)')
        else:    
            print(f' Type of Product = {variation_type}')
            
        print(f' Price = {variation_price}')
        if name_exists:
            print(f' Variation Name = {variation_name}')
        print('')
        return rank

    def Run(self, URL, PrePurchase, Time_Available = None, Wallet_check = True):
        ### 1. Check for Available Items and find respective Button Rank
        self.FindProductVariation(URL, PrePurchase)
        Button_Rank = int(input("Enter Button Rank: "))
        
        ### 2. Ask Permissions ###
        Digital_Only = False
        if input("Product is Digital Only? (y/n): ") == 'y':
            Digital_Only = True           
        if Wallet_check:
            Ready_to_Purchase = (input("Warning: typing y will purchase the item: Purchase Item? (y/n): ") == 'y')          
        if Ready_to_Purchase == False:
            if input("Do you want to simulate the purchase? (y/n): ") != 'y':
                sys.exit()
                
        ### 3. Purchase the item ###
        self.LogInBooth()
        if PrePurchase and Time_Available == None:
            Time_Available = input("Enter purchase time \"HH:MM\" (military): ")
        else:
            time.sleep(Consts.LOADING_LAG.value)
        if PrePurchase == True:
            self.Preparation(URL,PrePurchase, Time_Available)
        else:
            self.driver.get(URL)
            print("VIVA HOLOLIVE RESISTANCE")
        self.AddToCart(Button_Rank, Digital_Only)

        self.PurchaseItem(Ready_to_Purchase)
        if input("Close Window? (y/n): ") == 'y':
            self.driver.close()
