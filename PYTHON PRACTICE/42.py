"""
CHEF AND HIS FRUIT SALAD difficulty rating:822
Chef has closed his restaurant and decided to run a fruit stand instead. His signature dish is a fruit chaat consisting of 2 bananas and 1 apple. He currently has X bananas and Y apples. How many chaats can he make with the fruits he currently has?
Input Format
The first line will contain T, the number of testcases. Then the testcases follow.
Each testcase consists of a single line containing two space separated integers - X and Y
Output Format
For each testcase, output the answer on a new line.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    a=a//2
    if(a>=b):
        print(b)
    else:
        print(a)
