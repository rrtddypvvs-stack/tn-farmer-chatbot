import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.tn.gov.in/"
START_URL = "https://www.tn.gov.in/scheme_list.php?dep_id=Mg=="

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Download the scheme listing page
response = requests.get(START_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Store all scheme URLs
scheme_links = []

# Find all scheme links
for link in soup.find_all("a"):
    href = link.get("href")

    if href and "scheme_details.php" in href:
        full_url = urljoin(BASE_URL, href)
        scheme_links.append(full_url)

print(f"Found {len(scheme_links)} scheme pages.\n")

# Download each scheme page
for index, url in enumerate(scheme_links, start=1):

    print(f"Downloading {index}/{len(scheme_links)} : {url}")

    page = requests.get(url)
    page.raise_for_status()

    page_soup = BeautifulSoup(page.text, "html.parser")

    # Find the scheme details table
    table = page_soup.find("table", class_="table")

    if table:
        text = table.get_text(separator="\n", strip=True)
    else:
        text = "No scheme details found."

    filename = f"data/scheme_{index}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

print("\nAll scheme pages downloaded successfully!")