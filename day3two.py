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
possible_gears = []


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
                    if check_number(
                        i, j - num_length + 1, num_length, height, width, number
                    ):
                        score += int(number)
                    num_length = 0
                    number = ""

            else:
                if len(number) > 0:
                    # print(number, " is ", num_length)
                    if check_number(
                        i, j - num_length, num_length, height, width, number
                    ):
                        score += int(number)
                num_length = 0
                number = ""

    print("Score is: ", score)

    ratio_total = 0
    while len(possible_gears) > 0:
        tester = possible_gears.pop()
        count = 1
        g_ratio = 1
        for gear in possible_gears:
            if tester.i == gear.i and tester.j == gear.j:
                count += 1
                g_ratio = int(gear.numb) * int(tester.numb)
        if count > 2:
            print("Count is greater than 2!")

        if count == 2:
            ratio_total += g_ratio

    print(ratio_total)


class Gear:
    def __init__(self, i, j, numb) -> None:
        self.i = i
        self.j = j
        self.numb = numb


# i, j is first digit, num_length is length
# need to check above line, line of, and below line
def check_number(i, j, num_length, height, width, numb):
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
            if is_symbol(grid[number[0]][number[1]], number, numb):
                return True

    return False


def is_symbol(char_check, number, numb):
    if char_check == "*":
        new_gear = Gear(number[0], number[1], numb)
        possible_gears.append(new_gear)
        return True

    if char_check == ".":
        return False
    if char_check.isdecimal():
        return False
    return True


if __name__ == "__main__":
    main()
