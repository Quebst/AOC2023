raw_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()

    words = read_data.split(",")
    total_score = 0
    boxes = {}
    focal = -1

    for word in words:
        # print(word)
        if "=" in word:
            code, focal = word.split("=")
            key = hashed(code)
            flag = True
            # update in place if in dictionary

            if key in boxes:
                i = 0
                while i < len(boxes[key]):
                    if boxes[key][i][0] == code:
                        boxes[key][i][1] = focal
                        flag = False
                        break
                    i += 1

                if flag:
                    boxes[key].append([code, focal])
            else:
                boxes[key] = [[code, focal]]

        else:
            code = word[:-1]
            key = hashed(code)

            # remove item if it exists, else ignore
            if key in boxes:
                i = 0
                while i < len(boxes[key]):
                    if boxes[key][i][0] == code:
                        del boxes[key][i]
                    i += 1

    # print(boxes)
    total_score = focus_power(boxes)
    print("Total score is: ", total_score)


def focus_power(boxes_total):
    total_score = 0

    for box in boxes_total:
        i = 0
        while i < len(boxes_total[box]):
            total = (1 + box) * (i + 1) * (int(boxes_total[box][i][1]))
            total_score += total
            i += 1

    return total_score


def hashed(word):
    score = 0
    for char in word:
        score += ord(char)
        score = score * 17
        score = score % 256

    return score


if __name__ == "__main__":
    main()
