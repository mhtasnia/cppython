num_of_contestant, problem_limit = map(int, input().split())
count = 0

contestant_result = list(map(int, input().split()))

for score in contestant_result:
    if score >= contestant_result[problem_limit - 1] and score > 0:
        count += 1

print(count)
