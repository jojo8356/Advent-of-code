# Advent of Code

Solutions aux puzzles d'[Advent of Code](https://adventofcode.com/), organisées
**par exercice** : un dossier par jour, un fichier par partie.

## Structure

```
<année>/
├── dayNN/                 un dossier par exercice
│   ├── part1.py           partie 1 (le langage est donné par l'extension)
│   ├── part2.py           partie 2
│   ├── part2.rs           la même partie dans un autre langage
│   └── ...
├── inputs/
│   └── dayNN.txt          l'entrée du puzzle, partagée par toutes les parties du jour
└── README.md              index des exercices de l'année

run.py                     lance n'importe quelle solution, quel que soit le langage
```

Conventions :

- `dayNN` sur deux chiffres (`day01`, `day12`) : l'ordre alphabétique est aussi
  l'ordre des jours.
- `partN` donne la partie ; l'extension donne le langage (`.py`, `.c`, `.rs`).
  Deux fichiers avec le même nom de partie = deux implémentations équivalentes.
- Une seule entrée par jour dans `inputs/`, lue par défaut par chaque solution
  (chemin résolu depuis le fichier source, donc peu importe le `cwd`).
- Chaque solution expose une fonction `solve(...)` (logique pure) et un `main()`
  qui lit l'entrée puis affiche le résultat : appelable en script comme en module.
- Les binaires compilés ne sont pas versionnés, ils sont reconstruits à la volée.

## Exercices couverts

| Année | Jours | Parties | Détail |
|-------|-------|---------|--------|
| [2015](2015/README.md) | 1–4, 12–25 | 1 et 2 (sauf 23 et 25) | Python, plus du C pour le jour 20 |
| [2020](2020/README.md) | 2 | 1 | Python et C |
| [2025](2025/README.md) | 1–12 | 1 et 2 (sauf 12) | Python, plus du Rust pour les jours 2, 9 et 12 |

Les entrées des jours 13 à 19 de 2015 ne sont pas encore versionnées (voir
[2015/README.md](2015/README.md)) : le lanceur les signale comme « sans entrée »
au lieu de les exécuter à vide.

## Lancer

```bash
python3 run.py 2025 1        # 2025, jour 1, les deux parties
python3 run.py 2015 20 2     # 2015, jour 20, partie 2
python3 run.py 2025 12 --lang rust
python3 run.py 2015          # toute une année
python3 run.py --all         # tout le dépôt
python3 run.py --list        # inventaire des exercices
```

Sans passer par le lanceur, chaque solution reste exécutable seule :

```bash
python3 2025/day01/part1.py            # lit 2025/inputs/day01.txt
python3 2025/day01/part1.py autre.txt  # ou une entrée au choix
gcc -O2 -o /tmp/day20 2015/day20/part1.c && /tmp/day20 2015/inputs/day20.txt
rustc -O -o /tmp/day12 2025/day12/part1.rs && /tmp/day12 2025/inputs/day12.txt
```

Options utiles du lanceur : `-i fichier` pour imposer une entrée, `--timeout N`
pour les solutions lentes, `--lang python|c|rust` pour filtrer, `--list` pour
l'inventaire.

## Dépendances

- Python 3.9+
- `gcc` pour les solutions C
- `rustc` pour les solutions Rust
- `scipy` pour `2025/day10/part2.py` (`pip install scipy`)

## License

MIT
