"""
THE TWO DISHES difficulty rating:1254
Chef prepared two dishes yesterday. Chef had assigned the tastiness 
T1 and T2 to the first and to the second dish respectively. The tastiness of the dishes can be any integer between 0 and N (both inclusive).
Unfortunately, Chef has forgotten the values of T1 and T2 that he had assigned to the dishes. However, he remembers the sum of the tastiness of both the dishes - denoted by S.
Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes. Can you help the Chef in finding the maximum absolute difference?
It is guaranteed that at least one pair {T1,T2} exist such that 2≤T1+T2=S,0≤T1,T2≤N.
Input Format
The first line of input contains a single integer T, denoting the number of testcases. The description of the T testcases follows.
The first and only line of each test case contains two space-separated integers N,S, denoting the maximum tastiness and the sum of tastiness of the two dishes, respectively.
Output Format
For each testcase, output a single line containing the maximum absolute difference between the tastiness of the two dishes.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    t1=min(a,b)
    t2=b-t1
    g=t1-t2
    if(g>0):
        print(g)
    else:
        print(-1*g)
