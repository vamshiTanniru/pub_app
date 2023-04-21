import streamlit as st
import os
import pandas as pd
import time
from matplotlib import image



#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
dir_of_interest = os.path.join(FILE_DIR1,"resources","data","open_pubs_clean.csv")
dir_of_interest1 = os.path.join(FILE_DIR1,"resources","image","vamshi.jpg")
pub_img = os.path.join(FILE_DIR1,"resources","image","pub.jpg")

st.set_page_config(layout="wide")
st.title(':white[🍻Pubs In United Kingdom To Have Some Drink And Chillout🍻]')
st.subheader( " My self : ***:green[TANNIRU Vamshi Prakash]***")
st.snow()


st.subheader(":red[You can reach me]")

col1,col2,col3=st.columns(3, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/vamshi-prakash/)")
with col2:
    st.subheader("[GitHub](https://github.com/vamshiTanniru)")
with col3:
    if st.button('Bio'):
      img = image.imread(dir_of_interest1)
      st.markdown('''Name: T.Vamshiprakash
      Education : B.tech(ECE)''')
      st.image(img,caption='decent boy')



df = pd.read_csv(dir_of_interest)

#Page Heading
st.header("🍾All Pubs Information in United Kingdom🍸")

with st.expander(label='Click Here to see the dataset overview',expanded=False):
     img1 = image.imread(pub_img)
     st.image(img1)
     st.balloons()
     st.dataframe(df)


#Unique Bars and Local Authorities
unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=True)

if option=='Number of Pubs':
    st.subheader(f"Total Pubs in UK: :blue[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in UK: :blue[{df['postcode'].nunique()}]")
else:
    st.subheader(f"Total Local Authorities in UK :blue[{df['local_authority'].nunique()}]")

st.subheader(":red[🥂🍹Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind and stories to be told🥂🍹.]")



