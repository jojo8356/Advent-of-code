/* 2017, jour 15 : Dueling Generators — partie 1.
 *
 * 40 millions de paires, 16 bits de poids faible comparés.
 * Version C de part1.py : même algorithme, ~50 fois plus rapide.
 */
#include <stdio.h>
#include <stdlib.h>

#define MODULO 2147483647LL
#define FACTEUR_A 16807LL
#define FACTEUR_B 48271LL
#define MASQUE 0xFFFFLL
#define PAIRES 40000000LL

/* Lit les deux valeurs de départ (chacune est le seul nombre de sa ligne). */
static int lire_departs(const char *chemin, long long *a, long long *b)
{
    FILE *f = fopen(chemin, "r");
    if (!f) { perror(chemin); return 0; }
    char mot[128];
    long long vals[2];
    int n = 0;
    while (fscanf(f, "%127s", mot) == 1) {
        char *fin;
        long long v = strtoll(mot, &fin, 10);
        if (*fin == '\0' && n < 2) vals[n++] = v;
    }
    fclose(f);
    if (n != 2) { fprintf(stderr, "deux valeurs attendues\n"); return 0; }
    *a = vals[0];
    *b = vals[1];
    return 1;
}

int main(int argc, char **argv)
{
    long long a = 0, b = 0;
    if (argc > 1) {
        if (!lire_departs(argv[1], &a, &b)) return 1;
    } else if (scanf("%lld %lld", &a, &b) != 2) {
        fprintf(stderr, "entrée attendue\n");
        return 1;
    }

    long long total = 0;
    for (long long i = 0; i < PAIRES; i++) {
        a = (a * FACTEUR_A) % MODULO;
        b = (b * FACTEUR_B) % MODULO;
        if ((a & MASQUE) == (b & MASQUE)) total++;
    }
    printf("Paires identiques: %lld\n", total);
    return 0;
}
