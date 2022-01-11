from predict import predicted, name_to_uid
import streamlit as st
import pandas as pd
from render import render, home_page

st.set_page_config(page_title="Anime Recommender",layout ='wide')

df=pd.read_csv('cleaned_data.csv')
list_of_anime = df['title'].to_list()

st.title("Anime Recommendation Engine")

anime_name = st.sidebar.selectbox('Enter the Name',['---']+list_of_anime)
preference = st.sidebar.selectbox("Preference",('home','Story', 'Genre', 'Popular'))
if anime_name != '---':
    genre_list,synop_list,popular_list = predicted(anime_id=name_to_uid(anime_name))

    if len(anime_name)>1:
        if preference =='Popular':
            render(popular_list,200)
        elif preference == 'Genre':
            render(genre_list,200)
        elif preference == 'home':
            home_page()
        else:
            render(synop_list,200)
else:
    home_page()
