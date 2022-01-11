import pandas as pd
import numpy as np
import string
import ast
from recommender import genre_based, synopsis_based

synopsis=pd.read_csv('synopsis.csv')
df=pd.read_csv('cleaned_data.csv')
genre=df[['uid','genre']]
genre['genre'] = genre.genre.apply(lambda x: ast.literal_eval(str(x)))

# concatenating list and stripping off comma and bracker 
def list_to_string(x):
    stri=" "
    return (stri.join(x))

genre['genre_new']=genre['genre'].map(lambda x:list_to_string(x))
genre.drop('genre',inplace=True,axis=1)

# converting name to anime's uid
def name_to_uid(name):
    uid = df[df['title']==name]['uid']
    return uid.values[0]

# outputs the series of predicted animes
def predicted(anime_id):
    
    genre_matrix=pd.read_pickle(r'genre.pkl')
    genre_list = genre_based(genre, anime_id=anime_id,df_full=df,genre_matrix=genre_matrix)
    synop_list = synopsis_based(synopsis, anime_id=anime_id, df_full=df)
    popular = df.sort_values('popularity')['img_url'][:10]

    return genre_list,synop_list,popular
