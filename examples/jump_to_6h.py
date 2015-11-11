from redeal import *

vuln = True

#predeal = {'S': H('K73 62 A975 A753'), 'N': H('- KQ8754 - -')}
#predeal = {'S': H('K73 J2 A975 A753'), 'N': H('- KQ8754 - -')}
#predeal = {'S': H('K73 62 AJ75 A753'), 'N': H('- KQ8754 - -')}
predeal = {'S': H('K73 62 A975 A953'), 'N': H('- KQ8754 - -')}

def initial():
    global TABLE

    TABLE = Payoff(('4H', '6H'), imps)


def accept(deal):
    if not weak_two(deal.west, 'spades'):
        return False
    if deal.east.hcp > 11:
        return False
    # if len(deal.east.spades) < 3:
    #     return False

    shearts = str(deal.north.hearts)
    if len(shearts) < 6:
        return False
    if deal.north.hcp > 16:
        # if len(shearts) == 6 and not (shearts.startswith('AK') or shearts.startswith('AQJ') or shearts.startswith('KQJ')):
        #     return False
        return True
    elif deal.north.hcp > 12:
        if len(shearts) < 7:
            return False
        # if not shearts.startswith('AK') or shearts.startswith('AQJ') or shearts.startswith('KQJ'):
        #     return False
        return True
    else:
        return False


def do(deal):
    score_4h = deal.dd_score('4HN', vuln)
    score_6h = deal.dd_score('6HN', vuln)

    print('{} | {} {}'.format(deal, score_4h, score_6h))

    TABLE.add_data({'4H':score_4h, '6H':score_6h})


def final(n_tries):
    TABLE.report()


def weak_two(hand, suitname):
    if hand.hcp < 5 or hand.hcp > 10:
        return False
    suit = getattr(hand, suitname)
    if len(suit) != 6:
        return False
    if hand.shape not in Shape("6322") + Shape("6331"):
        return False
    if not good_suit(suit):
        return False
    return True


def good_suit(suit):
    scards = str(suit)
    if scards.startswith('AK') or scards.startswith('AQ') or scards.startswith('AJ') or scards.startswith('AT'):
        return True
    if scards.startswith('KJT') or scards.startswith('KQ'):
        return True
    if scards.startswith('QJT'):
        return True
    return False