def is_lucky_ticket(ticket):
    n = len(ticket)
    if n % 2 == 0:
        half = n // 2
        first_half = ticket[:half]
        second_half = ticket[half:]
        if sum(map(int, first_half)) == sum(map(int, second_half)):
            return True


n = int(input())
tickets = input().split()
list_of_tickets = list(tickets)
count = 0

for element in tickets:
    for i in tickets:
        if is_lucky_ticket(element + i):
            count = count + 1

print(count)
