from collections import Counter 

X = int(input())
shoes = list(map(int, input().split()))
N = int(input())

keyvalues = Counter(shoes)
earnings = 0
for _ in range(N):
    size,price = map(int, input().split())
    if keyvalues[size] > 0:
        earnings += price
        keyvalues[size] -= 1
        
print(earnings)

