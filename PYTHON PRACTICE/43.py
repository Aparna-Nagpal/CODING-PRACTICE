"""
CHECK ALGORITHM difficulty rating:1273
One day, Saeed was teaching a string compression algorithm. This algorithm finds all maximal substrings which contains only one character repeated one or more times (a substring is maximal if it we cannot add one character to its left or right without breaking this property) and replaces each such substring by the string "cK", where K is the length of the substring and c is the only character it contains. For example, "aabaaa" is compressed to "a2b1a3".
Saeed wanted to check if the students understood the algorithm, so he wrote a string S on the board and asked the students if the algorithm is effective on S, i.e. if the string created by compressing S is strictly shorter than S. Help them answer this question.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single string S.
Output
For each test case, print a single line containing the string "YES" if the algorithm is effective on S or "NO" if it is not.
"""
t=int(input())
while(t>0):
    t=t-1
    s=input()
    g=s[0]
    r=''
    h=0
    j=0
    k=0
    for i in s:
        if(g==i):
            h=h+1
        else:
            r=r+g+str(h)
            g=i
            h=1
    r=r+g+str(h)
    if(len(r)<len(s)):
        print("YES")
    else:
        print("NO")
