"""
BEAR AND CANDIES 123 difficulty rating:1028
Bears love candies and games involving eating them. Limak and Bob play the following game. Limak eats 1 candy, then Bob eats 2 candies, then Limak eats 3 candies, then Bob eats 4 candies, and so on. Once someone can't eat what he is supposed to eat, he loses.
Limak can eat at most A candies in total (otherwise he would become sick), while Bob can eat at most B candies in total. Who will win the game? Print "Limak" or "Bob" accordingly.
Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The only line of each test case contains two integers A and B denoting the maximum possible number of candies Limak can eat and the maximum possible number of candies Bob can eat respectively.
Output
For each test case, output a single line containing one string — the name of the winner ("Limak" or "Bob" without the quotes).
"""
t=int(input())
while(t>0):
    t=t-1
    z=0
    l,b=map(int,input().split())
    for i in range(1000):
        z=i+1
        if(i%2==0):
            l=l-z
            if(l<0):
                g=0
                break
        else:
            b=b-z
            if(b<0):
                g=1
                break
    if(g==0):
        print("Bob")
    else:
        print("Limak")
