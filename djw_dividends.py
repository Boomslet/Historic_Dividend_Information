"""
A script that retrieves historic data regarding dividends
paid by Djerriwarrh Investments to shareholders
on the ASX, 1996 - current.

Expected Yield is calculated by (units_held * cps),
and can be altered by adjusting units_held.

Makes use of urllib module:
https://docs.python.org/2/library/urllib.html#

and the BeautifulSoup library:
https://www.crummy.com/software/BeautifulSoup/

Author: Mark Boon
Date: 7/08/2017
Version: 1.1
"""

import urllib.request
from bs4 import BeautifulSoup


units_held = 0
url = "http://www.djerri.com.au/Dividend-History.aspx"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")  # default html parser
data = soup.find_all("td")

print("DJW Dividend Summary: \n")
print('{:14}'  '{:5}'  '{:9}'  '{:}'
      .format("Date", "CPS", "Franked", "Ex-Yield"))

for i in range(8, len(data) - 4, 4):  # iterating by 4 allows i to correctly index every row of information

    date = data[i].text.strip().split(" ")
    date = date[0] + "/" + date[1][:3] + "/" + date[-1]
    cps = float(data[i + 1].text.strip())
    franked = str(data[i + 2].text.strip() == "100.00%")
    ex_yield = (cps / 100) * units_held

    print('{:14}'  '{:<5.0f}'  '{:10}'  '{:}'  '{:.2f}'
          .format(date, cps, franked, "$", ex_yield))
