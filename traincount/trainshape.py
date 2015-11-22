import sys
import time

from redeal import *

def train_shape(known):
    dealer = Deal.prepare({})
    t_start = time.time()
    n_correct = 0
    while True:
        deal = dealer()
        shape = [
            len(deal.south.spades),
            len(deal.south.hearts),
            len(deal.south.diamonds),
            len(deal.south.clubs)
        ]
            
        print(' '.join(map(str, shape[:known])))
        
        x = sys.stdin.readline()
        
        try:
            x = int(x)
            if x == sum(shape[known:]):
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
    known = int(sys.argv[1])
    train_shape(known)
