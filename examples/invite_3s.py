from redeal import *

vuln = True


predeal = {'S': H('AQ963 AQT6 K9 85')}

def initial():
    global TABLE

    TABLE = Payoff(('pass', 'bid3S', 'bid4S'), matchpoints)


def accept(deal):
    if deal.north.hcp < 5 or deal.north.hcp > 9:
        return False
    if len(deal.north.spades) != 3:
        return False
    return True


def do(deal):
    score_pass = deal.dd_score('2SS', vuln)
    score_4s = deal.dd_score('4SS', vuln)
    if deal.north.hcp > 7:
        score_3s = score_4s
    else:
        score_3s = deal.dd_score('3SS', vuln)

    TABLE.add_data({'pass': score_pass, 'bid3S': score_3s, 'bid4S': score_4s})

    print('{} | {} {} {}'.format(deal, score_pass, score_3s, score_4s))


def final(n_tries):
    TABLE.report()

