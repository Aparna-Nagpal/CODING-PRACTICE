"""
Sardar Singh has many men fighting for him, and he would like to calculate the power of each of them to better plan for his fight against Ramadhir.
The power of a string S of lowercase English alphabets is defined to be
i=1 ∑∣S∣i⋅ord(Si)
where ord(Si) is the position of Si in the alphabet, i.e,ord(′a′)=1,ord(′b′)=2,…,ord(′z′)=26.
Each of Sardar Singh's men has a name consisting of lowercase English alphabets. The power of a man is defined to be the maximum power over all possible rearrangements of this string.
Find the power of each of Sardar Singh's men.
Input Format
The first line of input contains an integer T, denoting the total number of Sardar Singh's men.
Each of the next T lines contains a single string Si, the name of Sardar Singh's i-th man.
Output Format
Output T lines, each containing a single integer. The i-th of these lines should have the power of the i-th of Sardar Singh's men.
"""
t=int(input())
while(t>0):
    t=t-1
    a=input()
    n=len(a)
    c=0
    s=0
    a=sorted(a)
    for i in a:
        c=c+1
        f=ord(i)-96
        s=s+f*c
    print(s)
