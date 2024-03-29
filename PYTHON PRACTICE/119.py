"""
SLEEPY CHEF difficulty rating:1445
Chef has to work on a project for the next N hours. He is given a work plan to do this, which is given to you as a binary string S of length N. Si=1 if Chef has to work on the project during the i-th hour, and Si=0 if Chef is free during the i-th hour.
Chef would like to use some of his free time to take naps. He needs a minimum of K consecutive hours of free time to take a nap. What is the maximum number of naps that Chef can take during the next N hours?
Note that it is allowed for one nap to immediately follow another, i.e, Chef can wake up from one nap and then immediately take another one (if he has enough free time to do so), and these will be counted as different naps.
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K respectively.
The second line of each test case contains a binary string S of length N denoting Chef's work plan.
Output Format
For each test case, print a single line containing one integer — the maximum number of naps that Chef can take.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    s=input()
    n=s.count('0'*b)
    print(n)
