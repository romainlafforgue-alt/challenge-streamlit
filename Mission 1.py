import streamlit as st
import pandas as pd

# Charger le dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

st.title("Bienvenue sur le site web de Romain")

# Menu déroulant
arrondissement = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    df["pickup_borough"].dropna().unique()
)

st.write(f"Tu as choisis: {arrondissement}")

# Dictionnaire d'images
images = {
    "Manhattan": "images/manhattan.jpg",
    "Bronx": "images/bronx.jpg",
    "Brooklyn": "images/brooklyn.jpg",
    "Queens": "images/queens.jpg"
}

# Affichage image
if arrondissement in images:
    st.image(images[arrondissement], use_container_width=True)
else:
    st.write("Pas d'image disponible")