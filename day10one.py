raw_data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

pipes = {
    "|": "north_south",
    "-": "east_west",
    "L": "north_east",
    "J": "north_west",
    "7": "south_west",
    "F": "south_east",
    ".": "ground",
    "S": "starting_location",
}


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
            break

    print("Count is: ", count)
    print("Steps are :", count // 2)


# find next legal moves, return next pipe and direction
def find_next(grid, i, j, direction):
    char = grid[i][j]
    if direction == "North":
        if char == "|":
            i -= 1
        elif char == "7":
            j -= 1
            direction = "West"
        elif char == "F":
            j += 1
            direction = "East"
    elif direction == "South":
        if char == "|":
            i += 1
        elif char == "J":
            j -= 1
            direction = "West"
        elif char == "L":
            j += 1
            direction = "East"
    elif direction == "East":
        if char == "-":
            j += 1
        elif char == "7":
            i += 1
            direction = "South"
        elif char == "J":
            i -= 1
            direction = "North"
    elif direction == "West":
        if char == "-":
            j -= 1
        if char == "F":
            i += 1
            direction = "South"
        if char == "L":
            i -= 1
            direction = "North"

    return i, j, direction


if __name__ == "__main__":
    main()
