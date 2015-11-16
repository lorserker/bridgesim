from redeal import *
from collections import Counter

import random

predeal = {'W': H('AQ6 AJ3 KJ6543 T')}

def initial():
    global TABLE
    global CNT
    global WIN_SAMPLE
    global LOSE_SAMPLE
    TABLE = Payoff(('2HN', '2SW'), imps)
    CNT = Counter()
    WIN_SAMPLE = set()
    LOSE_SAMPLE = set()

def accept(deal):
    if not balanced(deal.south):
        return False
    if deal.south.hcp < 12 or deal.south.hcp > 15:
        return False
    if len(deal.south.spades) > 4:
        return False
    if len(deal.south.diamonds) < 3:
        return False
    if deal.east.hcp > 5:
        return False
    if deal.east.hcp >= 3 and len(deal.east.spades) >= 6:
        return False
    if deal.east.hcp >= 5 and len(deal.east.spades) >= 5:
        return False
    if deal.east.hcp > 3 and len(deal.east.diamonds) > 2:
        return False
    if len(deal.east.clubs) > 6:
        return False
    if len(deal.north.hearts) < 5:
        return False
    if deal.north.hcp > 8:
        return False
    if deal.north.hcp > 5 and len(deal.north.hearts) > 5:
        return False

    return True

def do(deal):
    score_2s = deal.dd_score('2SW')
    # if random.random() < 0.25:
    #     score_2s = deal.dd_score('2SXW')
    # if score_2s < 0:
    #     if random.random() < 0.75:
    #         score_2s = deal.dd_score('2SXW')

    if len(deal.east.spades) == 3 and len(deal.east.diamonds) >= 3 or len(deal.east.spades) < 3 and len(deal.east.diamonds) >= 2:
        score_2s = deal.dd_score('3DW')
        # if random.random() < 0.25:
        #     score_2s = deal.dd_score('3DXW')
        # if score_2s < 0:
        #     score_2s = deal.dd_score('3DXW')
        #     if random.random() < 0.75:
        #         score_2s = deal.dd_score('3DXW')

    if len(deal.east.spades) == 4 and 'A' in str(deal.east):
        score_2s = deal.dd_score('3SW')

    score_2h = -deal.dd_score('2HN')

    TABLE.add_data({'2HN': score_2h, '2SW': score_2s})

    if len(deal.east.spades) == 4:
        CNT['4'] += 1
    if len(deal.east.spades) == 5:
        CNT['5'] += 1

    if score_2s > score_2h:
        CNT['better_bid'] += 1
        WIN_SAMPLE.add((deal, score_2h, score_2s))
    else:
        LOSE_SAMPLE.add((deal, score_2h, score_2s))

    #EV.append(score_2s + score_2h)

    print('{} | {} {}'.format(deal, score_2h, score_2s))

def final(n_tries):
    TABLE.report()

    print(CNT)

    print('winning examples')
    for ex in list(WIN_SAMPLE)[:10]:
        print('{} | {} {}'.format(ex[0], ex[1], ex[2]))
    print('losing examples')
    for ex in list(LOSE_SAMPLE)[:10]:
        print('{} | {} {}'.format(ex[0], ex[1], ex[2]))


