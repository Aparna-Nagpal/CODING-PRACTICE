"""
MINIMUM ATTENDENCE REQUIREMENT difficulty rating:1053
A semester in Chef's University has 120 working days. The University's requirement is that a student should be present for at least 75% of the working days in the semester. If not, the student is failed.
Chef has been taking a lot of holidays, and is now concerned whether he can pass the attendance requirement or not. N working days have already passed, and you are given N bits - B1,B2,..., BN. 
Bi=0 denotes that Chef was absent on the ℎith day, and Bi=1 denotes that Chef was present on that day.
Can Chef hope to pass the requirement by the end of the semester?
Input:
First line will contain T, the number of testcases. Then the testcases follow.
Each testcase contains two lines of input.
The first line of each testcase contains a single integer, N, the number of days till now.
The second line of each testcase contains a string B of length N where Bi represents the status of the ℎith day.
Output:
For each testcase, output the answer in a single line - "YES" if Chef can pass the attendance requirement and "NO" if not.
"""
t=int(input())
while(t>0):
    t=t-1
    a=int(input())
    b=input()
    c=b.count('0')
    d=120-c
    e=d/120*100
    if(e>=75):
        print("YES")
    else:
        print("NO")
