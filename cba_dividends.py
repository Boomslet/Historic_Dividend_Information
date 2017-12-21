import urllib.request

"""
A script that retrieves historic data regarding dividends
paid by Commonwealth Bank of Australia to shareholders
on the ASX, 1997 - current.

Expected Yield is calculated by (units_held * cps),
and can be altered by adjusting units_held.

Makes use of urllib module:
https://docs.python.org/2/library/urllib.html#

and the BeautifulSoup library:
https://www.crummy.com/software/BeautifulSoup/

Author: Mark Boon
Date: 21/12/2017
Version: 3.0
"""

from bs4 import BeautifulSoup


def cba_summary(units=0):
    url = "http://www.sharedividends.com.au/cba+dividend+history"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')  # default html parser
    data = soup.find_all("td")

    print("CBA Dividend Summary:b \n")
    print('{:13}'  '{:6}'  '{:10}'  '{:}'
          .format("Date", "CPS", "Franked", "Ex-Yield"))

    for i in range(240, 0, -6):  # iterating by -6 allows i to correctly index every row of information

        date = (data[i - 6].text.strip())

        cps = float(data[i - 5].text.strip())

        franked = str(data[i - 4].text.strip()[0:3] == "100")

        ex_yield = (cps * units)

        print('{:13}'  '{:<6.0f}'  '{:10}'  '{:}'  '{:.2f}'
              .format(date, cps * 100, franked, "$", ex_yield))
