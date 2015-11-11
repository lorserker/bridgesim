from redeal import *

predeal = {'S': H('J8 AQT5 QT AQ843')}

vuln = True

def initial():
    global TABLE
    global N_GAME

    TABLE = Payoff(('pass', 'bid2N', 'bid3N'), imps)
    N_GAME = 0


def accept(deal):
    if deal.north.hcp < 6 or deal.north.hcp > 9:
        return False
    if len(deal.north.spades) > 3 or len(deal.north.hearts) > 3 or len(deal.north.diamonds) > 4:
        return False

    return True


def do(deal):
    global N_GAME
    score_pass = deal.dd_score('1NN', vuln)
    score_3n = deal.dd_score('3NN', vuln)
    if deal.north.hcp >= 8:
        score_2n = deal.dd_score('3NN', vuln)
    else:
        score_2n = deal.dd_score('2NN', vuln)

    print('{} | {} {} {}'.format(deal, score_pass, score_2n, score_3n))

    if score_3n > 0:
        N_GAME += 1

    TABLE.add_data({'pass': score_pass, 'bid2N': score_2n, 'bid3N': score_3n})


def final(n_tries):
    TABLE.report()

    print(N_GAME)