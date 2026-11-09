# Réponses

Carnet des résultats, rempli **exercice par exercice** au fil de l'avancement.
Chaque valeur est la sortie réelle du fichier de solution correspondant, lancée
sur l'entrée de `inputs/` avec `python3 run.py <année> <jour> <partie>`.

## 2015

| Jour | Partie 1 | Partie 2 | Statut |
|------|---------:|---------:|--------|
| 01 | **232** | **1783** | ✅ |
| 02 | **1598415** | **3812909** | ✅ |
| 03 | **2565** | **2639** | ✅ |
| 04 | **282749** | **9962624** | ✅ |
| 05 | **255** | **55** | ✅ |
| 06 | **569999** | **17836115** | ✅ |
| 07 | **16076** | **2797** | ✅ |
| 08 | **1333** | **2046** | ✅ |
| 09 | **207** | **804** | ✅ |
| 10 | **360154** | **5103798** | ✅ |
| 11 | **hxbxxyzz** | **hxcaabcc** | ✅ |
| 12 | **111754** | **65402** | ✅ |
| 13 | **709** | **668** | ✅ |
| 14 | **2655 km** | **1059 pts** | ✅ |
| 15 | **13882464** | **11171160** | ✅ |
| 16 | **373** | **260** | ✅ |
| 17 | **654** | **57** (4 containers) | ✅ |
| 18 | **821** | **886** | ✅ |
| 19 | **518** | **200** | ✅ |
| 20 | **786240** | **831600** | ✅ |
| 21 | **111** | **188** | ✅ |
| 22 | **900** | **1216** | ✅ |
| 23 | **307** | **160** | ✅ |
| 24 | **11846773891** | **80393059** | ✅ |
| 25 | **9132360** | — | ✅ |

### 2016

| Jour | Partie 1 | Partie 2 | Statut |
|------|----------|----------|--------|
| 01 | **226** | **79** | ✅ |
| 02 | **35749** | **9365C** | ✅ |
| 03 | **869** | **1544** | ✅ |
| 04 | **185371** | **984** | ✅ |
| 05 | **d4cd2ee1** | **f2c730e5** | ✅ |
| 06 | **nabgqlcw** | **ovtrjcjh** | ✅ |
| 07 | **110** | **242** | ✅ |
| 08 | **110** | **ZJHRKCPLYJ** | ✅ |
| 09 | **115118** | **11107527530** | ✅ |
| 10 | **86** | **22847** | ✅ |
| 11 | **37** | **61** | ✅ |
| 12 | **318003** | **9227657** | ✅ |

## 2020

| Jour | Partie 1 | Partie 2 | Statut |
|------|---------:|---------:|--------|
| — | | | en attente |

## 2025

| Jour | Partie 1 | Partie 2 | Statut |
|------|---------:|---------:|--------|
| 01 | **980** | **5961** | ✅ |

## Légende

- ✅ les deux parties tournent sur l'entrée versionnée
- 🕓 à traiter
- ⚠️ entrée du puzzle manquante ou dépendance externe (voir les README par année)

## Détail des jours traités

### 2015 — jour 1 : Not Quite Lisp

- **Partie 1 — 232.** On parcourt la consigne : `(` monte d'un étage, `)`
  descend, et on renvoie l'étage final.
- **Partie 2 — 1783.** Même parcours, mais on renvoie la position (1-indexée)
  du premier caractère qui fait passer l'ascenseur au sous-sol (étage `-1`).

### 2015 — jour 2 : I Was Told There Would Be No Math

- **Partie 1 — 1598415.** Pour chaque paquet `l x w x h` : surface
  `2*(l*w + w*h + h*l)` plus le « slack » égal à la surface du plus petit côté.
  Somme sur les 1 000 paquets.
- **Partie 2 — 3812909.** Ruban = plus petit périmètre
  `2*(deux plus petites dimensions)` + le nœud (volume `l*w*h`).

### 2015 — jour 3 : Perfectly Spherical Houses in a Vacuum

- **Partie 1 — 2565.** Le Père Noël part de `(0,0)` ; `^ v < >` le déplacent.
  On compte les positions distinctes visitées.
- **Partie 2 — 2639.** Deux livreurs alternent (indices pairs / impairs),
  chacun avec sa position ; on compte l'union des maisons visitées.

### 2015 — jour 4 : The Ideal Stocking Stuffer

Clé secrète : `yzbqklnj`.

- **Partie 1 — 282749.** Plus petit `n` tel que
  `md5("yzbqklnj" + n)` commence par `00000`.
- **Partie 2 — 9962624.** Idem avec six zéros : `000000`.

### 2015 — jour 5 : Doesn't He Have Intern-Elves For This?

- **Partie 1 — 255.** Chaîne gentille si au moins 3 voyelles, une lettre
  doublée, et aucune des paires `ab`, `cd`, `pq`, `xy` (1 000 chaînes testées).
- **Partie 2 — 55.** Chaîne gentille si elle contient `x?x` (même lettre
  séparée par une autre) et une paire `ab` répétée sans chevauchement.

### 2015 — jour 6 : Probably a Fire Hazard

Grille de 1 000 × 1 000 lumières, 300 instructions `turn on` / `turn off` /
`toggle` sur des rectangles inclusifs.

- **Partie 1 — 569999.** `turn on` allume, `turn off` éteint, `toggle`
  inverse ; on compte les lumières allumées à la fin.
- **Partie 2 — 17836115.** Luminosité : `turn on` +1, `turn off` −1 (plancher
  0), `toggle` +2 ; on somme la luminosité de toute la grille.

### 2015 — jour 7 : Some Assembly Required

Circuit de 339 fils (`AND`, `OR`, `NOT`, `LSHIFT`, `RSHIFT`, constantes).

- **Partie 1 — 16076.** Évaluation à la demande avec mémoïsation : l'ordre des
  lignes du fichier n'a pas d'importance. Opérations sur 16 bits
  (masque `0xFFFF`, `NOT` = complément à 16 bits).
- **Partie 2 — 2797.** On force `b` à la valeur trouvée en partie 1 (16076),
  puis on relit `a`.

### 2015 — jour 8 : Matchsticks

300 littéraux de chaîne (échappements `\"`, `\\`, `\xNN`).

- **Partie 1 — 1333.** Écart entre la longueur écrite (6 310 caractères au
  total) et la longueur une fois interprétée en mémoire (4 977) :
  `6 310 − 4 977 = 1 333`.
- **Partie 2 — 2046.** On ré-encode chaque littéral (antislash devant `"` et
  `\`, plus les guillemets) : 8 356 caractères, soit `8 356 − 6 310 = 2 046`.

### 2015 — jour 9 : All in a Single Night

8 villes, 28 distances (graphe complet symétrique).

- **Partie 1 — 207.** Plus court trajet passant par chaque ville une seule fois
  (40 320 permutations parcourues).
- **Partie 2 — 804.** Même chose en cherchant le plus long.

> Piège évité : contrairement au voyageur de commerce cyclique, on **ne peut pas**
> fixer la ville de départ ; sinon on rate les trajets qui ne commencent pas par
> elle (l'exemple officiel donnait 659 au lieu de 982).

### 2015 — jour 10 : Elves Look, Elves Say

Séquence de départ : `1113122113`. Chaque itération décrit la précédente en
groupes (`1` -> `11`, `21` -> `1211`, ...).

- **Partie 1 — 360154.** Longueur de la chaîne après **40** itérations.
- **Partie 2 — 5103798.** Longueur après **50** itérations (la chaîne grossit
  d'un facteur ~1,3 par étape, d'où les 5,1 millions de chiffres).

### 2015 — jour 11 : Corporate Policy

Mot de passe de départ : `hxbxwxba` (8 lettres minuscules).

- **Partie 1 — `hxbxxyzz`.** Prochain mot de passe valide : suite de trois
  lettres croissantes, aucune `i`/`o`/`l`, au moins deux paires distinctes.
- **Partie 2 — `hxcaabcc`.** Le suivant après `hxbxxyzz` (environ 1,5 million
  de candidats testés, 1,4 s).

### 2015 — jour 12 : JSAbacusFramework.io

Document JSON de 26 664 caractères (racine = objet, 219 occurrences de `"red"`).

- **Partie 1 — 111754.** Somme de **tous** les nombres, où qu'ils soient
  (obtenue par parcours récursif, et confirmée par un simple `-?\d+` sur le texte).
- **Partie 2 — 65402.** On ignore tout objet qui a `"red"` parmi ses **valeurs**
  (la clé n'est pas concernée) ; les tableaux, eux, sont toujours parcourus.

### 2015 — jour 13 : Knights of the Dinner Table

8 personnes, 56 relations de bonheur (table circulaire).

- **Partie 1 — 709.** Meilleur arrangement possible : chaque convive rapporte
  son bonheur vis-à-vis de ses deux voisins. Parcours de `7!` arrangements.
- **Partie 2 — 668.** On s'ajoute soi-même (bonheur 0 avec tout le monde) ;
  la table passe à 9 convives et le meilleur score baisse, car ajouter une
  place neutre casse la meilleure configuration à 8.

### 2015 — jour 14 : Reindeer Olympics

9 rennes, course de 2 503 secondes (vol/repos en cycles).

- **Partie 1 — Donner, 2655 km.** Distance parcourue au bout de 2 503 s
  (`cycles complets × temps de vol + reste`). Podium : Donner 2655, Vixen 2640,
  Cupid 2592.
- **Partie 2 — Vixen, 1059 points.** Chaque seconde, le(s) renne(s) en tête
  marque(nt) un point ; c'est Vixen qui en cumule le plus, malgré une distance
  finale inférieure à Donner.

### 2015 — jour 15 : Science for Hungry People

4 ingrédients, 100 cuillères à répartir.

- **Partie 1 — 13882464.** Score = produit des 4 propriétés (négatifs ramenés à
  0). Meilleure recette : Sprinkles 28, PeanutButter 35, Frosting 18, Sugar 19
  (capacité 86, durabilité 59, saveur 72, texture 38 ; 435 calories).
- **Partie 2 — 11171160.** Même score, mais avec **exactement 500 calories** :
  Sprinkles 27, PeanutButter 27, Frosting 15, Sugar 31 (77 / 39 / 60 / 62,
  500 calories).

### 2015 — jour 16 : Aunt Sue

500 tantes Sue, comparées au relevé MFCSAM (`children: 3, cats: 7, samoyeds: 2,
pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1`).

- **Partie 1 — Sue 373.** Toutes les propriétés connues doivent être **égales**
  (`pomeranians: 3`, `perfumes: 1`, `vizslas: 0`).
- **Partie 2 — Sue 260.** Règles « floues » : `cats` et `trees` doivent être
  **strictement supérieurs**, `pomeranians` et `goldfish` **strictement
  inférieurs**, le reste reste égal (`goldfish: 0` < 5, `vizslas: 0`,
  `samoyeds: 2`).

### 2015 — jour 17 : No Such Thing as Too Much

20 containers (50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47,
36, 24, 22, 40), cible : **150 litres**.

- **Partie 1 — 654.** Toutes les combinaisons de containers dont la somme fait
  exactement 150.
- **Partie 2 — 57.** Il faut au minimum **4** containers ; 57 combinaisons de
  exactement 4 containers totalisent 150 litres.
  Répartition : 4 → 57, 5 → 231, 6 → 262, 7 → 97, 8 → 7.

### 2015 — jour 18 : Like a GIF For Your Yard

Grille 100 x 100, 4 905 lumières allumées au départ, 100 générations.
Règles (automate de Conway) : une lumière allumée reste allumée avec 2 ou 3
voisins allumés ; une éteinte s'allume avec exactement 3 voisins.

- **Partie 1 — 821.** Simulation classique sur 100 générations.
- **Partie 2 — 886.** Les quatre coins sont bloqués en position allumée à
  chaque génération (y compris au départ).

### 2015 — jour 19 : Medicine for Rudolph

43 règles de remplacement, molécule de 488 caractères (285 atomes).

- **Partie 1 — 518.** Nombre de molécules **distinctes** obtenues par un seul
  remplacement (on teste chaque règle à chaque position, y compris les
  chevauchements).
- **Partie 2 — 200.** Nombre minimal d'étapes pour partir de `e`. Deux méthodes
  concordent : remontée gloutonne (règles inversées, plus long membre droit
  d'abord) et formule fermée
  `atomes − 1 − Rn − Ar − 2×Y = 285 − 1 − 32 − 32 − 20 = 200`.
  La version aléatoire d'origine (qui bouclait) a été remplacée.

### 2015 — jour 20 : Infinite Elves and Infinite Houses

Cible : **34 000 000** de cadeaux.

- **Partie 1 — 786240.** L'elfe n visite que les maisons multiples de n et
  laisse `10 × n` cadeaux : la maison h reçoit `10 × somme des diviseurs de h`.
  Maison 786240 → 34 137 600 cadeaux (et 786239 → 8 276 400, donc c'est bien
  la première).
- **Partie 2 — 831600.** Chaque elfe s'arrête après **50 maisons** et laisse
  `11 × n` : on ne garde que les diviseurs d vérifiant `h / d ≤ 50`.
  Maison 831600 → 35 780 206 cadeaux (831599 → 9 147 589).
  Le C et le Python du dépôt donnent les mêmes deux valeurs.

### 2015 — jour 21 : RPG Simulator

Boss de votre entrée : **109 PV, 8 dégâts, 2 armure** ; joueur : 100 PV.
Boutique : 5 armes (obligatoire, 1 seule), 6 armures (0 ou 1), 6 anneaux (0 à 2).

- **Partie 1 — 111 pièces d'or.** Équipement le moins cher qui gagne :
  Longsword (40) + Chainmail (31) + anneau Def+2 (40) → 7 dégâts, 4 armure.
- **Partie 2 — 188 pièces d'or.** Équipement le plus cher qui perd encore :
  Dagger (8) + anneaux Dmg+3 (100) et Def+3 (80) = 188, sans armure
  (3 d'armure au total contre 2 au boss : le combat reste perdu).

### 2015 — jour 22 : Wizard Simulator

Votre boss : **51 PV, 9 dégâts** (joueur : 50 PV, 500 mana, aucun équipement
passif). Recherche du mana minimal pour gagner.

- **Partie 1 — 900 mana.** Séquence optimale :
  Magic Missile → Poison → Recharge → Magic Missile → Poison → Shield →
  Magic Missile → Magic Missile.
- **Partie 2 — 1216 mana.** Mode difficile : le joueur perd 1 PV au début de
  chacun de ses tours, d'où un mana minimal plus élevé.

### 2015 — jour 23 : Opening the Turing Lock

Programme de 47 instructions (`hlf`, `tpl`, `inc`, `jmp`, `jie`, `jio`).

- **Partie 1 — 307.** Départ `a = 0, b = 0` : `b` finit à **307**
  (1 780 instructions exécutées, `a` finit à 1).
- **Partie 2 — 160.** Départ `a = 1` : `b` finit à **160**
  (935 instructions exécutées).

### 2015 — jour 24 : It Hangs in the Balance

29 paquets, somme 1560. QE = produit des poids du premier groupe.

- **Partie 1 — 11846773891.** 3 groupes de 520 ; premier groupe = **6 paquets**.
- **Partie 2 — 80393059.** 4 groupes de 390 ; premier groupe = **4 paquets**.

Vérifié par deux algorithmes indépendants (énumération + test de partition exact).

### 2015 — jour 25 : Let It Snow

Case **(2981, 3075)** de la grille en diagonale.

- **Partie 1 — 9132360.** Indice de la case : 18 331 560 ;
  code = `20151125 × 252533^(n−1) mod 33554393`.
- **Partie 2 — aucune** : terminer le jour 25 donne la 50ᵉ étoile.

### 2016 — jour 1 : No Time for a Taxicab

164 instructions (`R`/`L` + distance), départ face au nord.

- **Partie 1 — 226.** Arrivée en **(91, 135)** face à l'ouest ;
  distance de Manhattan |91| + |135| = **226**.
- **Partie 2 — 79.** Première case franchie deux fois : **(75, −4)** →
  |75| + |−4| = **79**.

Exemples officiels vérifiés : R2,L3 → 5 ; R2,R2,R2 → 2 ; R5,L5,R5,R3 → 12 ;
R8,R4,R4,R8 → 4. Recalcul indépendant (nombres complexes) : 226 / 79.

### 2016 — jour 2 : Bathroom Security

5 lignes d'instructions (413 à 524 caractères), un bouton par ligne.

- **Partie 1 — 35749.** Pavé 3×3 `1`–`9`, départ sur `5`, les sorties de
  grille sont ignorées.
- **Partie 2 — 9365C.** Pavé en losange à 13 boutons (`1`–`9`, `A`–`D`),
  départ au centre sur `5`.

Exemple officiel `ULL / RRDDD / LURDL / UUUUD` → **1985** et **5DB3** ✔.
Recalcul indépendant sur grilles de caractères : mêmes deux codes.

### 2016 — jour 3 : Squares With Three Sides

1 599 lignes × 3 nombres. Triangle valide si `a + b > c` pour les trois
combinaisons (il suffit de tester les deux plus petits contre le plus grand).

- **Partie 1 — 869.** Chaque ligne est un triangle.
- **Partie 2 — 1544.** Lecture **par colonnes** : par blocs de 3 lignes, chaque
  colonne forme un triangle (1 599 est bien multiple de 3).

Exemple officiel (`5 10 25` / `5 10 26` / `101 102 103`) → 1 seul valide ✔.
Recalcul indépendant avec les trois inégalités explicites : mêmes résultats.

### 2016 — jour 4 : Security Through Obscurity

980 salles `nom-identifiant[somme]`, dont **337** valides.

- **Partie 1 — 185371.** Somme des identifiants des salles dont la somme de
  contrôle est bien les 5 lettres les plus fréquentes (égalité → ordre
  alphabétique, tirets exclus).
- **Partie 2 — 984.** Décalage de César de `identifiant` mod 26 sur le nom ;
  la salle `northpole object storage` est l'identifiant **984**.

Exemple officiel → **1514** ✔ (`qzmt-zixmtkozy-ivhz-343` → « very encrypted
name »). Recalcul indépendant (comptage manuel, regex séparée) : 185371 / 984.

### 2016 — jour 5 : How About a Nice Game of Chess?

Sel : **ugkcyxxp**. MD5 de `sel + n` pour n = 0, 1, 2, …

- **Partie 1 — `d4cd2ee1`.** Hachages commençant par `00000` → 6ᵉ caractère
  hexadécimal. Indices trouvés : 702868, 1776010, 8421983, 8744114, 8845282,
  9268910, 9973527, 10253166.
- **Partie 2 — `f2c730e5`.** Le 6ᵉ caractère (0–7) donne la position, le 7ᵉ le
  caractère ; positions déjà remplies et 8–f ignorées. Dernière position
  remplie à l'indice 25 176 241.

Exemple officiel `abc` → `18f47a30` et `05ace8e3` ✔ (24 s). Recalcul
indépendant, mêmes deux mots de passe.

### 2016 — jour 6 : Signals and Noise

650 messages de 8 caractères.

- **Partie 1 — `nabgqlcw`.** Par colonne, on garde le caractère le **plus
  fréquent** (le signal majoritaire).
- **Partie 2 — `ovtrjcjh`.** Par colonne, on garde le caractère le **moins
  fréquent** (la « vérité » est plus rare que les erreurs).

Aucun ex-aequo dans les 8 colonnes : les réponses sont nettes. Recalcul
indépendant (comptage par dictionnaire, sans `zip` ni `Counter`) : identique.

### 2016 — jour 7 : Internet Protocol Version 7

2 000 adresses `abcd[efgh]ijkl` (segments internes entre crochets).

- **Partie 1 — 110.** TLS : un **ABBA** (`xyyx`, x ≠ y) dans un segment
  externe et **aucun** ABBA dans un segment interne.
- **Partie 2 — 242.** SSL : une séquence **ABA** externe (`xyx`) et la
  séquence **BAB** correspondante (`yxy`) dans un segment interne.

Exemples officiels : 2 adresses TLS sur 4 ✔, 3 adresses SSL sur 4 ✔.
Recalcul indépendant (découpage par `split('[')`, ensembles d'ABA/BAB) :
110 / 242, identique.

### 2016 — jour 8 : Two-Factor Authentication

153 instructions sur un écran 50 × 6 : 20 `rect`, 36 `rotate row`,
97 `rotate column`.

- **Partie 1 — 110.** Pixels allumés à la fin.
- **Partie 2 — `ZJHRKCPLYJ`.** Les pixels dessinent 10 lettres de 5 × 6
  (police 5 × 6, lecture par blocs de 5 colonnes).

Exemple officiel 7 × 3 (`rect 3x2`, rotations) simulé à la main : grille
identique ✔, 6 pixels. Recalcul indépendant de la simulation : 110, grille
caractère par caractère identique.

### 2016 — jour 9 : Explosives in Cyberspace

Une ligne de 12 156 caractères, 947 marqueurs `(LxF)`.

- **Partie 1 — 115118.** Une seule passe de décompression : le contenu répété
  n'est pas ré-examiné. On avance avec `i = fin_marqueur + L`.
- **Partie 2 — 11107527530.** Décompression **récursive** : on ne construit
  jamais la chaîne, on calcule la longueur par plages mémoïsées (`lru_cache`).

Les 6 exemples officiels de la partie 1 (6, 7, 9, 11, 6, 18) et ceux de la
partie 2 (20, 445, 241920) sont exacts. Recalcul indépendant (parseur regex,
récursion sur sous-chaînes) : mêmes deux valeurs.

### 2016 — jour 10 : Balance Bots

210 bots, 21 valeurs initiales, sorties 0 à 9.

- **Partie 1 — 86.** Le bot qui compare les puces **17** et **61** est le
  bot **86**.
- **Partie 2 — 22847.** Sorties 0, 1 et 2 = 67, 11 et 31 → 67 × 11 × 31 =
  **22847**.

Exemple officiel (paire 2 / 5) → bot **2** ✔ et produit des sorties = **30** ✔.
Recalcul indépendant (balayage répété au lieu d'une file) : 86 / 22847, et les
210 bots ont bien tous comparé exactement une fois.

### 2016 — jour 11 : Radioisotope Thermoelectric Generators

5 isotopes (strontium, plutonium, thulium, ruthenium, curium), 11 objets,
4 étages. BFS sur les états avec **canonisation** (les isotopes sont
interchangeables : on trie les paires générateur/puce).

- **Partie 1 — 37 trajets.** Tout amener au 4ᵉ étage.
- **Partie 2 — 61 trajets.** On ajoute un générateur et une puce **elerium**
  ainsi qu'un générateur et une puce **dilithium** au 1ᵉʳ étage.

Exemple officiel (2 isotopes) → **11** ✔. Recalcul indépendant avec un autre
codage (frozenset canonisé, `itertools.combinations`) : 37 / 61.

### 2016 — jour 12 : Leonardo's Monorail

23 instructions (`cpy`, `inc`, `dec`, `jnz`), quatre registres.

- **Partie 1 — 318003.** Tous les registres à 0.
- **Partie 2 — 9227657.** Registre `c` initialisé à 1.

Deux motifs de boucles (`inc x / dec y / jnz y -2` et `dec x / jnz x -2`) sont
exécutés d'un coup : 2,9 s → 0,09 s, résultats identiques.

Exemple officiel → 42 ✔. Contrôle par exécution **naïve** non optimisée :
318003 (954 164 instructions) et 9227657 (27 683 175 instructions).

### 2025 — jour 1 : Secret Entrance

- **Partie 1 — 980.** Le cadran part de `50` ; chaque ligne `L<n>` / `R<n>`
  décale modulo 100, et on compte les instructions qui terminent sur `0`.
- **Partie 2 — 5961.** On compte chaque **passage** par `0` pendant le
  déplacement (pas seulement l'arrivée), en gérant le cas où l'on part de 0.

## Commandes

```bash
python3 run.py 2015 1        # rejoue le jour 1 de 2015
python3 run.py 2015 2        # rejoue le jour 2 de 2015
python3 run.py 2015 5        # rejoue le jour 5 de 2015
python3 run.py 2015 6        # rejoue le jour 6 de 2015
python3 run.py 2015 7        # rejoue le jour 7 de 2015
python3 run.py 2015 8        # rejoue le jour 8 de 2015
python3 run.py 2015 9        # rejoue le jour 9 de 2015
python3 run.py 2015 10       # rejoue le jour 10 de 2015
python3 run.py 2015 11       # rejoue le jour 11 de 2015
python3 run.py 2015 12       # rejoue le jour 12 de 2015
python3 run.py 2015 13       # rejoue le jour 13 de 2015
python3 run.py 2015 14       # rejoue le jour 14 de 2015
python3 run.py 2015 15       # rejoue le jour 15 de 2015
python3 run.py 2015 16       # rejoue le jour 16 de 2015
python3 run.py 2015 17       # rejoue le jour 17 de 2015
python3 run.py 2015 18       # rejoue le jour 18 de 2015
python3 run.py 2015 19       # rejoue le jour 19 de 2015
python3 run.py 2015 20       # rejoue le jour 20 de 2015
python3 run.py 2015 21       # rejoue le jour 21 de 2015
python3 run.py 2015 22       # rejoue le jour 22 de 2015
python3 run.py 2015 23       # rejoue le jour 23 de 2015
python3 run.py 2015 24       # rejoue le jour 24 de 2015
python3 run.py 2015 25       # rejoue le jour 25 de 2015
python3 run.py 2025 1        # rejoue le jour 1 de 2025
python3 run.py --list        # tout ce qui est disponible
```
