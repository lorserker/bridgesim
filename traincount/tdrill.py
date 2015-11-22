import sys
import time

from redeal import *

def timed_drill(what, known):
    dealer = Deal.prepare({})
    t_start = time.time()
    n_correct = 0
    while True:
        deal = dealer()

        if what == "shape":
            values = [
                len(deal.south.spades),
                len(deal.south.hearts),
                len(deal.south.diamonds),
                len(deal.south.clubs)
            ]
        elif what == "points":
            values = [
                deal.north.hcp,
                deal.east.hcp,
                deal.south.hcp,
                deal.west.hcp,
            ]
            
        print(' '.join(map(str, values[:known])))
        
        x = sys.stdin.readline()
        
        try:
            x = int(x)
            if x == sum(values[known:]):
                n_correct += 1
            else:
                print('wrong answer')
                break
            if time.time() - t_start > 60:
                break
        except:
            print('wrong answer')
            break
    print('time\'s up!')        
    print('you got {} right'.format(n_correct))

if __name__ == '__main__':
    what = sys.argv[1]
    known = int(sys.argv[2])
    timed_drill(known)
