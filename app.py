import webbrowser
from bs4 import BeautifulSoup
import time
import streamlit as st
import requests

st.markdown("<h1 style='text-align:center;'> Image Web Scraper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword=st.text_input("Enter image keyword you want to search")
    search=st.form_submit_button("Search")
    placeholder=st.empty()

if keyword:
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup=BeautifulSoup(page.content,"html.parser")
    rows=soup.find_all("div",class_="ripi6")
    col1,col2=placeholder.columns(2)
    for index,row in enumerate(rows):
        figures=row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img", class_="YVj9w")
            list=img['srcset'].split("?")
            anchor=figures[i].find("a", class_="rEAWd")
            if i==0:
                col1.image(list[0])
                btn=col1.button("Download", key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("http://unsplash.com/download"+anchor["href"])
            time.sleep(0.5)

        



