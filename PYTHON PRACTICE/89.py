"""
ELECTIONS IN CHEFLAND difficulty rating:1034
There are 101 citizens in Chefland. It is election time in Chefland and 3 parties, A,B, and C are contesting the elections. Party A receives XA votes, party 
B receives 
XB votes, and party C receives XC votes.
The constitution of Chefland requires a particular party to receive a clear majority to form the government. A party is said to have a clear majority if it receives strictly greater than 50 votes.
If any party has a clear majority, print the winning party (A, B or C). Otherwise, print NOTA.
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains 3 space-separated integers — XA,XB, and XC.
Output Format
For each test case, if any party has a clear majority, print the winning party (A, B or C). Otherwise, print NOTA.
You can print each letter of the string in any case (upper or lower) (for instance, strings Nota, nOtA and notA will be considered identical).
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    if(a>50):
        print("A")
    elif(b>50):
        print("B")
    elif(c>50):
        print("C")
    else:
        print("NOTA")
