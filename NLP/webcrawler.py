import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("Page Title:")
    print(soup.title.text)

    print("\nFirst 20 Hyperlinks:\n")

    links = soup.find_all("a")

    for i, link in enumerate(links[:20], start=1):
        href = link.get("href")
        if href:
            print(f"{i}. {href}")
else:
    print("Failed to retrieve webpage.")