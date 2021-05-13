import threading
import time

from multithreading.count_three_sum import read_ints


class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def stopped(self):
        return self.stop_event.is_set()


class ThreeSumUnitOfWork(StoppableThread):

    def __init__(self, ints, name='TestThread'):
        super().__init__(name=name)
        self.ints = ints
        # self.stop_event = threading.Event()

    def run(self):
        print(f'{self.getName()} starts')

        self.count_three_sum(self.ints)

        print(f'{self.getName()} ends')

    # def stop(self):
    #     self.stop_event.set()

    def count_three_sum(self, ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if super().stopped():
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

    task = ThreeSumUnitOfWork(ints)
    task.start()

    time.sleep(10)

    task.stop()

    task.join()

    print(task.stopped())
    print('ended main')
