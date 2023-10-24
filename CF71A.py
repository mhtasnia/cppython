num_of_test_case = int(input())
for i in range(num_of_test_case):
    x = input()
    a = len(x)
    if a <= 10:
        print(x)
    else:
        z = list(x)
        y = list(x)
        y.pop(a-1)
        y.pop(0)
        print(z[0], end="")
        print(len(y), end="")
        print(z[a-1])
