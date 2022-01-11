import streamlit as st
import pandas as pd
import itertools

df=pd.read_csv('cleaned_data.csv')
def render(array_,width=180):
    col1,mid1,col2,mid2=st.columns([1,1.5,1,1.5])
    with col1:
        st.image(array_.values[0],  width=width)
        
    with mid1:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[0]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[0]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes ",df[df['img_url']==array_.values[0]]['episodes'].values[0])
        st.write("Score ",df[df['img_url']==array_.values[0]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[0]]['genre'].values[0][1:-1].replace("'",''))
        
    with col2:
        st.image(array_.values[1], width=width)

    with mid2:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[1]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[1]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[1]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[1]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[1]]['genre'].values[0][1:-1].replace("'",''))

    col1,mid1,col2,mid2=st.columns([1,1.5,1,1.5])
    with col1:
        st.image(array_.values[2], width=width)

    with mid1:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[2]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[2]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[2]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[2]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[2]]['genre'].values[0][1:-1].replace("'",''))

    with col2:
        st.image(array_.values[3], width=width)

    with mid2:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[3]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[3]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[3]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[3]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[3]]['genre'].values[0][1:-1].replace("'",''))

    col1,mid1,col2,mid2=st.columns([1,1.5,1,1.5])

    with col1:
        st.image(array_.values[4], width=width)

    with mid1:
        st.markdown(f'''<div style='text-align: left;'><a href="{df[df['img_url']==array_.values[4]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[4]]['title'].values[0]}</a></div>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[4]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[4]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[4]]['genre'].values[0][1:-1].replace("'",''))

    with col2:
        st.image(array_.values[5], width=width)

    with mid2:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[5]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[5]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[5]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[5]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[5]]['genre'].values[0][1:-1].replace("'",''))

    col1,mid1,col2,mid2=st.columns([1,1.5,1,1.5])

    with col1:
        st.image(array_.values[6], width=width)

    with mid1:
        st.markdown(f'''<div style='text-align: left;'><a href="{df[df['img_url']==array_.values[6]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[6]]['title'].values[0]}</a></div>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[6]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[6]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[6]]['genre'].values[0][1:-1].replace("'",''))

    with col2:
        st.image(array_.values[7], width=width)

    with mid2:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[7]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[7]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[7]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[7]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[7]]['genre'].values[0][1:-1].replace("'",''))

    col1,mid1,col2,mid2=st.columns([1,1.5,1,1.5])

    with col1:
        st.image(array_.values[8], width=width)

    with mid1:
        st.markdown(f'''<div style='text-align: left;'><a href="{df[df['img_url']==array_.values[8]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[8]]['title'].values[0]}</a></div>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[8]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[8]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[8]]['genre'].values[0][1:-1].replace("'",''))

    with col2:
        st.image(array_.values[9], width=width)

    with mid2:
        st.markdown(f'''<p style='text-align: left;'><a href="{df[df['img_url']==array_.values[9]]['link'].values[0]}" title="More info">{df[df['img_url']==array_.values[9]]['title'].values[0]}</a></p>''',unsafe_allow_html=True)
        st.write("Episodes",df[df['img_url']==array_.values[9]]['episodes'].values[0])
        st.write("Score",df[df['img_url']==array_.values[9]]['score'].values[0])
        st.write("Genre: ",df[df['img_url']==array_.values[9]]['genre'].values[0][1:-1].replace("'",''))


def home_page():
    img = st.container()
    img.subheader('Type the name of an anime, choose whether you want the recommendation to be based on genre or story and wait for couple of seconds.')
    img.image('img/lelouch2.jpg')