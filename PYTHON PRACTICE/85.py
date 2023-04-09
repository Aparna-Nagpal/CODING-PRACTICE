"""
SNAKE PROCESSION difficulty rating:1014
The annual snake festival is upon us, and all the snakes of the kingdom have gathered to participate in the procession. Chef has been tasked with reporting on the procession, and for this he decides to first keep track of all the snakes. When he sees a snake first, it'll be its Head, and hence he will mark a 'H'. The snakes are long, and when he sees the snake finally slither away, he'll mark a 'T' to denote its tail. In the time in between, when the snake is moving past him, or the time between one snake and the next snake, he marks with '.'s.
Because the snakes come in a procession, and one by one, a valid report would be something like "..H..T...HTH....T.", or "...", or "HT", whereas "T...H..H.T", "H..T..H", "H..H..T..T" would be invalid reports (See explanations at the bottom).
Formally, a snake is represented by a 'H' followed by some (possibly zero) '.'s, and then a 'T'. A valid report is one such that it begins with a (possibly zero length) string of '.'s, and then some (possibly zero) snakes between which there can be some '.'s, and then finally ends with some (possibly zero) '.'s.
Chef had binged on the festival food and had been very drowsy. So his report might be invalid. You need to help him find out if his report is valid or not.
Input
The first line contains a single integer, R, which denotes the number of reports to be checked. The description of each report follows after this.
The first line of each report contains a single integer, L, the length of that report.
The second line of each report contains a string of length L. The string contains only the characters '.', 'H', and 'T'.
Output
For each report, output the string Valid or Invalid in a new line, depending on whether it was a valid report or not.
"""
t=int(input())
while(t>0):
    t=t-1
    f=0
    a=int(input())
    b=input()
    for i in range(a):
        if(b[i]=='H'):
            f=f+1
            if(f>1):
                break
        elif(b[i]=='T'):
            f=f-1
            if(f<0):
                break
    if(f==0):
        print("Valid")
    else:
        print("Invalid")