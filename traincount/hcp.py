import random
import sys
import time


def get_deal():
    deal = []
    for suit in 'SHDC':
        for card in 'AKQJT98765432':
            deal.append((suit, card))
    return deal

HCP = dict(A=4, K=3, Q=2, J=1)

def main():
    t_start = time.time()
    n_correct = 0

    while True:
        deal = get_deal()
        random.shuffle(deal)
        hand = deal[:13]

        points = 0
        hand_suits = dict(S=[], H=[], D=[], C=[])
        for suit, card in hand:
            points += HCP.get(card, 0)
            hand_suits[suit].append(card)
        for suit in hand_suits.keys():
            hand_suits[suit] = sorted(hand_suits[suit], key=lambda card: (HCP.get(card, 0), card), reverse=True)

        print('\n')
        print_hand_suits(hand_suits)
        print('\n')

        try:
            x = int(sys.stdin.readline())
            if x == points:
                n_correct += 1
            else:
                print('wrong answer')
                break
        except:
            print('error input')
            break

        if time.time() - t_start > 60:
            print('time up')
            break

    print('you got {} right'.format(n_correct))

def print_hand_suits(hand_suits):
    for suit in 'SHDC':
        print(''.join(hand_suits[suit]))



if __name__ == '__main__':
    main()