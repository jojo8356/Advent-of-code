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
| 13 | **90** | **135** | ✅ |
| 14 | **15168** | **20864** | ✅ |
| 15 | **122318** | **3208583** | ✅ |
| 16 | **10101001010100001** | **10100001110101001** | ✅ |
| 17 | **RDRRULDDDR** | **392** | ✅ |
| 18 | **1987** | **19984714** | ✅ |
| 19 | **1842613** | **1424135** | ✅ |
| 20 | **4793564** | **146** | ✅ |
| 21 | **gbhcefad** | **gahedfcb** | ✅ |
| 22 | **981** | **233** | ✅ |
| 23 | **11552** | **479008112** | ✅ |
| 24 | **430** | **700** | ✅ |
| 25 | **189** | — | ✅ |

## 2017

| Jour | Partie 1 | Partie 2 | Statut |
|------|----------|----------|--------|
| 01 | **1390** | **1232** | ✅ |
| 02 | **30994** | **233** | ✅ |
| 03 | **552** | **330785** | ✅ |
| 04 | **466** | **251** | ✅ |
| 05 | **355965** | **26948068** | ✅ |
| 06 | **12841** | **8038** | ✅ |
| 07 | **vgzejbd** | **1226** | ✅ |
| 08 | **5143** | **6209** | ✅ |
| 09 | **21037** | **9495** | ✅ |
| 10 | **13760** | **2da93395f1a6bb3472203252e3b17fe5** | ✅ |
| 11 | **877** | **1622** | ✅ |
| 12 | **113** | **202** | ✅ |
| 13 | **632** | **3849742** | ✅ |
| 14 | **8194** | **1141** | ✅ |
| 15 | **650** | **336** | ✅ |
| 16 | **padheomkgjfnblic** | **bfcdeakhijmlgopn** | ✅ |
| 17 | **417** | **34334221** | ✅ |
| 18 | **2951** | **7366** | ✅ |
| 19 | **LXWCKGRAOY** | **17302** | ✅ |
| 20 | **258** | **707** | ✅ |
| 21 | **158** | **2301762** | ✅ |
| 22 | **5256** | **2511345** | ✅ |
| 23 | **3969** | **917** | ✅ |

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

### 2016 — jour 13 : A Maze of Twisty Little Cubicles

Nombre favori **1352**. La case (x, y) est un mur si
`x² + 3x + 2xy + y + y² + 1352` a un nombre **impair** de bits à 1.

- **Partie 1 — 90.** Distance minimale de (1, 1) à **(31, 39)**.
- **Partie 2 — 135.** Cases atteignables en **au plus 50 pas** (50 inclus).

Exemple officiel (favori 10, cible (7, 4)) → **11** ✔, et la grille 10 × 7
reproduite est identique à l'énoncé. Recalcul indépendant par Dijkstra avec
comptage de bits par décalages : 90 / 135.

### 2016 — jour 14 : One-Time Pad

Sel **qzyelonm**. Une clé est un indice dont le MD5 de `sel + n` contient un
**triplet** et dont l'un des 1 000 hachages suivants contient le
**quintuplet** du même caractère.

- **Partie 1 — 15168.** MD5 simple. Dernières clés : 14937, 14967, **15168**.
- **Partie 2 — 20864.** Hachage étiré : 1 MD5 initial puis **2 016**
  ré-hachages de l'empreinte seule (2 017 hachages MD5 au total, sel non
  réinjecté). Dernières clés : 20779, 20822, **20864**.

Exemple officiel `abc` → **22728** et **22551** ✔. Recalcul indépendant
(flux de hachages, regex `(.)\1\1`, fenêtre glissante) : mêmes deux valeurs,
clés bien croissantes.

### 2016 — jour 15 : Timing is Everything

6 disques (13, 5, 17, 3, 7, 19 positions). Le disque i est vide quand la
capsule passe à l'instant `t + i`, soit `t ≡ −depart − i (mod positions)`.

- **Partie 1 — 122318.** Congruences : t ≡ 1 (13), 3 (5), 3 (17), 2 (3),
  0 (7), 15 (19). Modules premiers entre eux (produit 440 895).
- **Partie 2 — 3208583.** On ajoute un disque #7 de **11 positions** en
  position 0 → t ≡ 4 (11).

Exemple officiel (5 et 2 positions) → **5** ✔. Recalcul indépendant par
théorème des restes chinois : mêmes valeurs, et `t − 1` échoue pour les deux.

### 2016 — jour 16 : Dragon Checksum

Graine **10001001100000001**. Étirement : `a -> a + "0" + inverse_complément(a)`
jusqu'à la taille du disque, puis somme de contrôle par paires jusqu'à une
longueur impaire.

- **Partie 1 — `10101001010100001`** (disque de 272 cases, 17 bits).
- **Partie 2 — `10100001110101001`** (disque de **35 651 584** cases, soit
  17 × 2²¹ : la somme de contrôle se réduit 21 fois et fait 17 bits).

Exemple officiel (graine `10000`, disque 20) → `01100` ✔. Recalcul indépendant
(construction bit à bit et XOR) : partie 2 identique.
Remarque : une première version utilisait par erreur 35 651 528 (longueur
4 456 441) — corrigé en 35 651 584.

### 2016 — jour 17 : Two Steps Forward

Sel **vkjiggvb**. Labyrinthe 4 × 4 ; les 4 premiers caractères hexadécimaux du
MD5 de `sel + chemin` donnent l'état des portes `U`, `D`, `L`, `R`
(ouvertes pour `b`–`f`).

- **Partie 1 — `RDRRULDDDR`** (10 pas). Chemin le **plus court** ; il est unique
  (trouvé par BFS).
- **Partie 2 — 392.** Sur les **1 106** chemins qui atteignent la sortie, le
  plus long fait 392 pas (le plus court en fait 10).

Exemples officiels : `ihgpwlah` → `DDRRRD` / 370 ; `kglvqrbo` → aucun chemin ;
`ulqzkmiv` → `DRURDRUDDLLDLUURRDULRLDUUDDDRR` / 830. Recalcul indépendant
(BFS séparé + parcours exhaustif des longueurs) : mêmes résultats.

### 2016 — jour 18 : Like a Rogue

Rangée initiale de 100 tuiles. Une tuile devient un piège si ses deux parents
**extérieurs** diffèrent (`^` à gauche et `.` à droite, ou l'inverse) ; le
parent du centre n'intervient pas ; hors rangée, voisins sûrs.

- **Partie 1 — 1987.** Tuiles sûres sur **40** rangées (initiale comprise).
- **Partie 2 — 19984714.** Sur **400 000** rangées.

Exemple officiel `.^^.^.^^^^` sur 10 rangées → **38** ✔. Recalcul indépendant
avec un encodage en entier (piège = XOR des décalages `<< 1` et `>> 1`) :
mêmes valeurs, en 0,26 s au lieu de 6,4 s.

⚠️ Piège évité : la règle « exactement un des trois parents est un piège » est
une lecture fausse (elle donne 68 sur l'exemple). C'est bien `gauche ^ droite`.

### 2016 — jour 19 : An Elephant Named Joseph

**3 018 458 elfes** en cercle.

- **Partie 1 — 1842613.** L'elfe élimine son voisin de gauche (Josèphe, k = 2).
  `n = 2²¹ + 921306` → `2 × 921306 + 1 = 1842613`.
- **Partie 2 — 1424135.** L'elfe élimine celui qui est **en face**.
  `3¹³ = 1594323` et `n − p = 1424135 ≤ p` → le survivant est `n − p`.

Les deux formules ont été validées contre des simulations directes pour tous
les `n` de 1 à 399 (aucun écart).

### 2016 — jour 20 : Firewall Rules

**1 176** plages interdites `début-fin` (très chevauchantes), espace
d'adressage `0` à `4 294 967 295`.

- **Partie 1 — 4793564.** Plus petite adresse non bloquée.
- **Partie 2 — 146.** Nombre d'adresses autorisées sur tout l'espace.

Exemple officiel (`5-8`, `0-2`, `4-7`) → **3** ✔ et **2** adresses libres
sur `0..9` ✔. Recalcul indépendant par **balayage d'événements** (`+1` au
début, `−1` après la fin) : mêmes valeurs.

### 2016 — jour 21 : Scrambled Letters and Hash

100 instructions (swap, rotate, reverse, move) sur 8 lettres.

- **Partie 1 — `gbhcefad`.** `abcdefgh` brouillé par les 100 instructions.
- **Partie 2 — `gahedfcb`.** Mot de passe qui donne `fbgdceah`. Recherche
  exhaustive des 8! = 40 320 permutations ; l'antécédent est **unique**.

Exemple officiel : `abcde` → `decab` ✔ (traçé instruction par instruction),
et `decab` → `abcde` ✔ en sens inverse. Recalcul indépendant de la partie 1
(implémentation séparée) : `gbhcefad`, et vérification directe que `gahedfcb`
produit bien `fbgdceah`.

### 2016 — jour 22 : Grid Computing

Grille **35 × 29** (1 015 nœuds), un seul nœud vide `(8, 28)` de 92 T libres,
33 nœuds « pleins » (≥ 490 T) formant un mur horizontal en `y = 22`.

- **Partie 1 — 981.** Couples (A, B) viables : A non vide et
  `utilisé(A) ≤ libre(B)`.
- **Partie 2 — 233.** Amener les données de `(34, 0)` en `(0, 0)` :
  `67` (trou → `(33,0)`) `+ 1 + 5 × 33 = 233`.

**Pourquoi 233 est exact** : les données cibles pèsent 66 T, or le seul nœud
offrant assez de place est le nœud vide (92 T) — tous les autres nœuds ont au
plus 30 T libres. Aucune autre manœuvre n'existe, donc le modèle « déplacer le
trou » est exact. Un BFS sur `(trou, position des données)` retrouve 233, et une
recherche exhaustive à état complet avait été envisagée mais explosait
(≈ 50! états).

### 2016 — jour 23 : Safe Cracking

Assembleur à quatre registres, 26 instructions, dont un `tgl` qui modifie le
programme en cours d'exécution.

- **Partie 1 — 11552.** Départ `a = 7`.
- **Partie 2 — 479008112.** Départ `a = 12` : `12! + 6512 = 479008112`.

Trois motifs de boucles sont exécutés d'un coup (même résultat) :
`cpy X c / inc a / dec c / jnz c -2 / dec d / jnz d -5` → `a += X × d`, plus
les deux classiques `inc x / dec y / jnz y -2` et `dec x / jnz x -2`.

Exemple officiel `tgl` → `a = 3` ✔. **Validation** : l'interpréteur optimisé
donne exactement les valeurs de l'exécution naïve pour `a = 7`, `8`, `9`
(11552, 46832, 369392), sur 56 659 à 2 672 408 pas. Sans optimisation, la
partie 2 demanderait de dérouler `12!` ≈ 4,8 × 10⁸ itérations.

### 2016 — jour 24 : Air Duct Spelunking

Grille **181 × 39**, huit points numérotés `0` à `7`.

- **Partie 1 — 430.** Plus court parcours depuis `0` visitant tous les points.
- **Partie 2 — 700.** Même parcours, mais il faut **revenir au `0`**.

Méthode : BFS sur la grille depuis chaque point (matrice des distances deux à
deux), puis parcours des 7! = 5 040 permutations.

**Vérification indépendante** : un BFS sur l'état complet
`(position, ensemble des points visités)` — sans décomposition ni permutations —
explore 478 144 états et retrouve exactement **430** et **700**.

### 2016 — jour 25 : Clock Signal

Programme de 30 instructions (`cpy`, `inc`, `dec`, `jnz`) avec l'instruction
`out`, qui émet une valeur.

- **Partie 1 — 189.** Plus petit `a` positif dont la sortie est
  `0, 1, 0, 1, …` indéfiniment.
- **Partie 2 — aucune.** Terminer le jour 25 donne la 50ᵉ étoile.

**Pourquoi 189** : le programme calcule `d = a + 11 × 231 = a + 2541`, puis
émet les bits de ce nombre **du poids faible vers le poids fort**. Il faut donc
que `a + 2541` s'écrive `101010…10` en binaire ; la plus petite telle valeur
au-dessus de 2541 est `2730 = 0b101010101010`, d'où `a = 2730 − 2541 = 189`.

Vérifié par émission : `a = 189` tient **500 sorties** consécutives, alors que
186, 187, 188 et 190 échouent. Contrôle de minimalité par la formule : aucun
`a < 189` ne convient.

### 2017 — jour 1 : Inverse Captcha

Séquence circulaire de **2 182 chiffres**.

- **Partie 1 — 1390.** Somme des chiffres égaux à leur **voisin de droite**
  (269 paires égales, le dernier étant comparé au premier).
- **Partie 2 — 1232.** Somme des chiffres égaux à celui situé **à l'opposé**
  (demi-tour, 2 182 / 2 = 1 091 positions plus loin ; 242 paires égales).

Les neuf exemples officiels sont exacts (P1 : 3, 4, 0, 9 ; P2 : 6, 0, 4, 12, 4).
Recalcul indépendant par décalage de chaîne et `zip` : mêmes valeurs.

### 2017 — jour 2 : Corruption Checksum

Tableur de **16 lignes × 16 colonnes**.

- **Partie 1 — 30994.** Pour chaque ligne, `max − min` ; on additionne les
  16 écarts.
- **Partie 2 — 233.** Pour chaque ligne, on cherche l'unique couple dont l'un
  divise l'autre exactement et l'on additionne les 16 quotients.

Exemples officiels : `5 1 9 5 / 7 5 3 / 2 4 6 8` → **18** ✔ et
`5 9 2 8 / 9 4 7 3 / 3 8 6 5` → **9** ✔. Recalcul indépendant (tri puis
recherche sur paires ordonnées) : mêmes valeurs ; l'unicité du couple
divisible est vérifiée sur les 16 lignes.

### 2017 — jour 3 : Spiral Memory

Spirale horaire, case 1 au centre, entrée **325489**.

- **Partie 1 — 552.** Distance de Manhattan : le numéro tombe en `(-267, -285)`.
  Formule : anneau `k = 285`, adossée au côté inférieur.
- **Partie 2 — 330785.** Spirale où chaque case vaut la **somme de ses 8
  voisines** ; première valeur dépassant 325489. Elle est en `(-1, 4)` et la
  valeur qui la précède vaut 312453 (< 325489), donc c'est bien la première.

Tests de l'énoncé : P1 `1→0, 12→3, 23→2, 1024→31` ✔ ; P2 `1→2, 2→4, 10→11,
100→122, 800→806` ✔. Recalcul indépendant par génération effective de la
spirale : position `(-267, -285)` → 552, première somme 330785.

### 2017 — jour 4 : High-Entropy Passphrases

**512** phrases de 4 à 11 mots.

- **Partie 1 — 466.** Phrases sans **aucun mot répété**.
- **Partie 2 — 251.** Phrases où aucun mot n'est une **anagramme** d'un autre
  (mots triés lettre par lettre). 215 phrases valides en partie 1 sont rejetées
  ici précisément à cause d'anagrammes.

Exemples officiels : P1 (3 lignes) → **2** ✔ ; P2 (5 lignes) → **3** ✔.
Recalcul indépendant par dictionnaires de fréquences : mêmes valeurs.

### 2017 — jour 5 : A Maze of Twisty Trampolines, All Alike

**1 059** offsets (de −1032 à 2).

- **Partie 1 — 355965.** L'offset quitté augmente toujours de 1.
- **Partie 2 — 26948068.** L'offset quitté diminue de 1 s'il vaut **3 ou plus**,
  augmente de 1 sinon.

Exemples officiels (`0 3 0 1 -3`) : P1 → **5** ✔, P2 → **10** ✔.
Recalcul indépendant (boucle `while` + `if` explicite, sans callback) : mêmes
valeurs. ~4 s pour les deux parties.

### 2017 — jour 6 : Memory Reallocation

**16** bancs, 112 blocs : `4 10 4 1 8 4 9 14 5 1 14 15 0 15 3 5`.

- **Partie 1 — 12841.** Cycles de redistribution avant de retrouver une
  configuration déjà vue.
- **Partie 2 — 8038.** Taille de la boucle : l'état répété `(1, 0, 14, 14, 12,
  11, 10, 9, 9, 7, 5, 5, 4, 3, 7, 1)` avait déjà été vu au cycle **4803**, d'où
  `12841 - 4803`.

Exemple officiel (`0 2 7 0`) : P1 → **5** ✔, P2 → **4** ✔.
Recalcul indépendant par division euclidienne `divmod(m, n)` au lieu d'une
boucle bloc par bloc : mêmes valeurs.

### 2017 — jour 7 : Recursive Circus

**1 230** programmes, 436 avec enfants, jusqu'à 7 enfants par nœud.

- **Partie 1 — `vgzejbd`.** La racine est le seul nom qui n'apparaît dans aucune
  liste d'enfants (unicité vérifiée).
- **Partie 2 — 1226.** Le fautif est **`kiatxq`** (poids propre 1232) : sa tour
  pèse 2096 alors que ses frères pèsent 2090. Ses trois enfants (`dispgy`,
  `irnjtjo`, `iqpoc`) sont pourtant équilibrés à 288 chacun → il devrait peser
  `1232 - 6 =` **1226**. Poids total de la racine : 955456.

Exemple officiel : racine `tknk`, poids corrigé **60** ✔.
Cas limite testé : fautif = feuille (`aaa (5) -> bbb, ccc, ddd` avec `ddd (12)`
→ 10) ✔ (un `set()` vide pour une feuille aurait fait échouer un test naïf).
Recalcul indépendant par récursion mémoïsée + `Counter` : `('kiatxq', 1226)` ✔.

### 2017 — jour 8 : I Heard You Like Registers

**1 000** instructions, **23** registres, les 6 opérateurs de condition
employés.

- **Partie 1 — 5143.** Plus grande valeur finale (registre `b` est le plus bas
  à −7741).
- **Partie 2 — 6209.** Plus grande valeur atteinte pendant l'exécution, pic
  supérieur au maximum final comme attendu.

Exemple officiel (4 lignes) : P1 → **1** ✔, P2 → **10** ✔.
Recalcul indépendant via `eval()` de la condition : mêmes valeurs.

### 2017 — jour 9 : Stream Processing

Flux d'une seule ligne, 28 913 caractères : **2 966** `{`, **1 064** déchets,
**7 937** annulations `!`.

- **Partie 1 — 21037.** Score = somme des profondeurs de chaque groupe.
- **Partie 2 — 9495.** Caractères de déchet non annulés (le plus long déchet
  fait 26 caractères).

Les **15 exemples officiels** passent tous (8 pour le score, 7 pour les déchets).
Recoupement par seconde méthode (purge `!.` puis regex `<([^>]*)>`) : 21037 et
9495 à l'identique.

### 2017 — jour 10 : Knot Hash

Entrée **227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144**.

- **Partie 1 — 13760.** Un seul tour sur la liste 0..255, produit des deux
  premiers éléments.
- **Partie 2 — `2da93395f1a6bb3472203252e3b17fe5`.** 64 tours avec suffixe
  `17, 31, 73, 47, 23`, XOR par blocs de 16, hexadécimal.

Exemples officiels : `[3,4,1,5]` → **12** ✔ ; hashes `""`, `AoC 2017`, `1,2,3`,
`1,2,4` tous ✔. Recalcul indépendant (indices circulaires puis XOR) : même hash.

⚠️ La valeur que je croyais être celle de `1,2,4` (`…13ed087ed58c1777b9bd`) était
**fausse** : l'officielle est `63960835bcdc130f0b66d7ff4f6a5a8e`, confirmée par
plusieurs sources. Ne pas la « corriger » de mémoire.

### 2017 — jour 11 : Hex Ed

**8 223** pas, 6 directions (1 701 `se`, 1 536 `s`, 1 336 `nw`, 1 331 `sw`,
1 295 `ne`, 1 024 `n`).

- **Partie 1 — 877.** Position finale en coordonnées cube `(329, -877, 548)`,
  distance `(|x|+|y|+|z|)/2`.
- **Partie 2 — 1622.** Distance maximale atteinte en cours de route.

Les 4 exemples officiels passent (`ne,ne,ne` → 3 ; `ne,ne,sw,sw` → 0 ;
`ne,ne,s,s` → 2 ; `se,sw,se,sw,sw` → 3). Recalcul indépendant en coordonnées
axiales : 877 / 1622 à l'identique.

### 2017 — jour 12 : Digital Plumber

**2 000** programmes (0 à 1999), liens symétriques dans le fichier.

- **Partie 1 — 113.** Taille du groupe contenant le programme 0.
- **Partie 2 — 202.** Nombre total de groupes ; le plus grand fait 143
  programmes, le plus petit 1.

Exemple officiel : P1 → **6** ✔, P2 → **2** ✔. Recalcul indépendant par
union-find (chemins compressés) : 113 / 202 à l'identique.

### 2017 — jour 13 : Packet Scanners

**43** scanners, profondeurs 0 à 98, fenêtres de 2 à 18. Un scanner de fenêtre
`n` est en position 0 aux temps multiples de `2(n-1)`.

- **Partie 1 — 632.** Sévérité des collisions à `t = 0`.
- **Partie 2 — 3849742.** Premier délai sans aucune collision (2,3 s).

Exemple officiel : P1 → **24** ✔, P2 → **10** ✔. Recoupements sur l'entrée
réelle : crible des délais interdits → 3849742 ; simulation physique du
va-et-vient (sans modulo) → 632.

⚠️ Piège rencontré : avancer le délai par PPCM des périodes déjà satisfaites
**rate la bonne réponse** (le délai n'appartient pas forcément à cette classe de
résidus). Ne pas réutiliser cette idée — le balayage exhaustif est correct et
suffisamment rapide.

### 2017 — jour 14 : Disk Defragmentation

Sel **`uugsqrei`**, grille 128 × 128 (ligne `i` = knot hash de `uugsqrei-i`).

- **Partie 1 — 8194.** Cases utilisées (soit ~50 % de la grille).
- **Partie 2 — 1141.** Régions : composantes connexes de `1` reliées
  orthogonalement.

Exemple officiel `flqrgnkx` : P1 → **8108** ✔, P2 → **1242** ✔ (et le début de
grille `d4f76bdc…` → `1101010011110111…` correspond à l'énoncé).
Recalcul indépendant (lignes en entiers 128 bits, flood-fill sur ensembles) :
8194 / 1141 à l'identique. Durée : 1,7 s pour les deux parties.

### 2017 — jour 15 : Dueling Generators

Départs **A = 783**, **B = 325** ; modulo 2147483647, facteurs 16807 / 48271.

- **Partie 1 — 650.** 16 bits de poids faible identiques sur 40 M de paires.
- **Partie 2 — 336.** Avec filtres (A multiples de 4, B multiples de 8),
  5 M de paires retenues.

Exemple officiel (65 / 8921) : P1 → **588** ✔, P2 → **309** ✔. Le couple
officiel `245556042 / 1431495498` est bien produit par le générateur.
Implémentations indépendantes Python et C : 650 / 336 à l'identique.
Durée en C : 0,19 s et 0,32 s (contre ~11 s en Python, car ni `rustc` ni
`numpy` ne sont disponibles).

### 2017 — jour 16 : Permutation Promenade

**10 000** mouvements (4 675 `x`, 3 082 `s`, 2 243 `p`), programmes `a`..`p`.

- **Partie 1 — `padheomkgjfnblic`.** Ordre après une danse.
- **Partie 2 — `bfcdeakhijmlgopn`.** Ordre après 1 000 000 000 danses : la
  permutation est **périodique de 60** (pré-période 0), et `1e9 mod 60 = 40`.
  Vérifié par simulation directe de 40 danses.

Exemple officiel (`s1,x3/4,pe/b` sur `abcde`) : 1 danse → **baedc** ✔,
2 danses → **ceadb** ✔. P1 recalculé par deux structures différentes
(liste de noms et dictionnaire nom→position) : identique. Durée : 0,6 s.

### 2017 — jour 17 : Spinlock

Pas **348**.

- **Partie 1 — 417.** Après 2017 insertions, le tampon fait 2 018 valeurs ; 2017
  est à l'indice 1819 et son voisin de droite est 417.
- **Partie 2 — 34334221.** 50 millions d'insertions sans construire le tampon :
  0 reste toujours en position 0, donc la réponse est la **dernière valeur
  insérée en position 1** (position suivie modulo la longueur).

Exemple officiel (pas 3) : P1 → **638** ✔, P2 → **1222153** ✔.
La méthode de la partie 2 a été confrontée à un vrai tampon pour les pas 3, 348
et 1 à 1 000 / 20 000 / 200 000 insertions : accord total. Durée : ~0,02 s (P1)
et ~2,9 s (P2).

### 2017 — jour 18 : Duet

Programme de **41** instructions (`set add mul mod jgz snd rcv`, registres
`a b f i p`).

- **Partie 1 — 2951.** Fréquence récupérée par le premier `rcv` déclenché.
- **Partie 2 — 7366.** Envois du programme 1 avec deux programmes en files de
  messages (`p = 0` et `p = 1`).

Exemples officiels : P1 → **4** ✔, P2 → **3** ✔. Recalcul indépendant (deques,
boucle par pas) : 2951 / 7366 à l'identique ; les deux files finissent vides.

⚠️ Piège rencontré : mon premier ordonnanceur de la partie 2 rendait la main dès
qu'un programme attendait, sans laisser l'autre progresser puis lui répondre —
il renvoyait 0. Il faut faire tourner chaque programme **jusqu'à son blocage**
et ne s'arrêter que lorsque **aucun** des deux ne progresse plus.

### 2017 — jour 19 : A Series of Tubes

Diagramme **201 × 201**, départ en `(0, 103)`, 10 lettres.

- **Partie 1 — `LXWCKGRAOY`.** Les 10 lettres de la grille sont visitées, sans
  doublon.
- **Partie 2 — 17302.** Cases parcourues jusqu'à sortir du diagramme.

Exemple officiel : P1 → **ABCDEF** ✔, P2 → **38** ✔ (les 8 segments donnés par
l'énoncé totalisent bien 38). Recalcul indépendant (virage choisi par test
explicite des 4 directions) : mêmes valeurs.

### 2017 — jour 20 : Particle Swarm

**1 000** particules (`p`, `v`, `a`), mise à jour semi-implicite (`v += a`, puis
`p += v`).

- **Partie 1 — 258.** Indice 0-based de la particule la plus proche à long
  terme. C'est la **seule** du jeu dont l'accélération est minimale
  (`|a|² = 1`) ; à `t = 10⁷` elle est toujours la plus proche
  (`(1398, -1069, 321)`, `v = (-59, 52, -15)`, `a = (-1, 0, 0)`).
- **Partie 2 — 707.** Particules restantes après destruction des collisions.

Exemples officiels : P1 → **0** ✔, P2 → **1** ✔ (4 particules → 3 collisions
simultanées à `t = 1`, puis 1 survivante).
Horizon de simulation **calculé**, pas deviné : racines entières des équations du
second degré par paire → dernier instant possible `t = 38`, qui est bien le
dernier tick meurtrier observé. Au-delà, stable jusqu'à 1 000 ticks.

⚠️ Piège majeur : chercher le **minimum de distance au cours du temps** donne 111,
qui est faux. La question porte sur la position **à long terme**, dominée par
l'accélération.

### 2017 — jour 21 : Fractal Art

Départ `.#./..#/###`, **108** règles (6 pour les blocs 2×2, 102 pour les 3×3),
chaque motif accepté sous ses **8 symétries**.

- **Partie 1 — 158.** Pixels `#` après 5 itérations (grille 18 × 18).
- **Partie 2 — 2301762.** Après 18 itérations (grille 2 187 × 2 187).

Exemple officiel (2 itérations) : grille intermédiaire `#..#/..../..../#..#` puis
**12** pixels ✔ — exactement les valeurs de l'énoncé. Recalcul indépendant
(indexation des blocs, rotations explicites) : 158 / 2301762 à l'identique.
Durée : 1,1 s pour les deux parties.

### 2017 — jour 22 : Sporifica Virus

Grille **25 × 25** (315 nœuds infectés), virus au centre orienté vers le haut,
grille creuse s'étendant à l'infini.

- **Partie 1 — 5256.** Rafales infectantes sur 10 000 (sain → gauche, infecté →
  droite).
- **Partie 2 — 2511345.** Sur 10 000 000 de rafales, avec quatre états
  (sain → affaibli → infecté → drapeau → sain).

Exemples officiels (`..#`/`#..`/`...#`) : P1 → **5** (7 rafales), **41** (70),
**5587** (10 000) ✔ ; P2 → **26** (100 rafales), **2511944** (10 M) ✔.
Durée : 3,6 s pour les deux parties.

### 2017 — jour 23 : Coprocessor Conflagration

Programme de **32** instructions (`set`, `sub`, `mul`, `jnz`), registres `a`–`h`.

- **Partie 1 — 3969.** Nombre d'exécutions de `mul` avec `a = 0`.
- **Partie 2 — 917.** Avec `a = 1`, le programme déroulé teste la primalité de
  `b` pour `b` allant de **106 500** à **123 500** par pas de **17** et compte
  les composites : **1 001** termes dont **84** premiers → **917** composites.

Les constantes sont lues dans le code (`set b 65`, `mul b 100`, `sub b -100000`,
`sub c -17000`, `sub b -17`), pas devinées. Cohérence vérifiée sur la structure
des boucles : `d` et `e` parcourent `2..b-1` (test de divisibilité), `f = 0`
signifie composite, et les bornes `b`/`c` correspondent exactement à `debut` et
`fin` (1 000 pas, dernier terme = `c`). Durée : 0,1 s.

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
