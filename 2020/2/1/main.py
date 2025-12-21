def read_file(chemin_fichier):
    """
    Lit et affiche le contenu d'un fichier texte.

    :param chemin_fichier: Chemin vers le fichier texte.
    """
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            return contenu
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def get_variables(line):
    mini, maxi = line.split(" ")[0].split("-")
    letter = line.split(" ")[1].replace(":", "")
    text = line.split(" ")[-1]
    return float(mini), float(maxi), letter, text


liste = read_file("ressources.txt").split("\n")
n = 0
for line in liste:
    mini, maxi, letter, text = get_variables(line)
    if mini <= text.count(letter) <= maxi:
        n += 1

print(n)
