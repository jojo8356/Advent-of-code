import sys
from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same circuit
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.num_components -= 1
        return True


def distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2


def solve(lines):
    # Parse junction box positions
    boxes = []
    for line in lines:
        line = line.strip()
        if line:
            x, y, z = map(int, line.split(','))
            boxes.append((x, y, z))

    n = len(boxes)
    if n < 2:
        return 0

    # Calculate all pairwise distances
    distances = []
    for i, j in combinations(range(n), 2):
        dist_sq = distance_squared(boxes[i], boxes[j])
        distances.append((dist_sq, i, j))

    # Sort by distance
    distances.sort()

    # Connect pairs until all in one circuit
    uf = UnionFind(n)
    last_i, last_j = 0, 0

    for dist_sq, i, j in distances:
        if uf.union(i, j):
            last_i, last_j = i, j
            if uf.num_components == 1:
                break

    # Multiply X coordinates of the last two connected boxes
    return boxes[last_i][0] * boxes[last_j][0]


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()
