import streamlit as st # Aliasing the streamlit app import as st

st.title('Bonfire-119 MTG Tracer Application')
st.text('My first application that uses pandas, streamlit, mongoDB and python to marry together a magic application')

st.header('Here are the different pages of my application:')
st.subheader('Image Return')
st.text('Image Return: Returns an image of the requested card')

st.subheader('Summary')
st.text('Summary: IT is a summarization page of all the inner workings of my application')

st.subheader('Recommender')
st.text('A rrecommendation system that we will build if we have time tomorrow!')

'''
pip install streamlit
$ cd src
$ streamlit run front_page.py
'''