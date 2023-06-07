# imports
import streamlit as st

# Create a title
st.title('Summary Page for Application')

#Give it a body
st.text("""
        This application was designed to show our students how to build an application using streamlit
        is to showcase how we can use Streamlit to create multi-page dashboards and effectively communicate
        information by returning images, we can grab any information from a database and have learned about how the
        info on mongodb . By creating a summary page, we can gain an understanding on how we can create these outlines
        how we create the functionality we do
        """)

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')
st.write("""
        We spent last week talking about SQL and today/tomorrow about NoSQL/MongoDB and about
        accessing a database and accessing info over a localized storage. Run times between the
        two are different. Database vs Local Memory gives winner to Database as large memory
        structures can slow down local host.
        """)