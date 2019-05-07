# mobile-wifi-battery-level
**MWBL - Mobile Wifi Battery Level**
Get battery level of TP-Link 4g mobile wifi. Tested to work with TP-Link M7350.

Script logins to TP-Link management website and scrapes battery level of the device.

Dependencies:
- Python
- Selenium
- BeautifulSoup

Usage:
```
python mwbl.py
```

Examples:\
I have set up cronjob every five minutes that prints output of this script to file that polybar reads.
