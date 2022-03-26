import streamlit as st
from PIL import Image
from pathlib import Path

def introduction():
    # SETTING PAGE CONFIG TO WIDE MODE
    st.set_page_config(
        page_title="Auto Claims Predictor",
        page_icon=":car:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )


    st.title('Welcome to Auto Claims Predictor')
    st.subheader('Let us help you to get back to road safely and quickly')


    im_path = Path('C:/Users/drag88/averie-woodard-5d20kdvFCfA-unsplash.jpg')
    image = Image.open(im_path)
    st.image(image)

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

def upload_image():
    st.subheader('Please upload the image of your damaged car below')
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    return uploaded_file