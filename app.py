import webbrowser
from bs4 import BeautifulSoup
import time
import streamlit as st
import requests

st.markdown("<h1 style='text-align:center;'> Image Web Scraper</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'> By Alok</h4>", unsafe_allow_html=True)

style="""<style>
a:link, a:visited {
  background-color: #f44336;
  color: black;
  padding: 5px 8px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: red;
}
</style>"""
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .css-1wbqy5l {visibility: hidden;}
            </style>
            
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown(style,unsafe_allow_html=True)

with st.form("Search"):
    keyword=st.text_input("Enter image keyword you want to search")
    search=st.form_submit_button("Search")


placeholder=st.empty() 

if keyword:
    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup=BeautifulSoup(page.content,'html.parser')
    rows=soup.find_all("div",class_="MorZF")
    
    col1,col2=placeholder.columns(2)
    
    for index,row in enumerate(rows):
        img=row.find("img")
        #link=row["href"]
        imgsrc=img["src"]
        html=f"""<a class='downld' style='' download target='_blank' href='{imgsrc}'>Download</a>"""
        if index%2==0:
            col1.image(imgsrc)
            #btn=col1.button("Download", key=str(index))
            col1.markdown(html, unsafe_allow_html=True)
            col1.markdown("---",unsafe_allow_html=True)
        else:
            col2.image(imgsrc)
            #btn=col2.button("Download", key=str(index))
            col2.markdown(html, unsafe_allow_html=True)
            col2.markdown("---",unsafe_allow_html=True)


         
        
        

        



