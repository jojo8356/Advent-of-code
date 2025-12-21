#include <stdio.h>
#include <stdlib.h>

int house_presents(int target) {
    int limit = target / 10;
    int *houses = (int*)calloc(limit + 1, sizeof(int));
    if (!houses) {
        fprintf(stderr, "Memory allocation failed\n");
        return -1;
    }

    for (int elf = 1; elf <= limit; elf++) {
        for (int house = elf; house <= limit; house += elf) {
            houses[house] += elf * 10;
        }
    }

    int result = -1;
    for (int i = 1; i <= limit; i++) {
        if (houses[i] >= target) {
            result = i;
            break;
        }
    }

    free(houses);
    return result;
}

int main() {
    int target = 33100000;
    int lowest_house = house_presents(target);
    if (lowest_house != -1) {
        printf("Lowest house number with at least %d presents is: %d\n", target, lowest_house);
    } else {
        printf("Error: could not find a house.\n");
    }
    return 0;
}
