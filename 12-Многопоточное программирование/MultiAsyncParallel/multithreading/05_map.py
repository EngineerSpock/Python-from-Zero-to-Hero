import concurrent.futures

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    data = read_ints("..\\data\\1Kints.txt")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_three_sum, (data, data, data, data), ('t1', 't2', 't3', 't4'))
        print('After map')
        for r in results:
            print(f'{r=}')
        print('End of map')

    print('ended main')