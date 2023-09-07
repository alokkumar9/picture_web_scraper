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
    rows=soup.find_all("div",class_="MorZF")
    
    col1,col2=placeholder.columns(2)
    for index,row in enumerate(rows):
         img=row.find("img")
         imgsrc=img["src"]
         print(imgsrc)
         if index%2==0:
            col1.image(imgsrc)
             btn=col1.button("Download", key=str(index))
         else:
            col2.image(imgsrc)
            btn=col1.button("Download", key=str(index))
         
        
        

        



