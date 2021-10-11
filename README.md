# python_2ass
## TITLE

Write a Python code which will get all articles, blogs, news related to the inputed cryptocurrency.

## Installation
PyPl
``` bash 
pip install beautifulsoup4
```


## Usage

``` bash 
from Site import findsites

scrapper = findsites()
list = scrapper.findArticle("bitcoin")
for i in list: print(i)
print(f"\n sites: {str(len(list))}")
import requests
from bs4 import BeautifulSoup


class findsites():
    def findArticle(self, crypto):
        url = "https://www.google.com/search?q=site%3Acoinmarketcap.com+alexandria+" + crypto
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")
        listOfLinks = []
        link: object
        for link in soup.find_all("a"):
            href = link.get("href")
            if 'https://coinmarketcap.com/' not in href:
                continue
            tLink = 'https://www.google.com' + href
            listOfLinks.append(tLink)
        return listOfLinks

``` 

## Examples


https://www.google.com/url?q=https://coinmarketcap.com/alexandria&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAUQAg&usg=AOvVaw0yhkAZsHGqOxqnZLbVhJZ1
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/crypto-basics&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQ0gJ6BAgFEAQ&usg=AOvVaw0izaW0cb03lWSfDzvBdZxc
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQ0gJ6BAgFEAU&usg=AOvVaw3bdBcrHsNtGxX_qkIZOWB2
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-price-analysis-the-upcoming-bull-run-will-be-wilder-than-the-previous-one&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQ0gJ6BAgFEAY&usg=AOvVaw0Xbzny3Qmqu8xungteB558
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/how-to-guides&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQ0gJ6BAgFEAc&usg=AOvVaw0DGD_HVlzEVrSrPOtHIDy0
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/about&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAcQAg&usg=AOvVaw2Hd99qyBDY3M7VaIVK4ilV
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAYQAg&usg=AOvVaw3v_uVFc6U-NVQZ6mz-EtI6
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/categories/crypto-basics&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAgQAg&usg=AOvVaw06EP7y4SBxIG1VHyjLbUCj
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/how-to-live-on-bitcoin&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAoQAg&usg=AOvVaw1AUbO60oT5vP-3VJOh8j0l
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/glossary/cryptocurrency&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAkQAg&usg=AOvVaw0sBhMbJtFATmQNq57BYatR
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-hits-50-000-for-first-time-in-a-month&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAIQAg&usg=AOvVaw3ynADonJXlt5n0OR7t-gmx
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/coinmarketcap-daily-oct-5-bitcoin-to-50k&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAMQAg&usg=AOvVaw3dvmNrE3w1Ma0EWnbWVzSG
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-price-prediction&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAEQAg&usg=AOvVaw3qI0zSJ3L0yfcFYo7Q90z3
https://www.google.com/url?q=https://coinmarketcap.com/alexandria/article/bitcoin-to-cross-55k-in-a-week&sa=U&ved=2ahUKEwixruXEhsDzAhV2R_EDHXtQAvoQFnoECAAQAg&usg=AOvVaw2yTSRnnUSNgID0OXkej3Md



## API Documentation

https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://pypi.org/project/requests/
