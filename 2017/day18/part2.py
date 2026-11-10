"""2017, jour 18 : Duet — partie 2.

Deux programmes exécutent le même code, avec `p = 0` et `p = 1`. Chacun a sa
file de messages :
  - `snd X` envoie la valeur de X dans la file de **l'autre** programme,
  - `rcv X` retire une valeur de sa file ; si elle est vide, le programme attend.

Ordonnancement : on fait tourner chaque programme **jusqu'à ce qu'il bloque ou
se termine**, en alternance. Un programme bloqué reprend dès qu'une valeur
arrive dans sa file. On s'arrête quand plus aucun des deux ne peut progresser
(interblocage) ou quand les deux sont terminés.

Réponse : nombre de valeurs envoyées par le programme 1.
"""

from pathlib import Path
import sys

from part1 import read_lignes, parse, valeur

DEFAULT_INPUT = Path(__file__).resolve().parent.parent / "inputs" / "day18.txt"


class Programme:
    """État d'un programme : registres, position, file de réception, compteur."""

    def __init__(self, numero, programme):
        self.registres = {"p": numero}
        self.position = 0
        self.file = []
        self.envoyes = 0
        self.programme = programme

    @property
    def termine(self):
        return not (0 <= self.position < len(self.programme))


def _executer_jusqu_au_blocage(programme, autre, index):
    """Fait avancer un programme jusqu'à blocage ou fin.

    Renvoie True si au moins une instruction a été exécutée.
    """
    progres = False
    while not programme.termine:
        instruction, x, y = programme.programme[programme.position]
        if instruction == "rcv":
            if not programme.file:
                return progres          # attend un message : on rend la main
            programme.registres[x] = programme.file.pop(0)
        elif instruction == "snd":
            autre.file.append(valeur(programme.registres, x))
            if index == 1:
                programme.envoyes += 1
        elif instruction == "set":
            programme.registres[x] = valeur(programme.registres, y)
        elif instruction == "add":
            programme.registres[x] = (valeur(programme.registres, x)
                                      + valeur(programme.registres, y))
        elif instruction == "mul":
            programme.registres[x] = (valeur(programme.registres, x)
                                      * valeur(programme.registres, y))
        elif instruction == "mod":
            programme.registres[x] = (valeur(programme.registres, x)
                                      % valeur(programme.registres, y))
        elif instruction == "jgz":
            if valeur(programme.registres, x) > 0:
                programme.position += valeur(programme.registres, y)
                progres = True
                continue
        else:
            raise ValueError(f"instruction inconnue : {instruction!r}")
        programme.position += 1
        progres = True
    return progres


def executer_deux(programme):
    """Fait tourner les deux programmes ; renvoie le nombre d'envois du n°1."""
    programmes = [Programme(0, programme), Programme(1, programme)]
    while True:
        progres = False
        for index in (0, 1):
            if _executer_jusqu_au_blocage(programmes[index], programmes[1 - index], index):
                progres = True
        if not progres:                  # les deux sont bloqués ou terminés
            return programmes[1].envoyes


def solve(lignes):
    return executer_deux(parse(lignes))


def main():
    print("Envois du programme 1:", solve(read_lignes()))


if __name__ == "__main__":
    main()
