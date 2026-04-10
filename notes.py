etudiants=[]


def ajouter_etudiants(nom,note):
    etudiants.append({"nom":nom,"note":note})
    print(f"Etudiants {nom}ajouté avec la note {note}.")