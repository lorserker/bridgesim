import sys
import time

from redeal import *

Hand.set_str_style('long')

def main():
    dealer = Deal.prepare({})

    t_start = time.time()
    n_correct = 0

    while True:
        deal = dealer()
        
        print('\n')
        print(' '.join([
            str(deal.south.spades),
            str(deal.south.hearts),
            str(deal.south.diamonds),
            str(deal.south.clubs),
        ]))
        print('\n')

        try:
            x = int(sys.stdin.readline())
            if x == deal.south.hcp:
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

if __name__ == '__main__':
    main()