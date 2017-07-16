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
Date: 15/07/2017
Version: 1.0
"""

from bs4 import BeautifulSoup

units_held = 0

url = ("https://www.westpac.com.au/about-westpac/investor-centre/dividend-information/dividend-payment-history/")
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")          # default html parser
data = soup.find_all("td")[3:]                     # slicing removes irrelevant data from the result set


print("WBC Dividend Summary: \n")
print('{:12}'  '{:6}'  '{:10}'  '{:}'
      .format("Date", "CPS", "Franked", "Ex-Yield"))

for i in range(0, 421, 6):                         # iterating by 6 allows i to correctly index every row of information

    date = data[i].text.strip()

    cps = float(data[i + 1].text.strip()) / 100

    franked = data[i + 2].text.strip()[0] == "F"   # checks if the 3rd element of the row begins with "F" for "Fully [franked]"
  
    print('{:12}'  '{:.2f}'  '  {:9}'  ' {:}'  '{:.2f}'  
          .format(date[:10], cps, str(franked),  "$", cps * units_held))  # slicing ensures only the 10 characters representing the date are printed
