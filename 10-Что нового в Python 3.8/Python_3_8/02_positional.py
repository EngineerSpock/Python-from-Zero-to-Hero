# x = float('2.1')
# print(x)

# help(float)


def avg(a, b, c, /):
    return (a + b + c) / 3


print(avg(1, 2, 3))


# print(avg(a=1, b=2, c=3))

def aseert_equal(left, right, /, fail_message=''):
    return (left == right, fail_message)


aseert_equal(1, 1)
aseert_equal(1, 2, fail_message='left not equals right')


# aseert_equal(left=1, right=2)

def copy(source, destination, overwrite=False):
    print(f'copying {source} to {destination} with overwrite={overwrite}')


copy("C:\\tmp\\file1.txt", "C:\\tmp\\file1_copy.txt", overwrite=True)


# def copy(source, destination, /, *, overwrite=False):
#     print(f'copying {source} to {destination} with overwrite={overwrite}')


# copy("C:\\tmp\\file1.txt", "C:\\tmp\\file1_copy.txt", overwrite=True)
