"""
HIRING TEST difficulty rating:1260
A company conducted a coding test to hire candidates. N candidates appeared for the test, and each of them faced M problems. Each problem was either unsolved by a candidate (denoted by 'U'), solved partially (denoted by 'P'), or solved completely (denoted by 'F').
To pass the test, each candidate needs to either solve X or more problems completely, or solve (X−1) problems completely, and Y or more problems partially.
Given the above specifications as input, print a line containing N integers. The ith integer should be 1 if the ith candidate has passed the test, else it should be 0.##Input:
The first line of the input contains an integer T, denoting the number of test cases.
The first line of each test case contains two space-separated integers, N and M, denoting the number of candidates who appeared for the test, and the number of problems in the test, respectively.
The second line of each test case contains two space-separated integers, X and Y, as described above, respectively.
The next N lines contain M characters each. The jth character of the ith line denotes the result of the ith candidate in the jth problem. 'F' denotes that the problem was solved completely, 'P' denotes partial solve, and 'U' denotes that the problem was not solved by the candidate.
###Output:
For each test case, print a single line containing N integers. The ith integer denotes the result of the ith candidate. 1 denotes that the candidate passed the test, while 0 denotes that he/she failed the test.
"""
t=int(input())
while(t>0):
    t=t-1
    l=[]
    s=[]
    k=''
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    for i in range(n):
        l.append(input())
    for i in l:
        if i.count('F')>=x or (i.count('F')==x-1 and i.count('P')>=y):
            s.append('1')
        else:
            s.append('0')
    for i in s:
        k=k+i
    print(k)
