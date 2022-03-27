import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pathlib import Path
import pathlib
from fastai.vision.widgets import *
from fastai.vision.all import *
from utils.ui import *
#from models.helpers import *
#from models import helpers
from helpers import *
from models.prediction import Predict
# from fastbook import *


introduction()
uploaded_file = upload_image()

if uploaded_file is not None:
    img = PILImage.create((uploaded_file))
    st.image(img.to_thumb(500,500), caption='Uploaded Image')
else: 'Please upload an image'


temp = Path()/'models'/'pkl'/'damage.pkl'
pathlib.PosixPath = pathlib.WindowsPath

car_damage = load_learner(Path()/'models'/'pkl'/'damage.pkl')

if st.button('Classify'):
    pred, pred_idx, probs = car_damage.predict(img)
    st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')
else: 
    st.write(f'Click the button to classify') 
