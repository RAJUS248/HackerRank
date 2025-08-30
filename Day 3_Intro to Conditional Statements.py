N = int(input().strip())
if N >= 6 and N <= 20:
    print("Weird")

elif N % 2 == 0:       
    print("Not Weird")

elif N > 20 and N % 2 != 0:
    print("Weird")


"""
Problem: Conditional Statements in Python
Objective

In this challenge, we learn about conditional statements.

Task

Given an integer N, perform the following conditional actions:

If N is odd, print "Weird".

If N is even and in the inclusive range [2, 5], print "Not Weird".

If N is even and in the inclusive range [6, 20], print "Weird".

If N is even and greater than 20, print "Not Weird".

Input Format

A single line containing a positive integer, N.

Constraints

1 ≤ N ≤ 100

Output Format

Print "Weird" if the number is weird. Otherwise, print "Not Weird".

Sample Input 0
3

Sample Output 0
Weird

Explanation 0

N = 3 → odd → Weird.

Sample Input 1
24

Sample Output 1
Not Weird

Explanation 1

N = 24 → even and greater than 20 → Not Weird.

"""
