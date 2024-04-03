import requests
from bs4 import BeautifulSoup
class AuthorScrapper:
    def scrap(authorURL):
        try:
            response = requests.get(authorURL)
            soup = BeautifulSoup(response.text, "html.parser")
            name = soup.find("span", itemprop="name").get_text() if soup.find("span", itemprop="name") else "NA"
            rating = soup.find("span", itemprop="ratingValue").get_text() if soup.find("span",itemprop="ratingValue") else "NA"
            website = soup.find("a", href=True, rel="noopener noreferrer", target="_blank")["href"] if soup.find("a",href=True,rel="noopener noreferrer",target="_blank") else "NA"
            twitter = soup.find("a", href=True, rel="nofollow noopener noreferrer", target="_blank")["href"] if soup.find("a", href=True, rel="nofollow noopener noreferrer", target="_blank") else "NA"
            books = ', '.join([book.get_text().strip() for book in soup.find_all("a", class_="bookTitle")])
            return name, website, twitter, rating, books
        except Exception as ex:
            pass