import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import streamlit as st
dataframe_=pd.read_csv('cleaned_data.csv')

def genre_based(df, anime_id,df_full,genre_matrix,total_num=30):
    # genre = CountVectorizer()
    # genre_matrix = genre.fit_transform(df['genre_new'])
    # pickle.dump(genre_matrix, open('genre.pkl', 'wb'))
    gen_sim = cosine_similarity(genre_matrix)

    location = df.loc[df['uid']==anime_id].index[0]
    recommended_lst = list(enumerate(gen_sim[location]))

    recommended_lst = sorted(recommended_lst, key = lambda x:x[1] ,reverse=True)
    recommended_lst = recommended_lst[1:total_num]

    movie_i = [j[0] for j in recommended_lst]
    final_list = [i for i in movie_i if 'Season' not in df_full['title'].iloc[i]]
    indices = pd.Series(df_full.index, index=df_full['uid'])
    final_list=[j for j in final_list if df_full['title'].iloc[indices[anime_id]].split(' ')[0].replace(':','') not in df_full['title'].iloc[j].split(' ')]
    recommended_series = df_full['img_url'].iloc[final_list]
    return recommended_series[:10]

def synopsis_based(df,anime_id, df_full, total_num=30):
    synopsis = CountVectorizer(stop_words='english')
    synopsis_matrix = synopsis.fit_transform(df['synopsis'])

    syn_similar = cosine_similarity(synopsis_matrix, synopsis_matrix)
    df1 = df.reset_index()
    indices = pd.Series(df1.index, index=df1['uid'])

    sim_scores = list(enumerate(syn_similar[indices[anime_id]]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:total_num]

    movie_indices = [i[0] for i in sim_scores]
    final_list = [i for i in movie_indices if 'Season' not in df_full['title'].iloc[i]]
    indices = pd.Series(df_full.index, index=df_full['uid'])
    final_list=[j for j in final_list if df_full['title'].iloc[indices[anime_id]].split(' ')[0] not in df_full['title'].iloc[j].split(' ')]
    recommended_series = df_full['img_url'].iloc[final_list]
    return recommended_series[:10]
 
