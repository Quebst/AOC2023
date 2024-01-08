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
    # 919 by 912 movement
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    instructs = []
    for row in lines:
        direct, length, col = row.split()
        instructs.append([direct, int(length)])

    # determining board size
    # up     down  left  right
    # -186   88   -288   200

    board = [[0 for _ in range(600)] for y in range(300)]
    start = (200, 300)
    # board = [[0 for _ in range(20)] for y in range(20)]
    # start = (5, 5)

    board[start[0]][start[1]] = 1
    cursor = list(start)

    for instruct in instructs:
        cursor = dig(board, cursor, instruct[0], instruct[1])

    # p_board(board)
    print("-----------------------------------------------")
    flood_fill(board, find_inside(board))
    # p_board(board)

    print("Total score is: ", calc_score(board))


# dig holes, return new cursor
def dig(board, cursor, direct, holes):
    x, y = cursor
    if direct == "U":
        for _ in range(holes):
            x -= 1
            board[x][y] = 1
    elif direct == "D":
        for _ in range(holes):
            x += 1
            board[x][y] = 1
    elif direct == "L":
        for _ in range(holes):
            y -= 1
            board[x][y] = 1
    elif direct == "R":
        for _ in range(holes):
            y += 1
            board[x][y] = 1
    else:
        print(direct)
        raise (ValueError)

    print([x, y])
    return [x, y]


def p_board(board):
    for row in board:
        print(row)


def find_inside(board):
    return [199, 299]
    # return [201, 301]


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


if __name__ == "__main__":
    main()
