"""
CHEF AND VACATION TRANSPORTATION difficulty rating:855
Vacations have arrived and Chef wants to go to his home in ChefLand. There are two types of routes he can take:
•	Take a flight from his college to ChefArina which takes �X minutes and then take a bus from ChefArina to ChefLand which takes �Y minutes.
•	Take a direct train from his college to ChefLand which takes �Z minutes.
Which of these two options is faster?
Input Format
•	The first line of the input contains a single integer �T - the number of test cases. The test cases then follow.
•	The first line of the test case contains three space-separated integers �X, �Y, and �Z.
Output Format
For each test case, if Chef takes the train output TRAIN, if Chef takes the plane and the bus output PLANEBUS, if both are equal output EQUAL.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    if(a+b<c):
        print("PLANEBUS")
    elif(a+b==c):
        print("EQUAL")
    else:
        print("TRAIN")

