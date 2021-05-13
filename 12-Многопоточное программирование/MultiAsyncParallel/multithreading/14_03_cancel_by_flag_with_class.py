import threading
import time

from multithreading.count_three_sum import read_ints


class ThreeSumTask:

    def __init__(self, ints):
        self.ints = ints
        self.canceled = False
        self.lock_obj = threading.Lock()

    def run(self):
        self.count_three_sum(self.ints)

    def cancel(self):
        with self.lock_obj:
            self.canceled = True

    def count_three_sum(self, ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.canceled:
                        print('Task was Cancelled')
                        counter = -1
                        return counter

                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found:{ints[i]}, {ints[j]}, {ints[k]}', end='\n')

        print(f'ended count_three_sum. Triplets counter={counter}')
        return counter


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')

    task = ThreeSumTask(ints)
    t1 = threading.Thread(target=task.run)
    t1.start()

    time.sleep(5)

    task.cancel()

    t1.join()

    print('ended main')
