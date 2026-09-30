import streamlit as st  #st sera le nom de mon fichier strealit.
import json

from fonctions_salaire_entreprise import calculer_salaire_employe


# Titre de l'application lancé.
st.title("Gestion des salaires")
# Ce qu'il sera écrit en dessous du titre.
st.write("Les statistiques et les salaires de l'entreprise.")


# On ouvre le fichier JSON avec les données des employés.
with open("employes_data_test.json", "r", encoding="utf-8") as fichier:
    donnees_entreprise = json.load(fichier)


# On choisit la filiale.
filiale_choisie = st.selectbox("Choisir une filiale :", donnees_entreprise.keys())


# On affiche les employés de la filiale choisie.
st.subheader(f"Salaires de {filiale_choisie}")


# On crée une liste pour mettre les salaires de la filiale choisie.
liste_salaires = []


# On parcourt les employés.
for employe in donnees_entreprise[filiale_choisie]:

    # Calculer le salaire.
    salaire_mensuel = calculer_salaire_employe(employe)

    # Le salaire s'ajoute dans la liste.
    liste_salaires.append(salaire_mensuel)

    # Affiche le nom du salarié, le poste du salarié et le salaire du salarié.
    st.write(
        employe["name"],
        "-",
        employe["job"],
        "-",
        round(salaire_mensuel, 2),
        "€"
    )


# On calcule les statistiques des salaires.
salaire_moyen = sum(liste_salaires) / len(liste_salaires)
salaire_max = max(liste_salaires)
salaire_min = min(liste_salaires)


# On affiche les statistiques salariales.
st.subheader("Statistiques salariales")

st.write("Moyenne Salariale :", round(salaire_moyen, 2), "€")
st.write("Salaire Minimum :", round(salaire_min, 2), "€")
st.write("Salaire Maximum :", round(salaire_max, 2), "€")

# Faire la recherche d'un employé.
st.subheader("Rechercher un employé")

# On écrit le nom de l'employé que l'on cherche.
nom_recherche = st.text_input("Entrer le nom de l'employé :")


# On parcourt toutes les filiales.
for nom_filiale, liste_employes in donnees_entreprise.items():

    # On parcourt les employés.
    for employe in liste_employes:

        # On vérifie si le nom correspond à notre recherche.
        if employe["name"].lower() == nom_recherche.lower():

            # On calcule son salaire.
            salaire_mensuel = calculer_salaire_employe(employe)

            # On affiche les informations de l'employé.
            st.write("Nom :", employe["name"])
            st.write("Poste :", employe["job"])
            st.write("Filiale :", nom_filiale )
            st.write("Salaire :", round(salaire_mensuel, 2), "€")