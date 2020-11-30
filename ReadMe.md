# Title: Booth Shoe Bot
Author: YahikoSV \
Contributor: CrugarMan \
Version: 2.1.1

#### FOR PERSONAL USE ONLY
#### ASK PERMISSION FROM AUTHOR IF YOU WANT TO USE IT

This is a Shoe Bot for Booth. Since it is only for personal project,
this only uses one method of purchasing an item. No UI Yet.

##### Pre-requisites: More necessary info/examples below: 
[1] Has existing Pixiv Account \
[2] Link of the merchandise from the circle/owner. \
[3] Selenium Webdriver (Chrome, Edge, Firefox) \
[4] Payment method must be Paypal and is already completed beforehand (first field) \
[5] Shipping address is already completed beforehand \
[6] Shipping method is either "Physical" or "Digital" only. \
[7] The language of the booth website when last logged-in should be in English. \
[8] Purchases only "1 item with 1 quantity" at a time.


##### Notes:

[1] Has existing Pixiv Account \
Basically you need your Username/Email and Password. \
Note: This program do not save data! Data is only stored locally.

[2] Link of the merchandise from the circle/owner
There are two similar links for example:
[A] https://booth.pm/en/items/2441613
[B] https://hololive.booth.pm/items/2441613

The merch is the same but the pages are different. Only the link with the circle/owner (e.g. hololive) domain present (B) can be used.

[3] Selenium Webdriver (Chrome, Edge, Firefox)
Download Selenium Driver of your browser choice. Make sure it is the same version as your browser.
Note: TBH, any browser available by selenium should work. 

[6] For Physical (direct) shipping your address must be in Japan either by proxy or in real life. "Buyee" (worldwide shipping) does not work because uses a different method. On the other hand, "Digital" items do not need a shipping address.

Note: Not all bugs and exceptions are all accounted for. There is still a need of human intervention if random bugs do occur.

Note2: There's still a lot of pre-requisites required...

Examples of some bugs:
[1] Random capcha when logging-in Pixiv. 
Solution: Solve the capcha by yourselves.

[2] Account failed to log-in properly. 
Possible Solution [1] Wrong credentials
Possible Solution [2] The loading when logging-in got overwritten by the next code. Requires adding buffer time

[3] A certain input/click keeps retrying but failed.
Possible Solution [1] Depends on the speed of your internet, the code may run faster than the loading time. Just wait for it to load.
Possible Solution [2] If [1] fails. Manually click the button. It should proceed to the next code.
Possible Solution [3] If [2] fails, Increase your Loadtime_buffer. Your PC/ISP might be too slow such that some codes get overrided.

### IF THERE ARE ANY ISSUES, PLEASE CONTACT US###
### FEEDBACK IS HIGHLY APPRECIATED ###

Short-term Developments:
[1] Translate variant type from Japanese to English
[2] Remove pre-requisite [7]
[3] Find more bugs/ exceptions

Long-term Developments: 
[1] Develop User Interface

Wasshoi!

Versions:
2.1.1 - Bug Fixes and Bug fixes
2.1 - Refactor code (CrugarMan)
2.0 - Convert Hololive Shoe Bot -> Booth Shoe Bot
1.0 - Base Code
