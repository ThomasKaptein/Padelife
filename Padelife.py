import pandas as pd
import streamlit as st
import plotly.express as px
import datetime
import numpy as np
from PIL import Image
import os
import math

st.set_page_config(
     page_title="Padelife/Worklife rekenmachine",
     page_icon='padelife_ico.ico',
     layout="wide")

image = Image.open('Padelife-logo.png')
image1 = Image.open('Worklife-logo.png')
col1, col2, col3 = st.columns([3,4,4])
with col1:
    st.header("Padelife / Worklife")
    st.write("Rekenmachine")
with col2: 
    st.image(image)
with col3: 
    st.image(image1)

st.write("Wat wil je komen doen?")
st.write("Geef dat hieronder aan, ik wil graag een:")

tot = 0
tot_c = 0
tot_l = 0
tot_a = 0
tot_b = 0
tot_v = 0

col3,col4 = st.columns(2)
with col3:
    clin = st.checkbox('Clinic')
    if clin:
        st.write('Hmm, clinic zeg je...')
        pers_c = st.number_input(
        "Leuk, met hoeveel personen dan?", min_value=4, max_value=24, value=8, step=1)
        
        #aantal banen op basis van aantal personen:
        #p_c = math.ceil(pers_c / 4)
        #train_c = math.ceil(pers_c / 8)
        baan_c = st.number_input(
        "Hoeveel banen zijn er nodig?", min_value=1, max_value=6, value=2, step=1)
        
        duur_c = st.radio(
        "Hoeveel minuten?",
        (60, 90))
        tijd_c = st.radio(
        "Piek of dal tijd?",
        ('Piek', 'Dal'))
        if tijd_c == 'Piek':
            t_c = 41
        else:
            t_c = 37
            
        train_c = st.number_input(
        "Hoeveel trainers?", min_value=1, max_value=6, value=1, step=1)
        extra_c = st.multiselect(
            'Welke extra dingen zijn nodig',
            ['Rackets'])
        if 'Rackets' in extra_c:
            tot_c = tot_c + pers_c * 5
       
        trainer = 30 * train_c
        tot_c = tot_c + (t_c * baan_c + trainer) * duur_c / 60
        totp_c = tot_c / pers_c
        st.write('Totaal banen = ', baan_c, 'banen * ', t_c, 'euro per uur incl. 5 euro per uur voor de ballen = ', t_c*baan_c*duur_c / 60)
        st.write('Trainer = ', trainer * duur_c / 60, 'euro tarief trainer')
        st.write('Totaal clinic (incl. eventueel rackets)= ', tot_c)
        st.write('Totaal clinic per persoon= ', totp_c)
with col4:
    lad = st.checkbox('Toernooi toernooi toernooi')
    if lad:
        st.write('Hmm, toernooitje heeft je voorkeur...')
        pers_l = st.number_input(
        "Leuk, met hoeveel personen?", min_value=12, max_value=24, value=12, step=1)
        st.write('Met ', pers_l, ' personen een toernooi.')
        
        #p_l = math.ceil(pers_l / 4)
        baan_l = st.number_input(
        "Hoeveel banen zijn er nodig?", min_value=1, max_value=6, value=3, step=1)
        duur_l = st.radio(
        "Hoeveel minuten?",
        (60, 90, 120))
        
        tijd_l = st.radio(
        "Piek of dal tijd?",
        ('Piek uren', 'Dal uren'))
        if tijd_l == 'Piek uren':
            t_l = 41
        else:
            t_l = 37
        extra_l = st.multiselect(
            'Welke extra dingen zijn nodig',
            ['Rackets'])
        if 'Rackets' in extra_l:
            tot_l = tot_l + pers_l * 5
        
        begeleiding = 15 * duur_l / 60
        tot_l = tot_l + t_l * baan_l * duur_l / 60 + begeleiding
        st.write('Totaal banen = ', baan_l, 'banen * ', t_l, 'euro per uur incl. 5 euro per uur voor de ballen = ', t_l*baan_l*duur_l / 60)
        st.write('Toernooileider = ', begeleiding, 'euro tarief toernooileider')
        st.write('Totaal toernooi (incl. eventueel rackets)= ', tot_l)
        st.write('Totaal toernooi per persoon= ', tot_l / pers_l)
    b = st.checkbox('Baanhuur')
    if b:
        st.write('Baanhuur heeft je voorkeur...')
        pers_b = st.number_input(
        "Met hoeveel personen?", min_value=4, max_value=24, value=8, step=1)
        st.write('Met ', pers_b, ' personen banen huren.')
        
        #p_l = math.ceil(pers_l / 4)
        baan_b = st.number_input(
        "Hoeveel banen?", min_value=1, max_value=6, value=3, step=1)
        duur_b = st.radio(
        "Hoeveel minuten?",
        (60, 90, 120))
        
        tijd_b = st.radio(
        "Piek of dal tijd?",
        ('Piek uren', 'Dal uren'))
        if tijd_b == 'Piek uren':
            t_b = 36
        else:
            t_b = 32
        extra_b = st.multiselect(
            'Welke extra dingen zijn nodig',
            ['Rackets', 'Ballen'])
        if 'Rackets' in extra_b:
            tot_b = tot_b + pers_b * 5
        if 'Ballen' in extra_b:
            tot_b = tot_b + baan_b * 5
        
        tot_b = tot_b + t_b * baan_b * duur_b / 60 
        st.write('Totaal banen = ', baan_b, 'banen * ', t_b, 'euro per uur = ', t_b*baan_b*duur_b / 60)
        #st.write('Toernooileider = ', begeleiding, 'euro tarief toernooileider')
        st.write('Totaal toernooi (incl. rackets en ballen)= ', tot_b)
        st.write('Totaal toernooi (incl. rackets en ballen) per persoon= ', tot_b / pers_b)
        
st.header('Anders nog iets?')
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
        "Hoe lang?",
        ("Halve dag", "Hele dag"))
        if 'Halve dag' in v:
            tot_v = tot_v + 15 * fl
        if 'Hele dag' in v:
            tot_v = tot_v + 25 * fl
    zaal = st.checkbox('Vergaderzaal')
    if zaal:
        z = st.number_input(
        "Voor hoeveel personen?", min_value=1, max_value=16, value=4, step=1)
        t_z = st.radio(
        "Hoe lang te vergaderen?",
        ("Halve dag", "Hele dag"))
        if 'Halve dag' in t_z:
            tot_v = tot_v + 80
        if 'Hele dag' in t_z:
            tot_v = tot_v + 150
    w_life = st.checkbox('Worklife afhuren')
    if w_life:
        w = st.number_input(
        "Hoeveel personen komen er?", min_value=1, max_value=16, value=4, step=1)
        t_w = st.radio(
        "Hoe lang Worklife te gebruiken?",
        ("Halve dag", "Hele dag"))
        if 'Halve dag' in t_w:
            tot_v = tot_v + 250
        if 'Hele dag' in t_w:
            tot_v = tot_v + 500
    st.write('Totaal vergaderen =', tot_v)
            

tot = tot_c + tot_l + tot_a + tot_b + tot_v
st.write('Totaal:', tot)

