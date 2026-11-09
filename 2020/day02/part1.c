#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_file(const char *chemin_fichier, char **contenu) {
    FILE *fichier = fopen(chemin_fichier, "r");
    if (fichier == NULL) {
        printf("Erreur : Le fichier '%s' est introuvable.\n", chemin_fichier);
        return;
    }

    fseek(fichier, 0, SEEK_END);
    long taille = ftell(fichier);
    fseek(fichier, 0, SEEK_SET);

    *contenu = (char *)malloc(taille + 1);
    fread(*contenu, 1, taille, fichier);
    (*contenu)[taille] = '\0';

    fclose(fichier);
}

void get_variables(const char *line, float *mini, float *maxi, char *letter, char *text) {
    sscanf(line, "%f-%f %s %[^\n]", mini, maxi, letter, text);
    letter[strcspn(letter, ":")] = '\0'; // Remove the colon
}

int main(int argc, char **argv) {
    char *contenu = NULL;
    /* L'entrée du puzzle vit dans le dossier inputs/ de l'année. */
    const char *path = argv[1] ? argv[1] : "2020/inputs/day02.txt";
    read_file(path, &contenu);
    if (contenu == NULL) {
        return 1;
    }

    char *line = strtok(contenu, "\n");
    int n = 0;

    while (line != NULL) {
        float mini, maxi;
        char letter[2], text[256];
        get_variables(line, &mini, &maxi, letter, text);

        int count = 0;
        for (char *p = text; *p != '\0'; p++) {
            if (*p == letter[0]) {
                count++;
            }
        }

        if (mini <= count && count <= maxi) {
            n++;
        }

        line = strtok(NULL, "\n");
    }

    printf("%d\n", n);
    free(contenu);
    return 0;
}