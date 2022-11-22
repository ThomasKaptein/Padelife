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
    #clinic
    clin = st.checkbox('Clinic')
    if clin:
        st.write('Hmm, clinic zeg je...')
        pers_c = st.number_input(
        "Leuk, met hoeveel personen dan?", min_value=4, max_value=24, value=8, step=1)
        
        #aantal banen op basis van aantal personen:
        #p_c = math.ceil(pers_c / 4)
        #train_c = math.ceil(pers_c / 8)
        st.write('Advies: 4 personen per baan, 1 trainer per 2 banen. Bij vragen mailen naar info@padelife.nl')
        baan_c = st.number_input(
        "Hoeveel banen zijn er nodig?", min_value=1, max_value=6, value=2, step=1)
        
        duur_c = st.radio(
        "Hoeveel minuten?",
        (60, 90))
        tijd_c = st.radio(
        "Piek of dal tijd? (Piek = ma-vrij vanaf 16uur en zat-zo, Dal = ma - vrij tot 16uur)",
        ('Piek', 'Dal'))
        if tijd_c == 'Piek':
            t_c = 45
        else:
            t_c = 37
            
        train_c = st.number_input(
        "Hoeveel trainers?", min_value=1, max_value=6, value=1, step=1)
        extra_c = st.multiselect(
            'Welke extra dingen zijn nodig',
            ['Rackets'])
        if 'Rackets' in extra_c:
            tot_c = tot_c + pers_c * 5
       
        trainer = 40 * train_c
        tot_c = round((tot_c + (t_c * baan_c + trainer) * duur_c / 60),2)
        totp_c = round((tot_c / pers_c),2)
        st.write('Totaal banen = ', baan_c, 'banen * ', t_c, 'euro per uur incl. 5 euro per uur voor de ballen = ', t_c*baan_c*duur_c / 60)
        st.write('Trainer = ', trainer * duur_c / 60, 'euro tarief trainer')
        st.write('Totaal clinic (incl. eventueel rackets)= ', tot_c)
        st.write('Totaal clinic per persoon= ', totp_c)
with col4:
    #toernooi
    lad = st.checkbox('Toernooi toernooi toernooi')
    if lad:
        st.write('Voor een toernooi is het minimale aantal spelers 12 en zijn er minimaal 3 banen nodig.')
        pers_l = st.number_input(
        "Leuk, met hoeveel personen?", min_value=12, max_value=24, value=12, step=1)
        st.write('Met ', pers_l, ' personen een toernooi.')
        
        #p_l = math.ceil(pers_l / 4)
        baan_l = st.number_input(
        "Hoeveel banen zijn er nodig?", min_value=3, max_value=6, value=3, step=1)
        duur_l = st.radio(
        "Hoeveel minuten?",
        (60, 90, 120))
        
        tijd_l = st.radio(
        "Piek of dal tijd? (Piek = ma-vrij vanaf 16uur en zat-zo, Dal = ma - vrij tot 16uur)",
        ('Piek uren', 'Dal uren'))
        if tijd_l == 'Piek uren':
            t_l = 45
        else:
            t_l = 37
        extra_l = st.multiselect(
            'Welke extra dingen zijn gewenst?',
            ['Rackets'])
        if 'Rackets' in extra_l:
            tot_l = tot_l + pers_l * 5
        
        begeleiding = 15 * duur_l / 60
        tot_l = round((tot_l + t_l * baan_l * duur_l / 60 + begeleiding),2)
        st.write('Totaal banen = ', baan_l, 'banen * ', t_l, 'euro per uur incl. 5 euro per uur voor de ballen = ', t_l*baan_l*duur_l / 60)
        st.write('Toernooileider = ', begeleiding, 'euro tarief toernooileider')
        st.write('Totaal toernooi (incl. eventueel rackets)= ', tot_l)
        st.write('Totaal toernooi per persoon= ', round((tot_l / pers_l),2))
    #baanhuur
    b = st.checkbox('Baanhuur')
    if b:
        st.write('Baanhuur heeft je voorkeur...')
        pers_b = st.number_input(
        "Met hoeveel personen?", min_value=4, max_value=None, value=8, step=1)
        st.write('Met ', pers_b, ' personen banen huren.')
        
        #p_l = math.ceil(pers_l / 4)
        baan_b = st.number_input(
        "Hoeveel banen?", min_value=1, max_value=6, value=3, step=1)
        duur_b = st.radio(
        "Hoelang (in minuten)?",
        (60, 90, 120, 180, 210, 240))
        
        tijd_b = st.radio(
        "Piek of dal tijd? (Piek = ma-vrij vanaf 16uur en zat-zo, Dal = ma - vrij tot 16uur)",
        ('Piek tijd', 'Dal tijd'))
        if tijd_b == 'Piek tijd':
            t_b = 40
        else:
            t_b = 32
        #counter om extra's bij te houden
        e = 0
        extra_b = st.multiselect(
            'Welke extra dingen zijn nodig',
            ['Rackets', 'Ballen'])
        if 'Rackets' in extra_b:
            tot_b = tot_b + pers_b * 5
            e = 1
        if 'Ballen' in extra_b:
            tot_b = tot_b + baan_b * 5
            e = e + 2
        
        tot_b = round((tot_b + t_b * baan_b * duur_b / 60),2)
        st.write('Totaal banen = ', baan_b, 'banen a ', t_b, 'euro per uur = ', t_b*baan_b*duur_b / 60)
        #st.write('Toernooileider = ', begeleiding, 'euro tarief toernooileider')
        if e == 1:
            st.write('Totaal baanhuur (incl. rackets)= ', tot_b)
            st.write('Totaal baanhuur (incl. rackets) per persoon= ', round((tot_b / pers_b),2))
        elif e == 2:
            st.write('Totaal baanhuur (incl. ballen)= ', tot_b)
            st.write('Totaal baanhuur (incl. ballen)= ', round((tot_b / pers_b),2))
        elif e == 3:
            st.write('Totaal baanhuur (incl. rackets en ballen)= ', tot_b)
            st.write('Totaal baanhuur (incl. rackets en ballen)= ', round((tot_b / pers_b),2))
        else:
            st.write('Totaal baanhuur = ', tot_b)
            st.write('Totaal baanhuur = ', round((tot_b / pers_b),2))
            
            
        
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

tot_a = round(tot_a, 2)
st.write('Subtotaal van de categorie "Anders nog iets?" = ', tot_a, 'euro')
ver = st.checkbox('Vergaderen')
if ver:
    st.write("Wat voor plek wil je?")
    flex = st.checkbox('Flexplek')
    if flex:
        fl = st.number_input(
        "Hoeveel plekken?", min_value=1, max_value=16, value=4, step=1)
        v = st.radio(
        "Hoe lang?",
        ("Halve dag", "Hele dag"))
        if 'Halve dag' in v:
            tot_v = tot_v + 15 * fl
        if 'Hele dag' in v:
            tot_v = tot_v + 25 * fl
        zaal = st.checkbox('Prive vergaderzaal')
        if zaal:
            z = st.number_input(
            "Voor hoeveel personen?", min_value=1, max_value=16, value=4, step=1)
            t_z = st.radio(
            "Hoe lang te vergaderen?",
            ("Halve dag", "Hele dag"))
            if 'Halve dag' in t_z:
                tot_v = tot_v + 30
            if 'Hele dag' in t_z:
                tot_v = tot_v + 50
    w_life = st.checkbox('Worklife afhuren')
    if w_life:
        w = st.number_input(
        "Hoeveel personen komen er?", min_value=1, max_value=None, value=4, step=1)
        t_w = st.radio(
        "Hoe lang Worklife te gebruiken?",
        ("Halve dag a 4 uur", "Hele dag van 9uur - 19uur"))
        if 'Halve dag a 4 uur' in t_w:
            tot_v = tot_v + 400 * 1.21
        if 'Hele dag van 9uur - 19uur' in t_w:
            tot_v = tot_v + 950 * 1.21
    st.write('Totaal vergaderen =', tot_v)
            

tot = tot_c + tot_l + tot_a + tot_b + tot_v
st.write('Totaal clinic:', tot_c, '+ totaal toernooi:', tot_l, ' + totaal losse baanhuur:', tot_b, ' + totaal anders nog iets:', tot_a, ' + totaal vergaderen:', tot_v, '=',tot)
st.write('Totaal =', tot)

