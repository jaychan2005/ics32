# lecture 1

n = 4

print('Regular!')

for i in range(n):
    print('* ' * (i + 1))

# OR

for i in range(n):
    for j in range(i + 1):
        print("* ", end='')
    print()
    
print('Reverse!')

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(n - i):
        print('*', end='')
    print()
    
for i in range(n):
    for j in range(n):
        if i > j:
            print(' ', end='')
        else:
            print('*', end='')
    print()