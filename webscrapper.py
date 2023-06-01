import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlit app title
st.title("Web Scraping App")

# Define the URL input field
url = st.text_input("Enter a URL to scrape")

# Define the scrape button
if st.button("Scrape"):
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Find and display the desired data from the scraped HTML
    data = soup.find("h1").text  # Example: Scraping the <h1> tag content
    st.write("Scraped Data:")
    st.write(data)
