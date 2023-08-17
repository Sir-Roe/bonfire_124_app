import plotly.express as px
from pathlib import Path
import streamlit as st
import pandas as pd
import os

#establish a filepath to the orcale_cards.csv file
filepath=os.path.join(Path(__file__).parents[1], 'data\oracle_cards.csv')
df = pd.read_csv(filepath,low_memory=False)

#take in an User input
viz_to_use=['scatterplot','histogram','bar chart']
answer=st.selectbox('select a column to visualize',options=list(df.columns))
if answer:
    try:
        st.plotly_chart(px.histogram(df,answer))
    except BaseException:
        st.error(f'''
                 {answer.title()} could not be plotted into a histogram!
                 ''')
