import urllib.request

"""
A script that retrieves historic data regarding dividends
paid by Westpac Banking Corporation to shareholders
on the ASX, 1983 - current.

Expected Yield is calculated by (units_held * cps),
and can be altered by adjusting units_held.

Makes use of urllib module:
https://docs.python.org/2/library/urllib.html#

and the BeautifulSoup library:
https://www.crummy.com/software/BeautifulSoup/

Author: Mark Boon
Date: 21/12/2017
Version: 2.0
"""

from bs4 import BeautifulSoup


def wbc_summary(units=0):
    url = "https://www.westpac.com.au/about-westpac/investor-centre/dividend-information/dividend-payment-history/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")  # default html parser
    data = soup.find_all("td")[3:]

    print("WBC Dividend Summary: \n")
    print('{:12}'  '{:6}'  '{:10}'  '{:}'
          .format("Date", "CPS", "Franked", "Ex-Yield"))

    # iterating by 6 allows i to correctly index every row of information
    for i in range(0, 421, 6):
        date = data[i].text.strip()

        cps = float(data[i + 1].text.strip()) / 100

        # checks if the third element of the row begins with "F" for "Fully franked"
        franked = str(data[i + 2].text.strip()[0] == "F")

        ex_yield = (cps * units)

        print('{:12}'  '{:<6.0f}'  '{:10}'  '{:}'  '{:.2f}'
              .format(date[:10], cps * 100, str(franked), "$", ex_yield))
