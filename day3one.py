raw_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_data = """100..........50
&.............&
...............
...........%666
.......*.......
......25.......
...............
...............
#..........55&.
800..........30"""

# Solution is 537732 for part 1

grid = []


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    rows = read_data.splitlines()
    height = len(rows)
    width = len(rows[0])
    score = 0
    num_length = 0
    number = ""

    for row in rows:
        grid.append(list(row))

    for i in grid:
        print(i)

    for i in range(height):
        for j in range(width):
            if grid[i][j].isdecimal():
                number = number + str(grid[i][j])
                num_length += 1
                if j == width - 1:
                    # print(number, " is ", num_length)
                    if check_number(i, j - num_length + 1, num_length, height, width):
                        score += int(number)
                    num_length = 0
                    number = ""

            else:
                if len(number) > 0:
                    # print(number, " is ", num_length)
                    if check_number(i, j - num_length, num_length, height, width):
                        score += int(number)
                num_length = 0
                number = ""

    print("Score is: ", score)


# i, j is first digit, num_length is length
# need to check above line, line of, and below line
def check_number(i, j, num_length, height, width):
    numbers = []
    k = j - 1
    numbers.append([i, k])
    numbers.append([i, j + num_length])

    while k <= j + num_length:
        numbers.append([i - 1, k])
        numbers.append([i + 1, k])
        k += 1

    for number in numbers:
        if 0 <= number[0] < height and 0 <= number[1] < width:
            if is_symbol(grid[number[0]][number[1]]):
                return True

    print("Number at ", i, " ", j, " is false")
    print("number starts with ", grid[i][j])
    return False


def is_symbol(char_check):
    if char_check == ".":
        return False
    if char_check.isdecimal():
        return False
    return True


if __name__ == "__main__":
    main()
