# Imports
import streamlit as st

# Create a title
st.title("Summary Page for Application")
st.text("""
        This application was designed to show our students how to build an application using Streamlit. The goal
        is to showcase how we can use Streamlit to create multi-page dashboards and effectively communicate information.
        By returning images, we can grab any information from a  database and have learned about how the info is found in MongoDB.
        By creating this summary page, we gained understanding on how we can create these outlines on the way we write our code and
        how we create the functionality we do.
        """)

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')
st.write("""
         We spent last week talking over SQL and today/tomorrow talking over NoSQL/Document Oriented databases. We talked over the difference between
         accessing a database and accessing information over the localized storage. The run times for each differ from one another.
         Accessing a database was found to be faster than local memory, as the structure of over 28,000 rows slowed down overall accessiblility
         """)