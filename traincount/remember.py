import sys
import time

from redeal import *

HIGH = set(list('AKQJT98'))
LOW = set(list('765432x'))

def compare_hands(h1, h2):
    score = 0
    for suit1, suit2 in zip(h1, h2):
        suit1, suit2 = suit1.upper(), suit2.upper()
        if len(suit1) != len(suit2):
            score -= 2
            continue
        suit1, suit2 = set(list(suit1)), set(list(suit2))
        n_high = len(suit1.intersection(HIGH))
        missed = len(suit1.intersection(HIGH) - suit2.intersection(HIGH))
        wrong = len(suit2.intersection(HIGH) - suit1.intersection(HIGH))
        score = score - missed - wrong + n_high - missed
    return score

def recall_drill(tlook=5, n=10):
    score = 0
    dealer = Deal.prepare({})

    for i in range(10):
        print(100*'\n')
        deal = dealer()

        print('\n')
        str_suits = [str(deal.south.spades), str(deal.south.hearts), str(deal.south.diamonds), str(deal.south.clubs)]
        n_high_cards = 0
        for s in str_suits:
            for c in s:
                if c in HIGH:
                    n_high_cards += 1
        print(' '.join(str_suits))
        print('\n')

        time.sleep(tlook + n_high_cards)

        print(100*'\n')

        try:
            hand_in = sys.stdin.readline().split()
            hand_score = compare_hands(str_suits, hand_in)
            score += hand_score
            print(' '.join(str_suits))
            print(hand_score)
        except:
            print('error input')
            break

        print('\n{}. score = {} (press ENTER)\n\n'.format(i+1, score))
        sys.stdin.readline()


if __name__ == '__main__':
    tlook = int(sys.argv[1])
    recall_drill()