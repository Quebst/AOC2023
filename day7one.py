raw_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

cards = {
    'A' : '14',
    'K' : '13',
    'Q' : '12',
    'J' : '11',
    'T' : '10',
    '9' : '09',
    '8' : '08',
    '7' : '07',
    '6' : '06',
    '5' : '05',
    '4' : '04',
    '3' : '03',
    '2' : '02',
}

winners = {
    'Five of a kind' : '90',
    'Four of a kind' : '80',
    'Full house' : '70',
    'Three of a kind' : '60',
    'Two pair' : '50',
    'One pair' : '40',
    'High card' : '20',
}

# Hand strength is a single number, first 2 digits hand, next 10 digits strength of each card in order
# example: QT5Q5 = 501210051205

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    h_hands = []
    lines = read_data.splitlines()
    total_score = 0
    for line in lines:
        hand, bid = line.split()
        h_hands.append([hash_hand(hand), int(bid)])
        
    h_hands.sort()
    print(h_hands)
    
    for i in range(len(h_hands)):
        temp = h_hands[i][1] * (i + 1)
        print(temp)
        total_score += temp
        
    print("Total score: ", total_score)


def hash_hand(hand):
    # Determineing hands len(counts)
    # 1 -> 5 of a kind
    # 2 -> 4 of a kind or full house
    # 3 -> 2 pair or three of a kind
    # 4 -> 1 pair
    # 5 -> High card
    rank = "rank not set"
    counts = {}
    card_values = ""
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
        card_values = card_values + cards[card]
        
    length = len(counts)
    
    if length == 1:
        rank = "Five of a kind"
    elif length == 2:
        if max(counts.values()) == 4:
            rank = "Four of a kind"
        else:
            rank = "Full house"
    elif length == 3:
        if max(counts.values()) == 3:
            rank = "Three of a kind"
        else:
            rank = "Two pair"
    elif length == 4:
        rank = "One pair"
    elif length == 5:
        rank = "High card"
    else:
        print("Length out of bounds")
        
    hashed = winners[rank] + card_values
    
    return int(hashed)
    


if __name__ == "__main__":
    main()