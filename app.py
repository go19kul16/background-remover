import streamlit as st
from rembg import remove 
from PIL  import Image

@st.cache_data
def load_image(image_file):
    img=Image.open(image_file)
    return img
col1,col2=st.columns(2)

st.header(":green[BACKGROUND] REMOVER")
st.subheader(":red[Upload Your Image]")
input_file=st.file_uploader("",type=['jpg','jpeg','png'])
if input_file is not None:
    img=load_image(input_file)
    
    input=Image.open(input_file)
    output=remove(input)
    st.image(output)
    with open ('output.png','rb') as file:
        btn=st.download_button(label="Download Image",data=file,file_name="output.png",mime='image/png')
