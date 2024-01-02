import math

x, y = map(int, input().split())
titan = list(input())

height = 0
len_titan = list(map(int, input().split()))

for i in range(len(titan)):
    if titan[i] == 'M':
        height += len_titan[1]
    if titan[i] == 'P':
        height += len_titan[0]
    if titan[i] == 'G':
        height += len_titan[2]

print(math.ceil(height/y))
