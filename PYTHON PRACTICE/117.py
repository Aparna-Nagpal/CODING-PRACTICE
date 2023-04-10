"""
VACCINE DISTRIBUTION difficulty rating:1219
Finally, a COVID vaccine is out on the market and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible. There are a total of N people with ages a1,a2,…,aN.
There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day. Anyone whose age is ≥80≥80 or ≤9≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.
Input
•	The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
•	The first line of each test case contains two space-separated integers N and D.
•	The second line contains N space-separated integers a1,a2,…,aN.
Output
For each test case, print a single line containing one integer ― the smallest required number of days.
"""
t=int(input())
while(t>0):
    t=t-1
    h=0
    r=0
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        if(i<=9 or i>=80):
            r=r+1
        else:
            h=h+1
    if(r%d!=0):
        r=r//d+1
    else:
        r=r//d
    if(h%d==0):
        h=h//d
    else:
        h=h//d+1
    print(r+h)
