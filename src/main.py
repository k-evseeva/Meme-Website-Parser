import requests
from bs4 import BeautifulSoup
import time

def make_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Accept": "text/html"
        }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} status code")
    except requests.RequestException:
        raise Exception(f"Error while requesting")
    return response

url = "https://memepedia.ru"
response = make_request(url)

soup = BeautifulSoup(response.text, "html.parser")
month_memes = soup.find_all("h2", class_="entry-title")

brainrot_url = ""

for meme in month_memes:
    meme_url = meme.find("a").get("href")
    if "brejnrot" in meme_url:
        brainrot_url = meme_url
        break

if not brainrot_url:
    print("Brainrot is outdated")
    print("Uploading a link to the page...", end="\n\n\n")
    brainrot_url = "https://memepedia.ru/italyanskie-brejnrot-zhivotnye-polnyj-gajd-s-kartinkami/"
else:
    print("Brainrot is still popular", end="\n\n\n")

time.sleep(5)
response = make_request(brainrot_url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h2")

for title in titles:
    title = title.text.strip()
    if "История" in title:
        break
    print(title, end="\n\n\n")