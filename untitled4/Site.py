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
