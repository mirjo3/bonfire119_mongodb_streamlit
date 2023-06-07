# Imports needed
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

# Creates a filepath to the system for the main folder where the path lives
filepath = os.path.join(Path(__file__).parents[1])

# This allows me to import diretly from the filepath I am wanting
sys.path.insert(0, filepath)
from to_mongo import ToMongo

#When I click on page:
# We set the title of the page
st.title("Image Return Page")

#We create a mongo class
c = ToMongo()

# Then we take import from user
answer = st.text_input("Enter a Card Name:", value='Sol Ring')

# Transform that input into a card name
card = list(c.cards.find({'name':answer}))[0]['image_uris']['normal']

# Return an image
st.image(Image.open(BytesIO(requests.get(card).content)))

#print(filepath)