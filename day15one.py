raw_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()

    words = read_data.split(",")
    total_score = 0

    for word in words:
        # print(word)
        total_score += hashed(word)

    print("Total score is: ", total_score)


def hashed(word):
    score = 0
    for char in word:
        score += ord(char)
        score = score * 17
        score = score % 256

    return score


if __name__ == "__main__":
    main()
