"""
MINIMUM NUMBER OF PIZZAS difficulty rating:1532
Chef is throwing a party for his N friends. There is a pizza store nearby and he wants to buy pizza for his friends. Each pizza has exactly K slices. Chef's friends get sad if one gets more slices than the other. Also, Chef gets sad if there are some pizza slices left. More formally, suppose Chef buys P pizzas, then everyone is happy if and only if there is a way to distribute K⋅P slices between N friends.
You need to find the minimum number of pizzas Chef has to buy to share all the slices among his friends so that none of his friends gets sad. Note that Chef hates pizza and doesn't take any slices.
Input Format
First line of input contains T, the number of test cases. Then the test cases follow.
Each test case contains two space-separated integers N and K, where N is the number of friends of chef and K is the number of slices in a pizza.
Output Format
For each test case, print the minimum number of pizzas chef has to buy to share among his friends so that none of his friends gets sad.
"""
import math
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    c=math.gcd(a,b)
    print(a//c)
