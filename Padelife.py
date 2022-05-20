import pandas as pd
import streamlit as st
import plotly.express as px
import datetime
import numpy as np
from PIL import Image
import os

st.set_page_config(
     page_title="Padelife keuzestress",
     page_icon='padelife_ico.ico',
     layout="wide")

image = Image.open('Padelife-logo.png')
col1, col2 = st.columns([3,4])
with col1:
    st.header("Padelife rekenmachine")
with col2: 
    st.image(image)

st.write("Wat wil je komen doen?")
st.write("Geef dat hieronder aan, ik wil graag een:")

tot = 0
tot_c = 0
tot_l = 0

col3,col4 = st.columns(2)
with col3:
    clin = st.checkbox('Clinic')
    if clin:
        st.write('Hmm, clinic zeg je...')
        pers_c = st.radio(
        "Leuk, met hoeveel personen dan?",
        (4, 6, 8))
        
        if pers_c == 8:
            p_c = 2
            st.write('Met 8 personen een clinic.')
                
                
        elif pers_c == 6:
            p_c = 2
            st.write("Met 6 personen een clinic.")
        else:
            p_c = 1
            st.write("Met 4 personen een clinic.")
        
        duur_c = st.radio(
        "Hoeveel minuten?",
        (60, 90))
        tijd_c = st.radio(
        "Piek of dal tijd?",
        ('Piek', 'Dal'))
        if tijd_c == 'Piek':
            t_c = 36
        else:
            t_c = 32
        extra_c = st.multiselect(
            'Welke extra dingen zijn nodig (meerdere te selecteren)',
            ['Rackets', 'Ballen'])
        if 'Rackets' in extra_c:
            tot_c = tot_c + pers_c * 5
        if 'Ballen' in extra_c:
            tot_c = tot_c + 5 * duur_c / 60
        tot_c = tot_c + t_c * p_c * duur_c / 60
        st.write('Totaal clinic = ', tot_c)
with col4:
    lad = st.checkbox('Laddertoernooi')
    if lad:
        st.write('Hmm, laddertoernooitje heeft je voorkeur...')
        pers_l = st.number_input(
        "Leuk, met hoeveel personen dan?", min_value=4, max_value=16, value=8, step=1)
        st.write('Met ', pers_l, ' personen een laddertoernooi.')
        duur_l = st.radio(
        "Hoeveel minuten?",
        (60, 90, 120))
        tijd_l = st.radio(
        "Piek of dal tijd?",
        ('Piek uren', 'Dal uren'))
        extra_l = st.multiselect(
            'Welke extra dingen zijn nodig (meerdere te selecteren)',
            ['Rackets', 'Ballen', 'Begeleiding'])

st.write('Anders nog iets?')
koffie = st.checkbox('Welkomstdrankje')
if koffie:
    st.number_input(
        "Hoeveel?", min_value=1, max_value=16, value=4, step=1)
bier = st.checkbox('Consumptie achteraf')
if bier:
    st.number_input(
        "Hoeveel?", min_value=1, max_value=200, value=4, step=1)
cat = st.checkbox('Catering')
if cat:
    st.number_input(
        "Voor hoeveel pers?", min_value=1, max_value=200, value=4, step=1)

ver = st.checkbox('Vergaderen')
if ver:
    st.radio(
    "Hoe lang te vergaderen?",
    ("Halve dag (@Boy: ik zou aanraden hier uit een #uren te laten kiezen", "Hele dag", "Vergaderzaal halve dag", "Vergaderzaal hele dag"))

st.write('totaal:', tot_c)

