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
#............#
#............#
############.#"""



START = [0, 1]

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    #board = [[999 for x in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    grid = [list(line) for line in lines]
    grid[0][1] = "#"
    goal = [len(lines) - 1, len(lines[0]) - 2]
    
    path = []
    front = set()
    longest_path = 0
    
    
    first_node = Node(START[0] + 1, START[1], None, 0, set())
    first_node.visited.add(tuple([first_node.x, first_node.y]))
    
    neighs = next(grid, first_node.x, first_node.y)
    
    for n in neighs:
        parent = first_node
        nnode = Node(n[0], n[1], parent, first_node.tcost + 1, first_node.visited)
        front.add(nnode)
        
    while front:
        nodel = front.pop()
        if nodel.x == goal[0] and nodel.y == goal[1]:
            if nodel.tcost > longest_path:
                longest_path = nodel.tcost
                print(longest_path + 1)
                #path = find_path(nodel)
                #print(path)
            continue
        
        neighs = next(grid, nodel.x, nodel.y)
    
        for n in neighs:
            if tuple([n[0], n[1]]) not in nodel.visited:
                nnode = Node(n[0], n[1], nodel, nodel.tcost + 1, nodel.visited)
                front.add(nnode)
            
        
# (^, >, v, and <)
def next(grid, x, y):
    #tests = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
    valids = []
    
    if x >= len(grid) - 1:
        return valids
    
    if grid[x - 1][y] == "." or grid[x - 1][y] == "^":
        valids.append([x - 1, y])
    if grid[x + 1][y] == "." or grid[x + 1][y] == "v":
        valids.append([x + 1, y])
    if grid[x][y - 1] == "." or grid[x][y - 1] == "<":
        valids.append([x, y - 1])
    if grid[x][y + 1] == "." or grid[x][y + 1] == ">":
        valids.append([x, y + 1])
        
    return valids
    
def find_path(endnode):
    path = []
    while endnode:
        path.append([endnode.x, endnode.y])
        endnode = endnode.parent
    return path[::-1]       

class Node:
    def __init__(self, x, y, parent, tcost, visited):
        self.x = x
        self.y = y
        self.parent = parent
        self.tcost = tcost
        self.visited = deepcopy(visited)
        self.visited.add(tuple([self.x, self.y]))
        
    def __repr__(self):
        return f"node x:{self.x} y:{self.y} parent:{self.parent} cost:{self.cost} line:{self.line} tcost:{self.tcost}"
    



if __name__ == "__main__":
    main()
