import streamlit as st
from PIL import Image
from pathlib import Path
import functools
from collections import defaultdict
import yaml

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


    im_path = Path()/'utils'/'averie-woodard-5d20kdvFCfA-unsplash.jpg'
    image = Image.open(im_path)
    st.image(image)

    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

def upload_image():
    st.subheader('Please upload the image of your damaged car below')
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    return uploaded_file

@st.cache(persist=True, allow_output_mutation = True)
def claim_amts():
    with open (Path()/'config.yaml') as f:
        claims_amts = yaml.load(f, Loader=yaml.FullLoader)['claim_amts']
        return claims_amts


def get_damage_prediction(pred_dict):
    val = []
    for k, v in pred_dict.items():
        if v == 'n': pred_dict[k] = 'No'
        elif v == '00-damage': pred_dict[k] = 'Car is damaged'
        elif v == 'y': pred_dict[k] = 'Yes'
        else: pred_dict[k] = 'Car is not damaged'


    # claim value and damage
    dd = defaultdict(tuple)
    for d in (pred_dict, claim_amts()): 
        for key, value in d.items():
            dd[key] += (value,)

    # claim total value
    for k,v in dd.items():
        if dd[k][0] == 'Yes':
            val.append(dd[k][1])
    try:
        claim_val = functools.reduce(lambda x,y : x+y, val)
    except:
        claim_val = 0

    pred_dict_group = defaultdict(list)
    for k, v in sorted(pred_dict.items()):  
        if k != 'damage':
            pred_dict_group[v].append(k)
    st.subheader(pred_dict['damage'])

    if len(pred_dict_group['Yes']) == 0:
            st.markdown('Could not identify areas of car damage')        
    else:            
        for k, v in sorted(pred_dict_group.items()):
            if k == 'Yes':
                for i in v:
                    if i == 'bumper_dent':
                        st.markdown(f'Bumper is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'door_dent':
                        st.markdown(f'Door is dented with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'door_scratch':
                        st.markdown(f'Door is scratched with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'front_whole':
                        st.markdown(f'Front whole is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'glass_shatter':
                        st.markdown(f'Glass is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'head_lamp':
                        st.markdown(f'Head lamp is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'side_whole':
                        st.markdown(f'Side whole is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                    elif i == 'tail_lamp':
                        st.markdown(f'Tail lamp is damaged with an estimated repair cost of ${claim_amts()[i]:,}')
                        
    st.markdown(f'Total estimated repair cost is ${claim_val:,}')