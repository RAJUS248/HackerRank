
N = int(input())
sets = list(map(int,input().split()))

captain = (sum(set(sets))*N - sum(sets))// (N-1)
print(captain)

# OR

N = int(input())
rooms = list(map(int, input().split()))

a = set()
b = set()

for room in rooms:
    if room not in a:
        a.add(room)        # mark it as seen
        b.add(room)        # first time → candidate for captain
    else:
        b.discard(room)    # second time → not captain, remove

b = list(b)
print(b[0])

"""
Output Format

Output the Captain's room number.

Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families.
In the given list, all of the numbers repeat  times except for room number .
Hence,  is the Captain's room number.

"""