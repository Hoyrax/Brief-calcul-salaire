import csv
from typing import Dict, List, Any


# 1er FONCTION : Calcul du salaire.
def calculer_salaire_employe(employe: Dict[str, Any]) -> float:
    """
    Calcule le salaire mensuel d'un employé.
    Entrée : les informations de l'employé.
    Sortie : le salaire mensuel.
    """

    # On récupère les informations de l'employé dans le fichier JSON.
    heures_travaillees: float = employe["weekly_hours_worked"]
    heures_contractuelles: float = employe["contract_hours"]
    taux_horaire: float = employe["hourly_rate"]

    # On calcule les heures supplémentaires.
    heures_sup: float = max(0, heures_travaillees - heures_contractuelles)

    # On calcule le salaire de la semaine avec les heures supplémentaires en plus.
    salaire_hebdomadaire: float = (heures_contractuelles * taux_horaire) + (heures_sup * taux_horaire * 1.5)

    # On multiplie par 4 pour avoir le salaire du mois.
    salaire_mensuel: float = salaire_hebdomadaire * 4

    # On renvoie le salaire calculé.
    return salaire_mensuel


# 2ème FONCTION : Afficher stats globales.
def afficher_statistiques_globales(salaires: List[float]) -> None:
    """
    Calcule et affiche les statistiques globales.
    Entrée : la liste des salaires.
    Sortie : aucune.
    """

    # On calcule la moyenne, le plus grand et le plus petit salaire.
    salaire_moyen_global: float = sum(salaires) / len(salaires) 
    """ sum additionne tous les salaires, 
    et len compte le nombre de salaire. 
    """
    salaire_max_global: float = max(salaires)                     
    salaire_min_global: float = min(salaires)

    # On affiche les résultats.
    print("-" * 50)
    print("             STATISTIQUES GLOBALES")
    print("-" * 50)
    print("    Salaire Moyen Global :", round(salaire_moyen_global, 2), "€")
    print("    Salaire Max Global   :", round(salaire_max_global, 2), "€")
    print("    Salaire Min Global   :", round(salaire_min_global, 2), "€")
    print("-" * 50)
    print("\n")


# 3ème FONCTION : Stats par filiale.
def afficher_stats_une_filiale(nom: str, salaires_filiale: List[float]) -> None:
    """
    Calcule et affiche les statistiques d'une filiale.
    Entrées : le nom de la filiale et la liste des salaires.
    Sortie : aucune.
    """

    # On calcule la moyenne, le plus grand et le plus petit salaire de la filiale.
    salaire_moyen_filiale: float = sum(salaires_filiale) / len(salaires_filiale)
    salaire_max_filiale: float = max(salaires_filiale)
    salaire_min_filiale: float = min(salaires_filiale)

    # On affiche les résultats de la filiale.
    print(f"Filiale : {nom}")
    print(f"    • Moyenne : {round(salaire_moyen_filiale, 2)} €")
    print(f"    • Maximum : {round(salaire_max_filiale, 2)} €")
    print(f"    • Minimum : {round(salaire_min_filiale, 2)} €")
    print("-" * 35)


# 4ème FONCTION : Création du fichier CSV.
def creer_csv(donnees_entreprise: Dict[str, Any]) -> None:
    """
    Crée un fichier CSV avec les salaires des employés.
    Entrée : les données de l'entreprise.
    Sortie : aucune.
    """

    # On crée le fichier CSV.
    with open("resultats_salaires.csv", "w", encoding="utf-8", newline="") as fichier_csv:

        # On prépare l'écriture dans le fichier.
        ecriture_csv = csv.writer(fichier_csv)

        # On écrit les titres des colonnes.
        ecriture_csv.writerow(["Filiale", "Nom", "Poste", "Salaire mensuel"])

        # On parcourt chaque filiale.
        for nom_filiale, liste_employes in donnees_entreprise.items():

            # On parcourt chaque employé.
            for employe in liste_employes:

                # On appelle la fonction A pour calculer le salaire.
                salaire_mensuel: float = calculer_salaire_employe(employe)

                # On écrit les informations de l'employé.
                ecriture_csv.writerow([
                    nom_filiale,
                    employe["name"],
                    employe["job"],
                    round(salaire_mensuel, 2)
                ])

        #On fait une ligne vide dans le CSV.
        ecriture_csv.writerow([])

            #On met le titre des stats globales.
        ecriture_csv.writerow(["STATISTIQUE GLOBAL"])

        #On créer une liste pour y mettre les salariés.
        tous_les_salaires: List[float] = []

        #On rentre dans les filiales.
        for nom_filiale, liste_employes in donnees_entreprise.items():

            #On parcourt les employés.
            for employe in liste_employes:

            #On calcule le salaire et on l'ajoute dans la liste.
                salaire_mensuel: float = calculer_salaire_employe(employe)

                tous_les_salaires.append(salaire_mensuel)

            #On calcul les stats
        salaire_moyen: float = sum(tous_les_salaires) / len(tous_les_salaires)
        salaire_max: float = max(tous_les_salaires)
        salaire_min: float = min(tous_les_salaires)

        #On écrit les stats dans le fichier CSV.

        ecriture_csv.writerow(["Moyenne", round(salaire_moyen, 2)])

        ecriture_csv.writerow(["Maximum", round(salaire_max, 2)])

        ecriture_csv.writerow(["Minimum", round(salaire_min, 2)])