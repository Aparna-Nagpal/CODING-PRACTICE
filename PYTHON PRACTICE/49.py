"""
AIRLINE RESTRICTIONS difficulty rating:1042
Chef has 3 bags that she wants to take on a flight. They weigh A, B, and C kgs respectively. She wants to check-in exactly two of these bags and carry the remaining one bag with her.
The airline restrictions says that the total sum of the weights of the bags that are checked-in cannot exceed D kgs and the weight of the bag which is carried cannot exceed E kgs. Find if Chef can take all the three bags on the flight.
Input Format
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
Each testcase contains a single line of input, five space separated integers A,B,C,D,E.
Output Format
For each testcase, output in a single line answer "YES" if Chef can take all the three bags with her or "NO" if she cannot.
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
"""
t=int(input())
while(t>0):
    t=t-1
    f=0
    l=0
    a,b,c,d,e=map(int,input().split())
    if(a+b<=d and c<=e):
        print("YES")
    elif(b+c<=d and a<=e):
        print("YES")
    elif(a+c<=d and b<=e):
        print("YES")
    else:
        print("NO")
