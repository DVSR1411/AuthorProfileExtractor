import requests
from bs4 import BeautifulSoup
def scrapeauthorinfo(authorname):
    searchURL = f"https://www.goodreads.com/search?utf8=%E2%9C%93&query={authorname}"
    response = requests.get(searchURL)
    soup = BeautifulSoup(response.text, "html.parser")
    if response.status_code == 200:
        result = soup.find("a",class_="authorName")
        if result:
            authorURL = result["href"]
            response = requests.get(authorURL)
            soup = BeautifulSoup(response.text, "html.parser")
            if response.status_code == 200:
                name = soup.find("span", itemprop="name").get_text() if soup.find("span", itemprop="name") else "N/A"
                rating = soup.find("span", itemprop="ratingValue").get_text() if soup.find("span",itemprop="ratingValue") else "N/A"
                website = soup.find("a", href=True, rel="noopener noreferrer", target="_blank")["href"] if soup.find("a", href=True, rel="noopener noreferrer", target="_blank") else "N/A"
                twitter = soup.find("a", href=True, rel="nofollow noopener noreferrer", target="_blank")["href"] if soup.find("a", href=True, rel="nofollow noopener noreferrer", target="_blank") else "N/A"
                birthdate = soup.find("div", class_="dataItem", itemprop="birthDate").get_text().strip() if soup.find("div",class_="dataItem", itemprop="birthDate") else "N/A"
                print(f"Author name: {name}")
                print(f"Birthdate: {birthdate}")
                print(f"Contact details:\nWebsite: {website}\nTwitter: {twitter}")
                print(f"Rating: {rating}")
                print(f"Book details: ")
                books=', '.join([book.get_text().strip() for book in soup.find_all("a", class_="bookTitle")])
                print(f'{books}')
            else:
                print(f"Error: {response.status_code}")
        else:
            print(f"No results found for '{authorname}'")
    else:
        print(f"Error: {response.status_code}")
authorname = input("Enter the name of the author: ")
scrapeauthorinfo(authorname)