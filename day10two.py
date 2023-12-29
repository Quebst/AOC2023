# S replacement is hard coded, south, i + 1, S becomes a '7' (value of 2)

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    grid = [list(line) for line in lines]

    start = [
        (i, j)
        for i, row in enumerate(grid)
        for j, char in enumerate(row)
        if char == "S"
    ]
    i, j = start[0]
    print(i, " ", j)
    direction_one = "South"
    actor_one_i = i + 1
    actor_one_j = j

    count = 1
    while True:
        count += 1
        actor_one_i, actor_one_j, direction_one = find_next(
            grid, actor_one_i, actor_one_j, direction_one
        )
        if grid[actor_one_i][actor_one_j] == "S":
            print("Hit the start!")
            grid[actor_one_i][actor_one_j] = 2
            break

    print("Count is: ", count)
    print("Steps are :", count // 2)

    total_area = 0
    for row in grid:
        in_loop = False
        turn_one = False

        for c in row:
            if c == 6:
                in_loop = not in_loop
            elif type(c) is int and 2 <= c <= 5:
                if turn_one == False:
                    turn_one = c
                else:
                    even_odd = (turn_one + c) % 2
                    if even_odd == 0:
                        in_loop = not in_loop

                    turn_one = False

            elif c == 0:
                continue
            else:
                if in_loop:
                    total_area += 1

    print("Area is: ", total_area)


# find next legal moves, return next pipe and direction
def find_next(grid, i, j, direction):
    char = grid[i][j]
    if direction == "North":
        if char == "|":
            grid[i][j] = 6
            i -= 1
        elif char == "7":
            grid[i][j] = 2
            j -= 1
            direction = "West"
        elif char == "F":
            grid[i][j] = 3
            j += 1
            direction = "East"
    elif direction == "South":
        if char == "|":
            grid[i][j] = 6
            i += 1
        elif char == "J":
            grid[i][j] = 5
            j -= 1
            direction = "West"
        elif char == "L":
            grid[i][j] = 4
            j += 1
            direction = "East"
    elif direction == "East":
        if char == "-":
            grid[i][j] = 0
            j += 1
        elif char == "7":
            grid[i][j] = 2
            i += 1
            direction = "South"
        elif char == "J":
            grid[i][j] = 5
            i -= 1
            direction = "North"
    elif direction == "West":
        if char == "-":
            grid[i][j] = 0
            j -= 1
        if char == "F":
            grid[i][j] = 3
            i += 1
            direction = "South"
        if char == "L":
            grid[i][j] = 4
            i -= 1
            direction = "North"

    return i, j, direction


if __name__ == "__main__":
    main()
