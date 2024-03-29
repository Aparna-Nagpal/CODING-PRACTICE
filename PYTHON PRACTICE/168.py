"""
Bob and Alice are having a lockout match between them. There are three problems in the contest worth A,B, and C points respectively. Only the first player to solve a problem gets points for that problem. It is impossible for Bob and Alice to solve a problem at the same time. Chef wants to know if there is any chance of a draw if Bob and Alice manage to solve all 3 problems. A draw occurs when both players end with equal number of points.
Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three space separated integers A, B, and C.
Output Format
For each testcase, output YES if the match can end in a draw, and NO otherwise.
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    if(a+b==c or c+b==a or a+c==b):
        print("YES")
    else:
        print("NO")
