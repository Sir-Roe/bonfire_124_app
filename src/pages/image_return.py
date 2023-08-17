#imports for image return page
import streamlit as st
import requests
import os
import sys
from PIL import Image
from pathlib import Path
from io import BytesIO

filepath = os.path.join(Path(__file__).parents[1])

sys.path.insert(0,filepath)
from to_mongo import ToMongo

st.title("Image Return Page")

c=ToMongo()


answer = st.text_input("Enter a Card Name", value= 'Sol Ring')
#connect to mongo and get the IMAGE URI
try:
    card=list(c.cards.find({'name':answer}))[0]['image_uris']['normal']
    st.image(Image.open(BytesIO(requests.get(card).content)))
except:
    print('error finding card')