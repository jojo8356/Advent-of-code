"""2017, jour 25 : The Halting Problem — partie 1.

Machine de Turing à une bande infinie dans les deux sens. On lit l'état initial,
le nombre d'étapes et, pour chaque état, les deux règles conditionnelles.

Réponse : **checksum** (nombre de 1 sur la bande) après toutes les étapes.
"""

from pathlib import Path
import re
import sys

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day25.txt"


def read_texte():
    """Renvoie le texte du programme (argument, fichier par défaut, ou stdin)."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    return path.read_text() if path.exists() else sys.stdin.read()


def parse(texte):
    """Renvoie (état initial, nombre d'étapes, {état: {valeur: (écrit, pas, suivant)}})."""
    lignes = [ligne.strip() for ligne in texte.splitlines()]
    etat_initial = None
    etapes = None
    regles = {}
    courant = None
    valeur_courante = None
    for ligne in lignes:
        if not ligne:
            continue
        if etat_initial is None:
            m = re.match(r"Begin in state (\w)", ligne)
            if m:
                etat_initial = m.group(1)
                continue
        if etapes is None:
            m = re.match(r"Perform a diagnostic checksum after (\d+) steps", ligne)
            if m:
                etapes = int(m.group(1))
                continue
        m = re.match(r"In state (\w):", ligne)
        if m:
            courant = m.group(1)
            regles[courant] = {}
            valeur_courante = None
            continue
        m = re.match(r"If the current value is (\d):", ligne)
        if m:
            valeur_courante = int(m.group(1))
            regles[courant][valeur_courante] = {}
            continue
        m = re.match(r"- Write the value (\d)", ligne)
        if m:
            regles[courant][valeur_courante]["ecrit"] = int(m.group(1))
            continue
        m = re.match(r"- Move one slot to the (\w+)", ligne)
        if m:
            regles[courant][valeur_courante]["pas"] = 1 if m.group(1) == "right" else -1
            continue
        m = re.match(r"- Continue with state (\w)", ligne)
        if m:
            regles[courant][valeur_courante]["suivant"] = m.group(1)
            continue
    if etat_initial is None or etapes is None:
        raise ValueError("en-tête illisible")
    return etat_initial, etapes, regles


def executer(etat_initial, etapes, regles):
    """Fait tourner la machine ; renvoie le checksum final."""
    bande = {}                       # position -> valeur (absente = 0)
    position = 0
    etat = etat_initial
    for _ in range(etapes):
        valeur = bande.get(position, 0)
        regle = regles[etat][valeur]
        if regle["ecrit"]:
            bande[position] = 1
        else:
            bande.pop(position, None)
        position += regle["pas"]
        etat = regle["suivant"]
    return len(bande)


def solve(texte=None):
    if texte is None:
        texte = read_texte()
    return executer(*parse(texte))


def main():
    print("Checksum:", solve())


if __name__ == "__main__":
    main()
