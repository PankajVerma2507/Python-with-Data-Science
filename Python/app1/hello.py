# streamlit run app1/hello.py
import streamlit as st
from PIL import Image


st.title("Sample App")
st.header("This is head")

image = st.camera_input("Take a picture")
if image:
    im = Image.open(image)
    color = st.color_picker("Pick a color","#00f900")

    
    # purple gradient image
    im2 = Image.new("RGB",im.size, color)
    # overlay the two images
    im = Image.blend(im,im2,0.5)
    
    

    st.sidebar.image(im)
    filename = st.text_input("Save as","image.png")
    if st.button("save"):
        
        im.save(filename)
        st.snow()
        st.balloons()