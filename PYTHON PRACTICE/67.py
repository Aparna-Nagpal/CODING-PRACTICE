"""
COLD PLAY difficulty rating:854
Chef is a big fan of Coldplay. Every Sunday, he will drive to a park taking �M minutes to reach there, and during the ride he will play a single song on a loop. Today, he has got the latest song which is in total �S minutes long. He is interested to know how many times will he be able to play the song completely.
Input Format
•	The first line contains an integer �T - the number of test cases. Then the test cases follow.
•	The only line of each test case contains two space-separated integers �,�M,S - the duration of the trip and the duration of the song, both in minutes.
Output Format
For each test case, output in a single line the answer to the problem.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    print(a//b)
