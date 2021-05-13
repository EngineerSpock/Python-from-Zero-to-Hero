import threading
import time

throw = False


def count():
    i = 0

    try:
        while True:
            if throw:
                raise ZeroDivisionError()

            i += 1
            print(f'{i=}')
            time.sleep(1)
    except ZeroDivisionError:
        print('Exception occured')


if __name__ == '__main__':
    print('started main')

    t1 = threading.Thread(target=count)
    t1.start()

    # try:
    #     t1.start()
    # except:
    #     print(f'Excepted')

    time.sleep(3)

    throw = True

    for x in range(1, 5):
        print(f'{x=}')
        time.sleep(1)
    print('ended main')
