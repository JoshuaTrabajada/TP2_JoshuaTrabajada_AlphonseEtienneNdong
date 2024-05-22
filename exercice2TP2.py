import csv


def charger_pokémons_csv(nom_fichier):
    pokemons = {}

    with open(nom_fichier, newline='') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)

        for ligne in lecteur_csv:
            nom_pokemon = ligne[0]
            stats = list(map(int, ligne[1:]))
            pokemons[nom_pokemon] = stats

    return pokemons


# Exemple:
pkmn = charger_pokémons_csv("pokemon.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

# Vérifications:
print(isinstance(pkmn, dict))  # Devrait afficher True
print(isinstance(pkmn["Pikachu"], list))  # Devrait afficher True
print(isinstance(pkmn["Pikachu"][0], int))  # Devrait afficher True
