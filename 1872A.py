import math

num_of_test_case = int(input())
for i in range(num_of_test_case):
    a, b, c = map(int, input().split())
    if a == b:
        turn = 0
    else:
        bigger_vessel = max(a, b)
        smaller_vessel = min(a, b)
        equal_part = (bigger_vessel + smaller_vessel) / 2
        gap = equal_part - smaller_vessel
        if gap < c:
            turn = 1
        else:
            turn = math.ceil(gap / c)

    print(turn)