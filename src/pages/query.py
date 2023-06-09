# Imports first:
from pathlib import Path
import streamlit as st
import sys
import os

# Grab the filepath again, just like our image_return.py file:
filepath = os.path.join(Path(__file__).parents[1])

# Insert filepath into system:
sys.path.insert(0, filepath)

# Import the ToMongo class:
from to_mongo import ToMongo

# Instantiate the class:
c = ToMongo()

# Now we query the database

"""
This is to return information about an item from our database to a user in a friendly format

Query the database based off a user input, then display that information back to them.

Why is this important?

When a user wants to search up information, but we don't have a local file to reference it to, we can
use a query function to return that data instead.

Also, when building dashboards and applications, knowing how to allow a user to retrieve information is critical.

How will we go about this?
First, we will use the user input to search the database
When we find a match, we will just return all information about that match to the user.
The .find() function will give us everything we need!
"""

answer = st.text_input('Enter a card name:', value = 'Sol Ring')
st.write(list(c.cards.find({'name':answer})))