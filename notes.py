etudiants=[]


def ajouter_etudiants(nom,note):
    etudiants.append({"nom":nom,"note":note})
    print(f"Etudiants {nom}ajouté avec la note {note}.")
    
def calculer_moyenne():
    if not etudiants:
    print("Aucun étudiant enrégistré.")
    return 0
   total=sum(e['note']for e in etudiants)
   moyenne=total/|en(etudiants)
   print(f"Moyenne de le classe:{moyenne:.2f}")
   return moyenne