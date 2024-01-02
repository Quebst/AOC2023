

raw_data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


def main():
    # 0 means R, 1 means D, 2 means L, and 3 means U
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    instructs = []
    nodes = []
    #split the hex lines into base 10
    for row in lines:
        direct, length, col = row.split()
        direct = int(col[-2])
        length = int(col[2:7], 16)
        #print(length)
        
        instructs.append([direct, length])
    # instructs = []
    # for row in lines:
    #     direct, length, col = row.split()
    #     if direct == "R":
    #         direct = 0
    #     elif direct == "D":
    #         direct = 1
    #     elif direct == "L":
    #         direct = 2
    #     elif direct == "U":
    #         direct = 3
    #     instructs.append([direct, int(length)])

    print(instructs)
    #nodes.append(Node(0, 0, 0, 0))

    # 0 means R, 1 means D, 2 means L, and 3 means U
    # create a node for each intersection
    xpos, ypos = 0, 0
    lastdir = 3
    xxs = []
    yys = []
    turn = "R"
    magsum = 0
    for inst in instructs:
        direct, mag = inst
        magsum += mag
        if direct == 3:
            xpos -= mag
            if lastdir == 0:
                turn = "L"
            else:
                turn = "R"                           
        elif direct == 1:
            xpos += mag
            if lastdir == 2:
                turn = "L"
            else:
                turn = "R"                
        elif direct == 2:
            ypos -= mag
            if lastdir == 3:
                turn = "L"
            else:
                turn = "R"       
        elif direct == 0:
            ypos += mag
            if lastdir == 1:
                turn = "L"
            else:
                turn = "R"        
        else:
            print(direct)
            raise (ValueError)
        xxs.append(xpos)
        yys.append(ypos)
        
        nodes.append(Node(xpos, ypos, direct, turn))
        
        
    # for node in nodes:
    #     print(node)
        
    print(xxs)
    print(yys)
    print(magsum)
    
    sl = shoelace(xxs, yys)
    
    print(1 + sl + magsum/2)


def shoelace(xx, yy):
	return abs(sum(xx[i-1]*yy[i]-xx[i]*yy[i-1] for i in range(len(xx)))) / 2.
    
    

# go through nodes, when there are two right turns add space to total
# and delete a node
def trans(x, y, nodes):
    removed_area = 0
    i = 2
    twoago = nodes[0]
    twoturn = twoago.turn
    oneago = nodes[1]
    oneturn = oneago.turn
    
    


# 0 means R, 1 means D, 2 means L, and 3 means U
class Node:
    def __init__(self, x, y, direct, turn):
        self.x = x
        self.y = y
        self.direct = direct
        self.turn = turn
        
    def __str__(self):
        return f"Node at x:{self.x} y:{self.y} dir:{self.direct} turn:{self.turn} "
        
        
        
# dig holes, return new cursor
# 0 means R, 1 means D, 2 means L, and 3 means U
def dig(board, cursor, direct, holes):
    x, y = cursor
    if direct == 3:
        for _ in range(holes):
            x -= 1
            board[x][y] = 1
    elif direct == 1:
        for _ in range(holes):
            x += 1
            board[x][y] = 1
    elif direct == 2:
        for _ in range(holes):
            y -= 1
            board[x][y] = 1
    elif direct == 0:
        for _ in range(holes):
            y += 1
            board[x][y] = 1
    else:
        print(direct)
        raise (ValueError)

    #print([x, y])
    return [x, y]


def p_board(board):
    for row in board:
        print(row)


def find_inside(board):
    #return [199, 299]
    return [2, 2]


def flood_fill(board, cords):
    x, y = cords
    board[x][y] = 1
    fillables = []
    fillables.append(cords)

    while fillables:
        x, y = fillables.pop()
        board[x][y] = 1
        if board[x - 1][y] == 0:
            fillables.append([x - 1, y])
        if board[x + 1][y] == 0:
            fillables.append([x + 1, y])
        if board[x][y - 1] == 0:
            fillables.append([x, y - 1])
        if board[x][y + 1] == 0:
            fillables.append([x, y + 1])


def calc_score(board):
    total_score = 0

    for row in board:
        for num in row:
            total_score += num

    return total_score

# 0 means R, 1 means D, 2 means L, and 3 means U
def find_board_size(instructs):
    mup, mdown, mleft, mright = 0, 0, 0, 0
    up, down, left, right = 0, 0, 0, 0
    vert, horz = 0, 0
    for row in instructs:
        print(row)
        if row[0] == 3:
            up += row[1]
            vert -= row[1]
        elif row[0] == 1:
            down += row[1]
            vert += row[1]
        elif row[0] == 2:
            left += row[1]
            horz -= row[1]
        elif row[0] == 0:
            right += row[1]
            horz += row[1]
        
        if vert < mup:
            mup = vert
        if vert > mdown:
            mdown = vert
        if horz < mleft:
            mleft = horz
        if horz > mright:
            mright = horz
        
    print(up, " ", down, " ", left, " ", right)
    print(mup, " ", mdown, " ", mleft, " ", mright) 

if __name__ == "__main__":
    main()
