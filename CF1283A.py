t = int(input())

for _ in range(t):
    h, m = map(int, input().split())

    minutes_before_new_year = (23 - h) * 60 + (60 - m)

    print(minutes_before_new_year)
