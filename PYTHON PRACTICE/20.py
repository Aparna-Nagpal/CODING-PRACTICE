"""
CYCLIC QUADRILATERAL difficulty rating: 735
You are given the sizes of angles of a simple quadrilateral (in degrees) A,B,C and D, in some order along its perimeter. Determine whether the quadrilateral is cyclic.
Note: A quadrilateral is cyclic if and only if the sum of opposite angles is 180∘.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers A, B, C and D.
Output
Print a single line containing the string "YES" if the given quadrilateral is cyclic or "NO" if it is not (without quotes).
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c,d=map(int,input().split())
    if(a+c==b+d==180):
        print("YES")
    else:
        print("no")
    
