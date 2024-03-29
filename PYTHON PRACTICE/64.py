"""
CHEF AND INTERACTIVE CONTESTS difficulty rating:951
Every beginning has an end... and an editorial.
What the hell are all these interactive problems? What does flushing output mean? So many questions... Chef explains it in an easy way: you must communicate with a grader program, which accepts your input only if you flushed the output.
There is a contest with interactive problems where N people participate. Each contestant has a known rating. Chef wants to know which contestants will not forget to flush the output in interactive problems. Fortunately, he knows that contestants with rating at least r never forget to flush their output and contestants with rating smaller than r always forget to do it. Help Chef!
Input
The first line of the input contains two space-separated integers N and r.
Each of the following N lines contains a single integer R denoting the rating of one contestant.
Output
For each contestant, print a single line containing the string "Good boi" if this contestant does not forget to flush the output or "Bad boi" otherwise.
"""
t,a=map(int,input().split())
while(t>0):
    t=t-1
    b=int(input())
    if(b<a):
        print("Bad boi")
    else:
        print("Good boi")
