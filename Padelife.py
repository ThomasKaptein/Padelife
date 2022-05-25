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
        pers_c = st.number_input(
        "Leuk, met hoeveel personen dan?", min_value=4, max_value=24, value=8, step=1)
        
        p_c = math.ceil(pers_c / 4)
        #train_c = math.ceil(pers_c / 8)
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
            
        train_c = st.number_input(
        "Hoeveel trainers?", min_value=1, max_value=6, value=1, step=1)
        extra_c = st.multiselect(
            'Welke extra dingen zijn nodig (meerdere te selecteren)',
            ['Rackets'])
        if 'Rackets' in extra_c:
            tot_c = tot_c + pers_c * 5
       
        trainer = 30 * train_c
        tot_c = tot_c + (t_c * p_c + trainer) * duur_c / 60
        totp_c = tot_c / pers_c
        st.write('Totaal clinic = 5 euro ballen per uur per baan * ', tot_c)
        st.write('Totaal clinic = ', tot_c)
        st.write('Totaal clinic per persoon= ', totp_c)
with col4:
    lad = st.checkbox('Toernooi toernooi toernooi')
    if lad:
        st.write('Hmm, toernooitje heeft je voorkeur...')
        pers_l = st.number_input(
        "Leuk, met hoeveel personen dan?", min_value=12, max_value=24, value=12, step=1)
        st.write('Met ', pers_l, ' personen een toernooi.')
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
        st.write('Totaal toernooi = ', tot_l)
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
cat = st.checkbox('Catering (excl. drank)')
if cat:
    c = st.number_input(
        "Voor hoeveel pers?", min_value=1, max_value=200, value=4, step=1)
    c1 = st.number_input(
        "Bedrag per persoon?", min_value=5, max_value=50, value=5, step=1)
    tot_a = tot_a + c * c1
    #st.write('@boy: voor het rekenvoorbeeld heb ik 10euro pp gekozen voor catering')

ver = st.checkbox('Vergaderen')
if ver:
    st.write("Wat voor plek wil je?")
    flex = st.checkbox('Flexplek')
    if flex:
        fl = st.number_input(
        "Hoeveel?", min_value=1, max_value=16, value=4, step=1)
        v = st.radio(
        "Hoe lang te vergaderen?",
        ("Halve dag", "Hele dag", "Vergaderzaal halve dag", "Vergaderzaal hele dag"))
        st.write('nog toevoegen: optie om eigen vergaderzaal')

tot = tot_c + tot_l + tot_a
st.write('totaal:', tot)

