num_of_test_case = int(input())
for i in range(num_of_test_case):
    a, b, c, d = map(int, input().split())

    skills = [a, b, c, d]
    skills.sort()

    if (skills[2] == max(a, b) and skills[3] == max(c, d)) or (skills[2] == max(c, d) and skills[3] == max(a, b)):
        print("YES")
    else:
        print("NO")
