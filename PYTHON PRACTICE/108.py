"""
GAME BETWEEN FRIENDS difficulty rating:991
Nitin and Sobhagya were playing a game with coins. If Sobhagya has more coins then he is winning, otherwise Nitin is winning. Note that this means if both Nitin and Sobhagya have the same number of coins, then Nitin is winning.
Initially Nitin has A coins while Sobhagya has B coins. Then Ritik came and gave his C coins to the player who is not winning currently, after which Satyarth came and repeated the same process (gave his D coins to the player who is not winning currently).
Find the final winner of the game.
Input Format
•	The first line of the input contains an integer T - the number of test cases. The test cases then follow.
•	The only line of each test case contains four space-separated integers A, B, C, and D.
Output Format
For each test case, output on a single line N if Nitin is the final winner of the game, or S if Sobhagya is the final winner of the game.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c,d=map(int,input().split())
    if(b>a):
        a=a+c
    else:
        b=b+c
    if(b>a):
        a=a+d
    else:
        b=b+d
    if(b>a):
        print("S")
    else:
        print("N")
