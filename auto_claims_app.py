from re import A
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pathlib import Path
import pathlib
from fastai.vision.widgets import *
from fastai.vision.all import *
from utils.ui import *
from helpers import *
from string import Template
from collections import defaultdict
pathlib.PosixPath = pathlib.WindowsPath

# @st.cache(allow_output_mutation = True)
def get_learners():
    pred_dict = {i.stem : load_learner(i).predict(img)[0] for i in (Path()/'models'/'pkls').ls()}
    return pred_dict


# Page introduction
introduction()

# Upload image
uploaded_file = upload_image()

if uploaded_file is not None:
    img = PILImage.create((uploaded_file))
    st.image(img.to_thumb(500,500), caption='Uploaded Image')
    pred_dict = get_learners()
else: 
    st.markdown('Please upload an image')


if st.button('Generate Claim Amount'):
    if uploaded_file is not None:
        get_damage_prediction(pred_dict)
    else :
        st.error('Please upload an image')
else: 
    st.write(f'Click the button to generate claim amout based on vehicle damage') 

st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)