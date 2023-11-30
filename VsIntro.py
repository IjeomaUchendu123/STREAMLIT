import streamlit as st
st.title("Name of jupiterfile e.g ML project")
st.header("Heading")
st.subheader("Introduction")
st.text("Welcome to streamlit class")
st.markdown("## Subheading")
st.caption("caption")
st.code("print('hello world')")
st.latex(r'''a^2 + b^2 = c^2''')
st.button('click me!')
st.subheader("AVAILABLE COURSES")
st.checkbox("Data Analytics", value= True)
st.checkbox("Data Science")
st.radio("Gender", ["Male", "Female"])
st.image("https://scontent.flos2-1.fna.fbcdn.net/v/t39.30808-6/304128219_486207943512198_1365860302696096819_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFhNPOxcULjhfiakw1Xqs3vxrGIHDgArPTGsYgcOACs9OKpOsNjKh8qy2iOZpRNs7E&_nc_ohc=PuJdDrTPVi4AX96prGR&_nc_zt=23&_nc_ht=scontent.flos2-1.fna&oh=00_AfC5hJm5fa5-5ZV80EIKlcagby96FbwI3AhciXpaD5Oiqg&oe=656A581B", width=200)
#using image from your system and not a link like the above
from PIL import Image
pic = Image.open("Ijeoma's Image.jpg")
st.image(pic, caption="Ijeoma's Image", width=200)
st.success("Registration Successful")
st.error("Invalid entry")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.info('Hint: Notice me')
st.warning("I am warning you")
st.help(range)
#Visualization
import pandas as pd
import numpy as np
dataframe= np.random.randn(10, 20)
st.dataframe(dataframe)
chart_data = pd.DataFrame(
		 	 np.random.randn(20, 3),
		    columns=['a', 'b', 'c'])
st.line_chart(chart_data)
#creating a bar chart
chart_data = pd.DataFrame(
		 	 np.random.randn(50, 3),
		    columns=['a', 'b', 'c'])
st.bar_chart(chart_data)
#creating map

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)
#Creating a radio button

genre = st.radio(
        "What's your favorite movie genre",
       ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
      st.write('You selected comedy.')
else:
      st.write("You didn't select comedy.")
      #using select box
option = st.selectbox(
	     'How would you like to be contacted?',
	     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)  
values = st.slider(
 	     'Select a range of values',
	     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
#TEXT

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
#NUMBER

number = st.number_input('Insert a number')
st.write('The current number is ',number)