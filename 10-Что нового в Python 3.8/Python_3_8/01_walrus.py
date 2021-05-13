walrus = False
print(walrus)

print(walrus := True)
print(type(walrus))

rows = input('Enter the number of rows')
for i in range(int(rows)):
    print('*' * (i + 1))
print(f'Number of rows:{rows}')
import random

for i in range(rows := int(input('Enter the number of rows'))):
    print('*' * (i + 1))
print(f'Number of rows:{rows}')


def read_file(fp):
    while True:
        line = fp.readline()
        if not line:
            break

        split_line = line.split(';')
        print(split_line[1])


def read_file2(fp):
    while line := fp.readline():
        if not line:
            break

        split_line = line.split(';')
        print(split_line[1])


def get_mode():
    return 's' if random.randint(1, 10) > 5 else None


mode = get_mode()
if mode:
    full_mode_name = 'silent' if mode == 's' else 'unknown'
    print(f'processing in {full_mode_name} mode')

if mode := get_mode():
    full_mode_name = 'silent' if mode == 's' else 'unknown'
    print(f'processing in {full_mode_name} mode')
