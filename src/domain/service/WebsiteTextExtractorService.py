import requests
from bs4 import BeautifulSoup
import os


class WebsiteTextExtractorService:
    def fetch_website_text(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text(separator='\n', strip=True)

    def save_text_to_file(self, text: str, filename: str) -> str:
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
        return filepath

    def extract_and_save(self, url: str, filename: str = "website_text.txt") -> str:
        text = self.fetch_website_text(url)
        return self.save_text_to_file(text, filename)