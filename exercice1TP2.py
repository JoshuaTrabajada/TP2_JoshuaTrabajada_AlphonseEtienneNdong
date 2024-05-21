import json
import csv

# Fonction pour lire le fichier JSON et retourner une liste de nombres complexes
def lire_json(nom_fichier):
    with open(nom_fichier, 'r') as f:
        data = json.load(f)
        nombres_complexes = [complex(r, i) for r, i in data]
    return nombres_complexes


# Fonction pour écrire les nombres complexes dans un fichier CSV
def ecrire_csv(nom_fichier, nombres_complexes):
    with open(nom_fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        # Écrire l'en-tête du fichier CSV
        writer.writerow(['reel', 'imaginaire'])
        # Écrire chaque nombre complexe dans une ligne du fichier CSV
        for nombre in nombres_complexes:
            writer.writerow([nombre.real, nombre.imag])

# Chemin du fichier JSON d'entrée
fichier_json = 'data.json'
# Chemin du fichier CSV de sortie
fichier_csv = 'resultat.csv'

# Lire les nombres complexes à partir du fichier JSON
nombres_complexes = lire_json(fichier_json)
# Écrire les nombres complexes dans un fichier CSV
ecrire_csv(fichier_csv, nombres_complexes)

print("Les nombres complexes ont été écrits dans le fichier", fichier_csv)
