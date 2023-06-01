import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_anchors(url):
   
    response = requests.get(url)
    content = response.content

    
    soup = BeautifulSoup(content, "html.parser")

    
    anchor_tags = soup.find_all("a")
    hrefs = [tag.get("href") for tag in anchor_tags]

    return hrefs


st.title("Anchor Tag Web Scraper")


url = st.text_input("Enter a URL to scrape")


if st.button("Scrape"):
    if url:
       
        scraped_hrefs = scrape_anchors(url)

       
        st.write("Scraped Anchor Tags:")
        for href in scraped_hrefs:
            st.write(href)
    else:
        st.write("Please enter a URL to scrape")
