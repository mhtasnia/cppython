# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
char = ".|."


for i in range(1, n, 2):
    # print(i)
    print(('-') * int((m-3*i)/2) + char * i + ('-') * int((m-3*i)/2))

print(('-') * int((m-7)/2) + 'WELCOME' + ('-') * int((m-7)/2))

for i in range(n-2, 0, -2):
    # print(i)
    print(('-') * int((m-3*i)/2) + char * i + ('-') * int((m-3*i)/2))


##link: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
