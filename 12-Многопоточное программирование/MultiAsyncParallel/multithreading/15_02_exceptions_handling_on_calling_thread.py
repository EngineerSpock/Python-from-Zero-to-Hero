import time
import concurrent.futures
from concurrent.futures import CancelledError


def div(divisor, limit):
    print(f'started div = {divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'divisor={divisor}, x={x}')
        time.sleep(0.2)

    print('raise exception')
    raise Exception('bad things happen!')

    return result


if __name__ == '__main__':
    print('started main')

    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        res_list = executor.map(div, (3, 5), (15, 25))
        while res_list:
            try:
                cur_res = next(res_list)
            except StopIteration:
                print('stop iteration excepted')
                break
            except Exception as ex:
                print('generalized exception')
                print(repr(ex))

    print('main ended')


# if __name__ == '__main__':
#     print('started main')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#         future = executor.submit(div, 3, 15)
#
#         time.sleep(5)
#         print('Nothing happens until...')
#
#         try:
#             res = future.result()
#         except CancelledError as ex:
#             print(repr(ex))
#         except TimeoutError as ex:
#             print(repr(ex))
#         except Exception as ex:
#             print(repr(ex))
#
#     print('main ended')
