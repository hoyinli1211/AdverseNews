import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def perform_search(name):
    search_url = f"https://www.google.com/search?q={name}+adverse+news"
    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="g")

    # Extract the title and link from the search results
    data = []
    for result in results[:5]:
        title = result.find("h3").text
        link = result.find("a")["href"]
        data.append({"Title": title, "Link": link})

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    return df
    
st.title("Adverse News Search")
name = st.text_input("Enter a name to search:")

if st.button("Search"):
    result = perform_search(name)
    st.success(result)
    
