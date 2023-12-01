raw_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()

    lines = read_data.splitlines()
    calib = []

    for line in lines:
        nums = [i for i in line if i.isdigit()]
        calib.append(int(nums[0] + nums[-1]))

    print(sum(calib))


if __name__ == "__main__":
    main()
