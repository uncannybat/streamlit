import streamlit as st
import requests
from bs4 import BeautifulSoup


st.title("Web Scraping App")


url = st.text_input("Enter a URL to scrape")


if st.button("Scrape"):
   
    response = requests.get(url)
    content = response.content

   
    soup = BeautifulSoup(content, "html.parser")

    
    data = soup.find("h2").text 
    st.write("Scraped Data:")
    st.write(data)
