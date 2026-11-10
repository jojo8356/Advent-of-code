/* 2017, jour 15 : Dueling Generators — partie 2.
 *
 * Filtres : A ne garde que les multiples de 4, B que les multiples de 8.
 * 5 millions de paires retenues, 16 bits de poids faible comparés.
 */
#include <stdio.h>
#include <stdlib.h>

#define MODULO 2147483647LL
#define FACTEUR_A 16807LL
#define FACTEUR_B 48271LL
#define MASQUE 0xFFFFLL
#define PAIRES 5000000LL

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
        do { a = (a * FACTEUR_A) % MODULO; } while (a & 3);
        do { b = (b * FACTEUR_B) % MODULO; } while (b & 7);
        if ((a & MASQUE) == (b & MASQUE)) total++;
    }
    printf("Paires identiques (filtrées): %lld\n", total);
    return 0;
}
