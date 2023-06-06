import streamlit
import pandas
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega oat meal')
streamlit.text('🥗 kale, spinach & ricket smoothy')
streamlit.text('🐔 hard boiled free range egg')
streamlit.text('🥑🍞Avakado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

