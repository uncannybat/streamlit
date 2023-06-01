import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_anchor_titles(url):
    
    response = requests.get(url)
    content = response.content

   
    soup = BeautifulSoup(content, "html.parser")

   
    anchor_tags = soup.find_all("a")
    titles = [tag.get("title") for tag in anchor_tags if tag.get("title")]

    return titles


st.title("Anchor Tag Title Scraper")


url = st.text_input("Enter a URL to scrape")


if st.button("Scrape"):
    if url:
       
        scraped_titles = scrape_anchor_titles(url)

       
        st.write("Scraped Titles:")
        for title in scraped_titles:
            st.write(title)
    else:
        st.write("Please enter a URL to scrape")
