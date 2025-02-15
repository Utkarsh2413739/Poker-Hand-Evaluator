
from collections import Counter

RANKS = "23456789TJQKA"
HAND_ORDER = ['High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']

def evaluate_hand(cards):
    ranks = sorted([RANKS.index(c[0]) for c in cards], reverse=True)
    suits = [c[1] for c in cards]
    rank_counts = Counter(ranks)
    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0]-5, -1))

    if is_straight and is_flush:
        return 'Straight Flush'
    elif 4 in rank_counts.values():
        return 'Four of a Kind'
    elif sorted(rank_counts.values()) == [2, 3]:
        return 'Full House'
    elif is_flush:
        return 'Flush'
    elif is_straight:
        return 'Straight'
    elif 3 in rank_counts.values():
        return 'Three of a Kind'
    elif list(rank_counts.values()).count(2) == 2:
        return 'Two Pair'
    elif 2 in rank_counts.values():
        return 'One Pair'
    else:
        return 'High Card'

hand = ['AH', 'KH', 'QH', 'JH', 'TH']
print(evaluate_hand(hand))
