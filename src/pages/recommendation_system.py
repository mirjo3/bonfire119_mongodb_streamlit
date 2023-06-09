import streamlit as st
import sys
import os
from pathlib import Path

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from model import dummy_func, Model

m = Model()

st.title('Recommended Cards:')

card_name = st.text_input(
    'Please enter the full name of the card you would like to see recommendations for:'
)
if st.button('Submit Card'):
    try:
        st.image(m.img_return(card_name))
        img_list = m.recommended_cards(card_name)
        st.write(
            f' Here are the 9 cards that would be recommended for your deck based off of the card {card_name.title()}'
        )
        col1, col2, col3 = st.columns(3)
        col1.image(img_list[0:3])
        col2.image(img_list[3:7])
        col3.image(img_list[7:11])
    except BaseException:
        st.error(f'''
                 {card_name.title()} is an invalid card.
                 Please retry with a valid card name. If the card name is valid,
                 try typing it exactly the way it appears on the card.''')