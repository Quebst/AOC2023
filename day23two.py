# Day 23 part 2
from copy import copy, deepcopy

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

test_data2 = """#.############
#.......####.#
###.###......#
#.#.########.#
#............#
############.#"""


START = (1, 1)


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
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
    front = []
    longest_path = 0
    qedges = []
    forks = {}

    first_edge = Edge([[START[0], START[1]], [START[0], START[1]]], 0)
    
    # Hardcoded in direction to south = 2, east = 1
    qedges.append([first_edge, 2])
    find_edges(edges, qedges, grid)

    find_forks(edges, forks)

    found = True
    while found:
        found = combine_edges(edges, forks)
        forks.clear()
        find_forks(edges, forks)
    

    edge_one = forks[START][0]
    # print(edge_one)
    epoint = deepcopy(edge_one.ends)
    epoint.remove(list(START))
    epoint = tuple(epoint[0])

    first_node = Node(edge_one, epoint, None, edge_one.mag + 1, set())
    first_node.visited.add(START)
    first_node.visited.add(epoint)

    neighs = forks[epoint]
    neighs = [e for e in neighs if e != edge_one]

    for n in neighs:
        parent = first_node
        temp = deepcopy(n.ends)
        temp.remove(list(epoint))
        temp = tuple(temp[0])
        nnode = Node(n, temp, parent, first_node.tcost + n.mag, first_node.visited)
        front.append(nnode)

    while front:
        nodel = front.pop()
        if nodel.endpoint == goal:
            #print("*", end="", flush=True)
            if nodel.tcost > longest_path:
                longest_path = nodel.tcost
                print(f"Longest path is : {longest_path} path: {nodel}")
                # path = find_path(nodel)
                # print(path)
            continue

        neighs = forks[nodel.endpoint]
        neighs = [e for e in neighs if e != nodel.aedge]

        for n in neighs:
            temp = deepcopy(n.ends)
            temp.remove(list(nodel.endpoint))
            temp = tuple(temp[0])
            if temp not in nodel.visited:
                nnode = Node(n, temp, nodel, nodel.tcost + n.mag, nodel.visited)
                front.append(nnode)


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
        temp = qedges.pop(0)
        nedge = temp[0]
        dir = temp[1]
        newx, newy = nedge.ends[1]
        grid[newx][newy] = "."

        while grid[newx][newy] == ".":
            
            neighs = next(grid, newx, newy)
            grid[newx][newy] = "X"
            
            if dir in neighs:
                flag = True
                neighs.remove(dir)
            else:
                flag = False
            

            for n in neighs:
                newxx = newx
                newyy = newy
                
                if n == 0:
                    newxx -= 1
                elif n == 1:
                    newyy += 1
                elif n == 2:
                    newxx += 1
                elif n == 3:
                    newyy -= 1
                
                
                new_edge = Edge([[newx, newy], [newxx, newyy]], 1)
                qedges.append([new_edge, n])
            
            # Two cases, has neighs or does not
            
            if flag and len(neighs) > 0:
                edges.append(nedge)
                nedge = Edge([[newx, newy], [newx, newy]], 0)
                
                
            if flag:
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
                
                if grid[newx][newy] == "X":
                    edges.append(nedge)
                    break
                    
        else:  
            edges.append(nedge)


        #print(nedge)

def combine_edges(edges, forks):
    found = False
    for f in forks:
        if len(forks[f]) == 2:
            found = True
            newmag = forks[f][0].mag + forks[f][1].mag
            newcords = []
            
            if forks[f][0].ends[0] == forks[f][1].ends[0]:
                newcords = [forks[f][0].ends[1], forks[f][1].ends[1]]
            elif forks[f][0].ends[0] == forks[f][1].ends[1]:
                newcords = [forks[f][0].ends[1], forks[f][1].ends[0]]
            elif forks[f][0].ends[1] == forks[f][1].ends[0]:
                newcords = [forks[f][0].ends[0], forks[f][1].ends[1]]
            elif forks[f][0].ends[1] == forks[f][1].ends[1]:
                newcords = [forks[f][0].ends[0], forks[f][1].ends[0]]
                
            new_edge = Edge(newcords, newmag)
            
            edges.remove(forks[f][0])
            edges.remove(forks[f][1])
            edges.append(new_edge)
            return found
            
    

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

    return valids


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
        return f"node aedge:{self.aedge} endpoint:{self.endpoint} tcost:{self.tcost}"


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
