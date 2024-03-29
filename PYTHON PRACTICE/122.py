"""
BINARY STRING COST difficulty rating:1069
According to the new tax scheme, a new tax called the binary string tax was introduced! JJ has a binary string S of length N. According to the tax scheme, for every occurrence of 01 in , a tax of X rupees will be charged, while for every occurrence of 10 in S, a tax of Y rupees will be charged.
For example, if X=5, Y=7 and S=11010, then S has 1 occurrence of 01 and 2 occurrences of 10, so the tax charged =5⋅1+7⋅2=19
JJ can rearrange the string S in any way he wants. He wants to minimize the amount of tax he has to pay. Can you help him do so?
Input Format
The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains three integers N, X and Y - the length of the binary string S, the tax charged on an occurrence of 01 and the tax charged on an occurrence of 10.
The second line of each test case contains a binary string S of length N containing 0s and 1s only.
Output Format
For each test case, output the minimum amount of tax that JJ has to pay.
"""
t=int(input())
while(t>0):
    t=t-1
    n,x,y=map(int,input().split())
    s=input()
    a=s.count("01")
    b=s.count("10")
    if(a==0 and b==0):
        print("0")
    else:
        if(x>=y):
            print(y)
        else:
            print(x)
