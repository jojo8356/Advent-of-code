# 2015

25 exercices répartis dans `dayNN/`, une entrée de puzzle partagée par jour dans `inputs/`.

> Les entrées des jours 13 à 19 ne sont pas encore versionnées : dépose le fichier
> dans `2015/inputs/dayNN.txt`, ou passe-le avec `-i` au lanceur.

| Jour | Partie 1 | Partie 2 | Entrée | Notes |
|------|----------|----------|--------|-------|
| 01 | [part1.py](day01/part1.py) | [part2.py](day01/part2.py) | [day01.txt](inputs/day01.txt) | |
| 02 | [part1.py](day02/part1.py) | [part2.py](day02/part2.py) | [day02.txt](inputs/day02.txt) | |
| 03 | [part1.py](day03/part1.py) | [part2.py](day03/part2.py) | [day03.txt](inputs/day03.txt) | |
| 04 | [part1.py](day04/part1.py) | [part2.py](day04/part2.py) | [day04.txt](inputs/day04.txt) | MD5 |
| 05 | [part1.py](day05/part1.py) | [part2.py](day05/part2.py) | [day05.txt](inputs/day05.txt) | |
| 06 | [part1.py](day06/part1.py) | [part2.py](day06/part2.py) | [day06.txt](inputs/day06.txt) | grille 1000×1000 |
| 07 | [part1.py](day07/part1.py) | [part2.py](day07/part2.py) | [day07.txt](inputs/day07.txt) | circuit 16 bits |
| 08 | [part1.py](day08/part1.py) | [part2.py](day08/part2.py) | [day08.txt](inputs/day08.txt) | échappements de chaînes |
| 09 | [part1.py](day09/part1.py) | [part2.py](day09/part2.py) | [day09.txt](inputs/day09.txt) | permutations |
| 10 | [part1.py](day10/part1.py) | [part2.py](day10/part2.py) | [day10.txt](inputs/day10.txt) | look-and-say |
| 11 | [part1.py](day11/part1.py) | [part2.py](day11/part2.py) | [day11.txt](inputs/day11.txt) | force brute sur 8 lettres |
| 12 | [part1.py](day12/part1.py) | [part2.py](day12/part2.py) | [day12.txt](inputs/day12.txt) | JSON, objets `"red"` ignorés |
| 13 | [part1.py](day13/part1.py) | [part2.py](day13/part2.py) | [day13.txt](inputs/day13.txt) | table circulaire |
| 14 | [part1.py](day14/part1.py) | [part2.py](day14/part2.py) | [day14.txt](inputs/day14.txt) | course de 2 503 s |
| 15 | [part1.py](day15/part1.py) | [part2.py](day15/part2.py) | [day15.txt](inputs/day15.txt) | répartition en 100 cuillères |
| 16 | [part1.py](day16/part1.py) | [part2.py](day16/part2.py) | [day16.txt](inputs/day16.txt) | relevé MFCSAM |
| 17 | [part1.py](day17/part1.py) | [part2.py](day17/part2.py) | [day17.txt](inputs/day17.txt) | sous-ensembles à somme 150 |
| 18 | [part1.py](day18/part1.py) | [part2.py](day18/part2.py) | [day18.txt](inputs/day18.txt) | automate de Conway, coins fixes en P2 |
| 19 | [part1.py](day19/part1.py) | [part2.py](day19/part2.py) | [day19.txt](inputs/day19.txt) | remplacement de molécules |
| 20 | [part1.c](day20/part1.c) · [part1.py](day20/part1.py) | [part2.c](day20/part2.c) · [part2.py](day20/part2.py) | [day20.txt](inputs/day20.txt) | Python **et** C, cible 34 000 000 |
| 21 | [part1.py](day21/part1.py) | [part2.py](day21/part2.py) | [day21.txt](inputs/day21.txt) | stats du boss lues dans l'entrée (109 / 8 / 2) |
| 22 | [part1.py](day22/part1.py) | [part2.py](day22/part2.py) | [day22.txt](inputs/day22.txt) | partie 2 = mode difficile ; stats du boss lues dans l'entrée (51 / 9) |
| 23 | — | [part2.py](day23/part2.py) | [day23.txt](inputs/day23.txt) | partie 1 : `registers = {"a": 0, "b": 0}` |
| 24 | [part1.py](day24/part1.py) | [part2.py](day24/part2.py) | [day24.txt](inputs/day24.txt) | 3 puis 4 groupes |
| 25 | [part1.py](day25/part1.py) | — | [day25.txt](inputs/day25.txt) | position lue dans la consigne |

## Lancer

```bash
python3 run.py 2015 12        # jour 12, les deux parties
python3 run.py 2015 20 --lang c
python3 run.py 2015 13 -i mon_input.txt
```
