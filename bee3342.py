x = int(input())
if (x % 2) == 0:
    white = int(x*(x/2))
    black = int(white)
else:
    black = int((x*((x-1)/2))+((x-1)/2))
    white = int(black + 1)

print(f"{white} casas brancas e {black} casas pretas")
