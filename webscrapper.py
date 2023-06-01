import streamlit as st
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.url = ""

    def scrape(self):
       
        response = requests.get(self.url)
        content = response.content

       
        soup = BeautifulSoup(content, "html.parser")

        
        anchor_tags = soup.find_all("a")
        titles = [tag.get("title") for tag in anchor_tags if tag.get("title")]

        return titles



st.title("AnimePahe.ru Anchor Tag Titles")


scraper = WebScraper()


scraper.url = "https://www.animepahe.ru/"


if st.button("Scrape"):
   
    scraped_titles = scraper.scrape()

   
