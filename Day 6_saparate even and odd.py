N = int(input())
for _ in range(N):
    string = input()
    odd_string = string[1::2]
    even_string = string[0::2]
    print(even_string, odd_string)

"""
string = "raja"

even_chars = []
odd_chars = []
for i, ch in enumerate(string):
    if i % 2 == 0:
        even_chars.append(ch)
    else:
        odd_chars.append(ch)

even_chars = "".join(even_chars)
odd_chars = "".join(odd_chars)
print(even_chars,odd_chars)

"""
