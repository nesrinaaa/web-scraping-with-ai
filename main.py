import streamlit as st
st.title("web scraper app")
url = st.text_input("Enter the URL of the website you want to scrape:")
if st.button("Scrape site"):
    st.write(f"Scraping {url}...")