
n, m = map(int, input().split())

is_colored = False

for _ in range(n):
    row = input().split()
    for pixel in row:
        if pixel in ('C', 'M', 'Y'):
            is_colored = True
            break


if is_colored:
    print("#Color")
else:
    print("#Black&White")