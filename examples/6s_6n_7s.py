from redeal import *

predeal = {'S': H('AQ87532 8 AJ A32'), 'N':H('K A - -')}

def initial():
    global TABLE
    TABLE = Payoff(('6S', '6N', '7S', '7N'), imps)

def accept(deal):
    if deal.north.hcp < 11:
        return False
    if len(deal.north.spades) < 3:
        return False
    kings = [int('K' in str(deal.north.hearts)), int('K' in str(deal.north.diamonds)), int('K' in str(deal.north.clubs))]
    if sum(kings) != 2:
        return False

    return True

def do(deal):
    score_6s = deal.dd_score('6SS')
    score_6n = deal.dd_score('6NN')
    score_7s = deal.dd_score('7SS')
    score_7n = deal.dd_score('7NN')

    print('{} | {} {} {} {}'.format(deal, score_6s, score_6n, score_7s, score_7n))

    scores = {'6S': score_6s, '6N': score_6n, '7S': score_7s, '7N': score_7n}

    TABLE.add_data(scores)


def final(n_tries):
    TABLE.report()

    #print(n_tries)