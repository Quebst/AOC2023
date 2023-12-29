import heapq


class Frontier:
    def __init__(self):
        self.heap = []
        self.unique = set()

    def add(self, d):
        if not d in self.unique:
            heapq.heappush(self.heap, d)
            self.unique.add(d)

    def pop(self):
        d = heapq.heappop(self.heap)
        self.unique.remove(d)
        return d


raw_data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

frontier = Frontier()
visited = set()


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = [[9999 for _ in range(len(lines) + 2)] for y in range(len(lines[0]) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = int(lines[i][j])

    start = [1, 1]
    goal = [len(lines), len(lines[0])]
    first_node = Node(1, 1, None, 0, 60, heur(start, goal))
    frontier.add(first_node)

    print("---------------------------------")

    while True:
        cnode = frontier.pop()

        # if current node is goal
        if goal == [cnode.x, cnode.y]:
            print(f"Found goal at: ")
            print("Total score is: ", cnode.tcost)

            print(find_path(cnode))
            # p_board(board, find_path(cnode))
            break

        visited.add(cnode)

        neighs = neighbors([cnode.x, cnode.y], cnode.line)
        for n in neighs:
            x, y = n[0]
            line = n[1]
            new_cost = cnode.cost + board[x][y] + heur([x, y], goal)
            new_node = Node(x, y, cnode, (cnode.cost + board[x][y]), line, new_cost)
            frontier.add(new_node)


class Node:
    def __init__(self, x, y, parent=None, cost=0, line=0, tcost=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.line = line
        self.tcost = tcost

    def __lt__(self, other):
        return self.tcost < other.tcost

    def __repr__(self):
        return f"node x:{self.x} y:{self.y} parent:{self.parent} cost:{self.cost} line:{self.line} tcost:{self.tcost}"

    def __str__(self):
        return f"node x:{self.x} y:{self.y} parent:{self.parent} cost:{self.cost} line:{self.line} tcost:{self.tcost}"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.line == other.line:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.x * 100000 + self.y + self.line * 100)


def heur(cords, goal):
    x, y = cords
    goal_x, goal_y = goal
    distance = goal_x - x + goal_y - y
    return distance


def find_path(endnode):
    path = []
    while endnode:
        path.append([endnode.x, endnode.y])
        endnode = endnode.parent
    return path[::-1]


def p_board(board, path):
    for p in path:
        x, y = p
        board[x][y] = 0
    for row in board:
        print(row)


# S, N, E, W
# line N = 20, E = 40, S = 60, W =80
# second digit is number of times in a row, ie 41,42,43,44
def neighbors(cords, line):
    x, y = cords
    valids = []
    first, last = divmod(line, 10)
    
    if first == 2:
        valids.append(([x, y + 1], 41))
        valids.append(([x, y - 1], 81))
        if last != 3:
            valids.append(([x - 1, y], line + 1))
    elif first == 6:
        valids.append(([x, y + 1], 41))
        valids.append(([x, y - 1], 81))
        if last != 3:
            valids.append(([x + 1, y], line + 1))
    elif first == 4:
        valids.append(([x + 1, y], 61))
        valids.append(([x - 1, y], 21))
        if last != 3:
            valids.append(([x, y + 1], line + 1))
    elif first == 8:
        valids.append(([x + 1, y], 61))
        valids.append(([x - 1, y], 21))
        if last != 3:
            valids.append(([x, y - 1], line + 1))

    return valids


if __name__ == "__main__":
    main()
