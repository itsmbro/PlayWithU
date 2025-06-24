import streamlit as st
import random

# Titolo e layout
st.set_page_config(page_title="🔥 Gioco Erotico di Coppia - Obbligo o Punizione", page_icon="❤️‍🔥", layout="centered")

st.markdown("""
<style>
    body {
        background-color: #1a1a1a;
        color: #ff4b5c;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #ff4b5c;
        color: white;
        font-weight: bold;
        height: 50px;
        font-size: 18px;
        border-radius: 10px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #ff758f;
        color: white;
    }
    .challenge-box {
        background-color: #2e2e2e;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        font-size: 22px;
        font-weight: 600;
        text-align: center;
        color: #ff9a76;
        box-shadow: 0 0 15px #ff4b5c;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔥 Gioco Erotico di Coppia: Obbligo & Punizione HARD 🔥")
st.write("Un gioco intenso e personalizzato per risvegliare la passione e far salire la tensione tra voi...")

# Ruoli
role = st.selectbox("Chi deve fare la sfida/punizione?", ["Lui (Michele)", "Lei (Martina)", "Mix (Alterna)"])

# Dati di sfide / punizioni hard personalizzate
punizioni_lui = [
    "Fermati prima di venire e siediti di fronte a lei. Lei muove i piedi lentamente sulla tua faccia, alternando tra avvicinarli e allontanarli, mentre ti comanda di baciarli o leccarli.",
    "Lei ti schiaccia leggermente con i piedi sulle palle, mentre ti bacia e lecca i piedi con passione.",
    "Seduto, fermati prima del piacere massimo, mentre lei ti soffoca con il sedere, alternando movimenti e pause.",
    "Lei ti lega i piedi e le mani, ti mette a pecora e ti lecca con un dito dietro, per almeno 5 minuti.",
    "Durante l'atto, lei ti comanda di non venire per 10 volte, usando i piedi o il sedere per controllarti e sedurti.",
]

punizioni_lei = [
    "Martina sdraiati a pancia in giù, Michele muoviti e fermati prima di venire per 10 volte, poi fallo ripetere a lei.",
    "Martina deve massaggiarti eroticamente con olio su piedi, glutei e tette per 5 minuti.",
    "Fai il 69 con lei, ma fermati prima di venire e lasciala dominare il ritmo con i piedi in bocca e sul viso.",
    "Legale piedi e mani e massaggiala usando solo la lingua, concentrandoti su piedi e glutei.",
    "Spalmale panna montata sul sedere e mangiala direttamente da lì, con fragole se vuoi.",
]

# Obblighi (possono sembrare punizioni se intesi così)
obblighi_generali = [
    "Leccami per 15 minuti senza fermarti.",
    "Massaggiami le zone erogene lentamente per 10 minuti.",
    "Fermati a 2 cm dal piacere e aspetta che sia l'altro a riprendere il ritmo.",
    "Gioca con i piedi dell'altro, alternando baci, leccate e leggere pressioni sul viso.",
    "Usa un cubetto di ghiaccio partendo dalla bocca e scendendo fino ai piedi dell'altro.",
]

# Funzione per pescare la sfida
def pesca_sfida(ruolo):
    if ruolo == "Lui (Michele)":
        return random.choice(punizioni_lui + obblighi_generali)
    elif ruolo == "Lei (Martina)":
        return random.choice(punizioni_lei + obblighi_generali)
    else:  # Mix
        return random.choice(punizioni_lui + punizioni_lei + obblighi_generali)

# Bottone per generare la sfida
if st.button("Genera la sfida erotica!"):
    sfida = pesca_sfida(role)
    st.markdown(f'<div class="challenge-box">{sfida}</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<p style="color:#ff4b5c; font-size: 14px; text-align:center; margin-top: 50px;">
Creato con amore e passione da ChatGPT 🔥<br>
Gioca responsabilmente e con rispetto reciproco!
</p>
""", unsafe_allow_html=True)
