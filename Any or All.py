n = int(input())
a = list(map(int,input().split()))

all_positive = all(x > 0 for x in a)

has_palindrom = any(str(x) == str(x)[::-1] for x in a)

print(all_positive and has_palindrom)
