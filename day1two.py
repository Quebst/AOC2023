W_NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()

    lines = read_data.splitlines()
    calib = []

    for line in lines:
        for j, numb_text in enumerate(W_NUMBERS):
            line = fix_number(line, numb_text, j + 1)

        nums = [i for i in line if i.isdigit()]
        calib.append(int(nums[0] + nums[-1]))

    print(sum(calib))


# take in a line and insert digits into 2nd char of string numbers
# unfixed is line, num_text is text of number, numb is digit
def fix_number(unfixed, num_text, numb):
    position = unfixed.find(num_text)

    if position == -1:
        return unfixed

    unfixed = unfixed[: position + 1] + str(numb) + unfixed[position + 2 :]

    return fix_number(unfixed, num_text, numb)


if __name__ == "__main__":
    main()
