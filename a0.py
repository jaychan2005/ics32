number = int(input())

print('+-+')
print('| |')
space = ''
for i in range(number - 1):
    print(space, end='')
    print('+-+-+')
    space = space + '  '
    print(space, end='')
    print('| |')
print(space, end='')
print('+-+')