import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_anchors(url):
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Find all anchor tags and extract their href attributes
    anchor_tags = soup.find_all("a")
    hrefs = [tag.get("href") for tag in anchor_tags]

    return hrefs

# Streamlit app title
st.title("Anchor Tag Web Scraper")

# Define the URL input field
url = st.text_input("Enter a URL to scrape")

# Define the scrape button
if st.button("Scrape"):
    if url:
        # Call the scrape_anchors function
        scraped_hrefs = scrape_anchors(url)

        # Display the scraped anchor tags
        st.write("Scraped Anchor Tags:")
        for href in scraped_hrefs:
            st.write(href)
    else:
        st.write("Please enter a URL to scrape")
