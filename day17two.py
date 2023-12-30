# currently returns 995 instead of 993

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

raw_data2 = """111111111111
999999999991
999999999991
999999999991
999999999991"""

raw_data3 = """19999
29999
39999
49999
59999
69999
79999"""

frontier = Frontier()
visited = set()


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = [[9999 for _ in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = int(lines[i][j])

    start = [1, 1]
    goal = [len(lines), len(lines[0])]
    first_node = Node(1, 1, None, 0, 90, heur(start, goal))
    frontier.add(first_node)

    print("---------------------------------")

    while True:
        cnode = frontier.pop()

        # if current node is goal
        if goal == [cnode.x, cnode.y]:
            print("Total score is: ", cnode.tcost)

            print(find_path(cnode))
            # p_board(board, find_path(cnode))
            break

        visited.add(cnode)

        neighs = neighbors([cnode.x, cnode.y], cnode.line, board)
        for n in neighs:
            x, y = n[0]
            line = n[1]
            xcost = n[2]
            if xcost < 0:
                continue
            new_cost = cnode.cost + board[x][y] + heur([x, y], goal) + xcost
            new_node = Node(
                x, y, cnode, (cnode.cost + board[x][y] + xcost), line, new_cost
            )
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
        return hash(str(self.x) + "x" + str(self.y) + "x" + str(self.line))


def heur(cords, goal):
    x, y = cords
    goal_x, goal_y = goal
    distance = goal_x - x + goal_y - y
    if distance < 5:
        return 0
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


# find next chunk four away, else return cost of -1 to skip
# returns value of middle 2 skipped nodes
def four_chunk(x, y, fourx, foury, board):
    if x <= 0 or fourx <= 0 or y <= 0 or foury <= 0:
        return -1
    if (
        x >= len(board) - 1
        or fourx >= len(board) - 1
        or y >= len(board[0]) - 1
        or foury >= len(board[0]) - 1
    ):
        return -1
    if x > fourx:
        swap = x
        x = fourx
        fourx = swap

    if y > foury:
        swap = y
        y = foury
        foury = swap

    xcost = 0
    for _ in range(fourx - x):
        x += 1
        xcost += board[x][y]

    for _ in range(foury - y):
        y += 1
        xcost += board[x][y]

    return xcost


# line N = 20, E = 40, S = 60, W =80
# second digit is number of times in a row, ie 41,42,43,44
def neighbors(cords, line, board):
    x, y = cords
    valids = []
    first, last = divmod(line, 10)

    # WORKING HERE remember to redo starting value of line
    if first == 2:
        valids.append(([x, y + 4], 41, four_chunk(x, y, x, y + 3, board)))
        valids.append(([x, y - 4], 81, four_chunk(x, y, x, y - 3, board)))
        if last != 7:
            valids.append(([x - 1, y], line + 1, 0))
    elif first == 6:
        valids.append(([x, y + 4], 41, four_chunk(x, y, x, y + 3, board)))
        valids.append(([x, y - 4], 81, four_chunk(x, y, x, y - 3, board)))
        if last != 7:
            valids.append(([x + 1, y], line + 1, 0))
    elif first == 4:
        valids.append(([x + 4, y], 61, four_chunk(x, y, x + 3, y, board)))
        valids.append(([x - 4, y], 21, four_chunk(x, y, x - 3, y, board)))
        if last != 7:
            valids.append(([x, y + 1], line + 1, 0))
    elif first == 8:
        valids.append(([x + 4, y], 61, four_chunk(x, y, x + 3, y, board)))
        valids.append(([x - 4, y], 21, four_chunk(x, y, x - 3, y, board)))
        if last != 7:
            valids.append(([x, y - 1], line + 1, 0))
    elif first == 9:
        valids.append(([x, y + 4], 41, four_chunk(x, y, x, y + 3, board)))
        valids.append(([x + 4, y], 61, four_chunk(x, y, x + 3, y, board)))
    return valids


if __name__ == "__main__":
    main()
