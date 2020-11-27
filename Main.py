# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:20:00 2020

@author: YahikoSV
"""

from shoemod import ShoeMod

###################
### Data Inputs ###
###################

# #Pixiv Details, format = "asdfg"
Pixiv_ID = "" # "abc123" / "abc@gmail.com"
Pixiv_Password = "" #"password"

#Merch Details
URL = ""  #"https://hololive.booth.pm/items/2533220" 

#Time Available
PrePurchase = True #If item not yet released = True
#Note: The button rank of the variants may change (e.g. when item(s) get sold out)
#Do not set it True when the item is already released to be safe

#Webdriver Location, link to where the webdriver application is
webdriver_type = ""  #Chrome, Edge, Firefox
webdriver_path = r'' #r'C:/Users/Downloads/chromedriver.exe'

### Internal Inputs ###  No need to change
Loadtime_buffer = 1  #(in seconds) Depends how fast your PC is

##############################################################################


### Run module ###

mod = ShoeMod(Pixiv_ID, Pixiv_Password, webdriver_type, webdriver_path, Loadtime_buffer)
mod.Run(URL, PrePurchase)
