import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_episode_titles(url):
    # Make a request to the URL and get the HTML content
    response = requests.get(url)
    content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(content, "html.parser")

    # Find all anchor tags with class="episode-title" and extract the text
    episode_tags = soup.find_all("a", class_="episode-title")
    titles = [tag.text for tag in episode_tags]

    return titles

# Streamlit app title
st.title("Episode Title Scraper")

# Define the URL input field
url = st.text_input("Enter a URL to scrape")

# Define the scrape button
if st.button("Scrape"):
    if url:
        # Call the scrape_episode_titles function
        scraped_titles = scrape_episode_titles(url)

        # Display the scraped titles
        st.write("Scraped Episode Titles:")
        for title in scraped_titles:
            st.write(title)
    else:
        st.write("Please enter a URL to scrape")
