# Day 23 part 2
from copy import deepcopy

raw_data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

test_data = """#.############
#.......####.#
#######.####.#
#######......#
#######.####.#
############.#"""


START = (1, 1)


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = raw_data.splitlines()
    # board = [[999 for x in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    grid = [list(line) for line in lines]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "#":
                grid[i][j] = "."

    grid[0][1] = "#"
    goal = tuple([len(lines) - 1, len(lines[0]) - 2])
    edges = []
    path = []
    front = set()
    longest_path = 0
    qedges = []
    forks = {}

    first_edge = Edge([[START[0], START[1]], [START[0], START[1]]], 0)
    qedges.append([first_edge, 1])
    find_edges(edges, qedges, grid)

    # for e in edges:
    #     print(e)

    find_forks(edges, forks)

    # for fork in forks:
    #     print(f"Fork: {fork} Values: {len(forks[fork])}")

    edge_one = forks[START][0]
    # print(edge_one)
    epoint = deepcopy(edge_one.ends)
    epoint.remove(list(START))
    epoint = tuple(epoint[0])

    first_node = Node(edge_one, epoint, None, edge_one.mag, set())
    first_node.visited.add(START)
    first_node.visited.add(epoint)

    neighs = deepcopy(forks[epoint])
    neighs = [e for e in neighs if e != edge_one]

    for n in neighs:
        parent = first_node
        temp = deepcopy(n.ends)
        temp.remove(list(epoint))
        temp = tuple(temp[0])
        nnode = Node(n, temp, parent, first_node.tcost + n.mag + 1, first_node.visited)
        front.add(nnode)

    while front:
        nodel = front.pop()
        if nodel.endpoint == goal:
            if nodel.tcost > longest_path:
                longest_path = nodel.tcost
                print(f"Longest path is : {longest_path} path: {nodel.visited}")
                # path = find_path(nodel)
                # print(path)
            continue

        neighs = deepcopy(forks[nodel.endpoint])
        neighs = [e for e in neighs if e != nodel.aedge]

        for n in neighs:
            temp = deepcopy(n.ends)
            temp.remove(list(nodel.endpoint))
            temp = tuple(temp[0])
            if temp not in nodel.visited:
                nnode = Node(n, temp, nodel, nodel.tcost + n.mag + 1, nodel.visited)
                front.add(nnode)


def find_forks(edges, forks):
    for edge in edges:
        if edge.mag == 0:
            pass
        else:
            for x in edge.ends:
                key = tuple(x)
                if key not in forks:
                    forks[key] = []
                forks[key].append(edge)


# Directions: N = 0, E = 1, S = 2, W = 3
def find_edges(edges, qedges, grid):
    while qedges:
        temp = qedges.pop()
        nedge = temp[0]
        dir = temp[1]
        newx, newy = nedge.ends[1]
        grid[newx][newy] = "."

        while grid[newx][newy] == ".":
            neighs = next(grid, newx, newy)
            grid[newx][newy] = "#"
            newxx = newx
            newyy = newy

            for n in neighs:
                # if new neigh is in same direction, continue
                if n == dir:
                    if len(neighs) > 1:
                        edges.append(nedge)
                        nedge = Edge([[newxx, newyy], [newxx, newyy]], 0)

                    if dir == 0:
                        newx -= 1
                    elif dir == 1:
                        newy += 1
                    elif dir == 2:
                        newx += 1
                    elif dir == 3:
                        newy -= 1
                    else:
                        print("No direction found")
                    nedge.mag += 1
                    nedge.ends[1] = [newx, newy]

                # start new edges if not in line
                elif n % 2 != dir % 2:
                    new_edge = Edge([[newxx, newyy], [newxx, newyy]], 0)
                    qedges.append([new_edge, n])
        else:
            edges.append(nedge)

        print(nedge)


# returns coords and direction of new edges
# Directions: N = 0, E = 1, S = 2, W = 3
def next(grid, x, y):
    # tests = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    valids = []

    if x >= len(grid) - 1:
        return valids

    if grid[x - 1][y] == ".":
        valids.append(0)
    if grid[x + 1][y] == ".":
        valids.append(2)
    if grid[x][y - 1] == ".":
        valids.append(3)
    if grid[x][y + 1] == ".":
        valids.append(1)

    return tuple(valids)


def find_path(endnode):
    path = []
    while endnode:
        path.append([endnode.x, endnode.y])
        endnode = endnode.parent
    return path[::-1]


# visited is a set
class Node:
    def __init__(self, aedge, endpoint, parent, tcost, visited):
        self.aedge = aedge
        self.parent = parent
        self.tcost = tcost
        self.endpoint = endpoint
        self.visited = deepcopy(visited)
        self.visited.add(self.endpoint)

    def __repr__(self):
        return f"node x:{self.x} y:{self.y} parent:{self.parent} cost:{self.cost} line:{self.line} tcost:{self.tcost}"


# direction
class Edge:
    def __init__(self, ends, mag):
        self.ends = ends
        self.mag = mag
        self.connects = []
        
        def __eq__(self, other):
            return (
            isinstance(other, Edge) and
            self.ends == other.ends and
            self.mag == other.mag 
        )

    def __hash__(self):
        return hash((self.ends, self.mag))

    def __repr__(self):
        return f"edge ends: {self.ends} mag: {self.mag} connects: {self.connects}"


if __name__ == "__main__":
    main()
