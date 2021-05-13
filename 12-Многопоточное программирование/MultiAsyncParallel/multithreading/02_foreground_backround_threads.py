import threading
import time

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')

    t1 = threading.Thread(target=count_three_sum, daemon=True, kwargs=dict(ints=ints))
    t1.start()

    print(input('What is your name?'))

    t1.join()
    print('ended main')
