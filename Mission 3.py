# ==============================
# IMPORTATION DES BIBLIOTHÈQUES
# ==============================

# Streamlit = création de l'application web
import streamlit as st

# Pandas = manipulation des données
import pandas as pd


# ==============================
# CONFIGURATION DE LA PAGE
# ==============================

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Application Chat",
    layout="wide"
)


# ==============================
# CHARGEMENT DU FICHIER CSV
# ==============================

# Lecture du fichier users.csv
users = pd.read_csv("users.csv")


# ==============================
# SESSION STATE
# ==============================

# Vérifie si l'utilisateur est connecté
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


# Vérifie si le username existe
if "username" not in st.session_state:

    st.session_state.username = ""


# Vérifie la page actuelle
if "page" not in st.session_state:

    st.session_state.page = "Accueil"


# ==============================
# PAGE DE CONNEXION
# ==============================

# Si l'utilisateur n'est pas connecté
if st.session_state.logged_in == False:

    # Titre principal
    st.title("Login")


    # Champ username
    username = st.text_input(
        "Username"
    )


    # Champ password
    password = st.text_input(
        "Password",
        type="password"
    )


    # Bouton login
    if st.button("Login"):


        # Vérifie si les champs sont remplis
        if username == "" or password == "":

            st.warning(
                "Les champs username et mot de passe doivent être remplis"
            )


        # Vérification des identifiants
        else:

            user = users[
                (users["name"] == username)
                &
                (users["password"] == password)
            ]


            # Si utilisateur trouvé
            if not user.empty:

                st.session_state.logged_in = True

                st.session_state.username = username

                st.rerun()


            # Si erreur login
            else:

                st.error(
                    "Identifiant ou mot de passe incorrect"
                )


# ==============================
# APPLICATION APRÈS CONNEXION
# ==============================

# Si utilisateur connecté
else:


    # ==============================
    # SIDEBAR
    # ==============================

    with st.sidebar:


        # Bouton déconnexion
        if st.button("Déconnexion"):

            st.session_state.logged_in = False

            st.session_state.username = ""

            st.session_state.page = "Accueil"

            st.rerun()


        # Message de bienvenue
        st.write(
            f"Bienvenue *{st.session_state.username}*"
        )


        # Séparation visuelle
        st.markdown("---")


        # Bouton page accueil
        if st.button("🤩 Accueil"):

            st.session_state.page = "Accueil"


        # Bouton page photos
        if st.button("🐱 Les photos de mon chat"):

            st.session_state.page = "Photos"


    # ==============================
    # PAGE ACCUEIL
    # ==============================

    if st.session_state.page == "Accueil":

        # Titre de la page
        st.markdown(
            "<h1 style='text-align:center;'>Bienvenue sur ma page</h1>",
            unsafe_allow_html=True
        )


        # Création des colonnes
        col1, col2, col3 = st.columns([1, 2, 1])


        # Image centrée
        with col2:

           st.image(
    "images/accueil.jpg",
    use_container_width=True)
           
    #======================
    # PAGE PHOTOS
    # ==============================

    elif st.session_state.page == "Photos":


        # Titre de la page
        st.markdown(
            "<h1>Bienvenue dans l'album de mes chats 🐱</h1>",
            unsafe_allow_html=True
        )


        # Création des 3 colonnes
        col1, col2, col3 = st.columns(3)


        # Première image
        with col1:

            st.image(
                "images/chat1.jpg"
            )


        # Deuxième image
        with col2:

            st.image(
                "images/chat2.jpg"
            )


        # Troisième image
        with col3:

            st.image(
                "images/chat3.jpg"
            )


# ==============================
# LANCEMENT DE STREAMLIT
# ==============================