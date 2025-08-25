T = int(input())   # number of test cases

for _ in range(T):
    N = int(input())
    A = set(map(int, input().split()))
    N2 = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
