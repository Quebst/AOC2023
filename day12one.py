raw_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

raw_data2 = """??? 1"""

BROKEN = "#"
WORK = "."
UNKNOWN = "?"


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    total_arrange = 0

    for line in lines:
        encoded, counts = line.split()
        groups = counts.split(",")
        brokes = list(map(int, groups))
        broke_sum = sum(brokes)
        works = len(encoded) - broke_sum
        print(brokes)
        encoded = encoded + "..."

        total_arrange += arrange(encoded, brokes)
        print(total_arrange)


# Recursive function to find all possible arrangements
# string, list -> 1 if option found, 0 if not
#
def arrange(text, brokes):
    # print(text)
    if len(text) == 1 and len(brokes) == 0:
        print("------------------------")
        return 1
    elif len(text) == 1:
        return 0

    # 3 possibilities based on current character
    current_char = text[:1]
    if current_char == WORK:
        return arrange(text[1:], brokes)

    if len(brokes) == 0:
        if BROKEN in text:
            return 0
    else:
        broke = brokes[0]

    if current_char == BROKEN:
        if insert_broken(text, broke):
            return arrange(text[broke + 1 :], brokes[1:])
        else:
            return 0

    elif current_char == UNKNOWN:
        total = arrange(text[1:], brokes)
        if len(brokes) != 0 and insert_broken(text, broke):
            total += arrange(text[broke + 1 :], brokes[1:])

        return total


# attempts to insert broken plus "." unless at end of text
# return true if successful, else false
# accepts single broke and a text area
def insert_broken(text, broke):
    if broke > len(text):
        return False

    # Makes sure all eligible spaces are either # or ?
    i = 0
    while i < broke:
        if text[i] == WORK:
            return False
        i += 1

    # check that next space is either UKNOWN or WORK

    if text[broke] != BROKEN:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
