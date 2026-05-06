# ==============================
# IMPORTATION DES BIBLIOTHÈQUES
# ==============================

# Streamlit = création de l'application web
import streamlit as st

# Pandas = manipulation des données
import pandas as pd

# Seaborn = création de la heatmap
import seaborn as sns

# Matplotlib = affichage graphique
import matplotlib.pyplot as plt

# ==============================
# TITRE DE L'APPLICATION
# ==============================

# Création du titre principal
st.title("Manipulation de données et création de graphiques")

# ==============================
# CHOIX DU DATASET
# ==============================

# Menu déroulant pour choisir le dataset
dataset = st.selectbox(
    "Quel dataset veux-tu utiliser",
    ["planets"]
)


# ==============================
# CHARGEMENT DU DATASET
# ==============================

# Lecture du fichier CSV
df = pd.read_csv("planets.csv")


# Affichage des premières lignes du dataset
st.write("Aperçu du dataset")

st.dataframe(df.head())

# ==============================
# CHOIX DES COLONNES
# ==============================

# Menu déroulant pour choisir la colonne X
colonne_x = st.selectbox(
    "Choisissez la colonne X",
    df.columns
)


# Menu déroulant pour choisir la colonne Y
colonne_y = st.selectbox(
    "Choisissez la colonne Y",
    df.columns
)

# ==============================
# CHOIX DU GRAPHIQUE
# ==============================

# Menu déroulant pour choisir le type de graphique
graphique = st.selectbox(
    "Quel graphique veux-tu utiliser ?",
    ["scatter_chart", "bar_chart", "line_chart"]
)

# ==============================
# AFFICHAGE DU GRAPHIQUE
# ==============================

# Sous-titre
st.subheader("Mon graphique")


# Si l'utilisateur choisit scatter_chart
if graphique == "scatter_chart":

    st.scatter_chart(
        df,
        x=colonne_x,
        y=colonne_y
    )


# Si l'utilisateur choisit bar_chart
elif graphique == "bar_chart":

    st.bar_chart(
        df,
        x=colonne_x,
        y=colonne_y
    )


# Si l'utilisateur choisit line_chart
elif graphique == "line_chart":

    st.line_chart(
        df,
        x=colonne_x,
        y=colonne_y
    )

# ==============================
# CHECKBOX MATRICE DE CORRÉLATION
# ==============================

# Création de la checkbox
afficher_corr = st.checkbox(
    "Afficher la matrice de corrélation"
)

# ==============================
# MATRICE DE CORRÉLATION
# ==============================

# Si la checkbox est cochée
if afficher_corr:

    # Sous-titre
    st.subheader("Ma matrice de corrélation")


    # Sélection des colonnes numériques
    df_numeric = df.select_dtypes(include="number")


    # Calcul de la corrélation
    correlation = df_numeric.corr()


    # Création de la figure matplotlib
    fig, ax = plt.subplots()


    # Création de la heatmap
    sns.heatmap(
        correlation,
        annot=True,
        ax=ax
    )


    # Affichage dans Streamlit
    st.pyplot(fig)
