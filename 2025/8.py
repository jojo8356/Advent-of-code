import sys
from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

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
        self.size[px] += self.size[py]
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def get_circuit_sizes(self):
        sizes = []
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                sizes.append(self.size[i])
        return sizes


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

    # Connect the 1000 closest pairs using Union-Find
    uf = UnionFind(n)
    num_connections = min(1000, len(distances))

    for k in range(num_connections):
        dist_sq, i, j = distances[k]
        uf.union(i, j)

    # Get circuit sizes and find top 3
    sizes = uf.get_circuit_sizes()
    sizes.sort(reverse=True)

    # Multiply top 3 sizes
    result = 1
    for i in range(min(3, len(sizes))):
        result *= sizes[i]

    return result


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
