raw_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    cards = read_data.splitlines()
    total_score = 0

    for card in cards:
        card_score = 0
        _, numbers = card.split(":")
        winning, have_numbs = numbers.split("|")
        winning = winning.split()
        have_numbs = have_numbs.split()

        print(winning)
        print(have_numbs)

        for win in winning:
            if win in have_numbs:
                if card_score == 0:
                    card_score = 1
                else:
                    card_score = card_score * 2

        print("Card Score : ", card_score)
        total_score = total_score + card_score

    print("Game Score : ", total_score)


if __name__ == "__main__":
    main()
