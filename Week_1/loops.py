for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

lines=int(input("Enter number of lines: "))+1
for i in range(1, lines, 1):
    for j in range(1, i+1, 1):
        print('*', end=' ')
    print()