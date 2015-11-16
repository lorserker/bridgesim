import sys
import random
import time


def count(known, total):
    t_start = time.time()
    n_correct = 0
    while True:
        shape = []
        
        n = total
        for _ in range(known):
            i = random.randint(0, min(total // 2 + 1, total-sum(shape)))
            shape.append(i)
            n -= i
            
        print(' '.join(map(str, shape)))
        
        x = sys.stdin.readline()
        
        try:
            x = int(x)
            if x == n:
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
    total = int(sys.argv[2])
    count(known, total)
