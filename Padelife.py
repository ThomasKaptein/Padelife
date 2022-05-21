import pandas as pd
import streamlit as st
import plotly.express as px
import datetime
import numpy as np
from PIL import Image
import os
import math

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
tot_a = 0

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
        ###
        p_l = math.ceil(pers_l / 4)
        duur_l = st.radio(
        "Hoeveel minuten?",
        (60, 90, 120))
        
        tijd_l = st.radio(
        "Piek of dal tijd?",
        ('Piek uren', 'Dal uren'))
        if tijd_l == 'Piek uren':
            t_l = 36
        else:
            t_l = 32
        extra_l = st.multiselect(
            'Welke extra dingen zijn nodig (meerdere te selecteren)',
            ['Rackets', 'Ballen', 'Begeleiding'])
        if 'Rackets' in extra_l:
            tot_l = tot_l + pers_l * 5
        if 'Ballen' in extra_l:
            tot_l = tot_l + 5 * duur_l / 60
        if 'Begeleiding' in extra_l:
            tot_l = tot_l + 15 * duur_l / 60
        tot_l = tot_l + t_l * p_l * duur_l / 60
        st.write('Totaal laddertoernooi = ', tot_l)
st.write('Anders nog iets?')
koffie = st.checkbox('Welkomstdrankje')
if koffie:
    k = st.number_input(
        "Hoeveel?", min_value=1, max_value=16, value=4, step=1)
    tot_a = tot_a + k * 3
bier = st.checkbox('Consumptie achteraf')
if bier:
    b = st.number_input(
        "Hoeveel?", min_value=1, max_value=200, value=4, step=1)
    tot_a = tot_a + b * 3
cat = st.checkbox('Catering')
if cat:
    c = st.number_input(
        "Voor hoeveel pers?", min_value=1, max_value=200, value=4, step=1)
    tot_a = tot_a + c * 10
    st.write('@boy: voor het rekenvoorbeeld heb ik 10euro pp gekozen voor catering')

ver = st.checkbox('Vergaderen')
if ver:
    v = st.radio(
    "Hoe lang te vergaderen?",
    ("Halve dag (@Boy: ik zou aanraden hier uit een #uren te laten kiezen", "Hele dag", "Vergaderzaal halve dag", "Vergaderzaal hele dag"))
    st.write('vergaderen wordt nu nog niet mee gerekend ')

tot = tot_c + tot_l + tot_a
st.write('totaal:', tot)

