num_of_test_case = int(input())

for i in range(num_of_test_case):
    a, b, c, n = map(int, input().split())

    max_coin = max(a, b, c)
    A = max_coin - a
    B = max_coin - b
    C = max_coin - c
    #print(max_coin)
    if a == b and b == c:
        A = B = C = 0

    if (A + B + C) > n:
        print("NO")
    elif (A + B + C) < n:
        if (n-(A+B+C)) % 3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")