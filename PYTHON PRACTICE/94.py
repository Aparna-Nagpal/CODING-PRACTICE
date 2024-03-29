"""
FROM HEAVEN TO EARTH 1066
Chef has been working in a restaurant which has N floors. He wants to minimise the time it takes him to go from the N-th floor to ground floor. He can either take the elevator or the stairs.
The stairs are at an angle of 45 degrees and Chef's velocity is V1 m/s when taking the stairs down. The elevator on the other hand moves with a velocity V2 m/s. Whenever an elevator is called, it always starts from ground floor and goes to N-th floor where it collects Chef (collecting takes no time), and makes its way down to the ground floor with Chef in it.
The elevator covers a total distance equal to N meters when going from N-th floor to ground floor or vice versa, while the length of the stairs is N2 because the stairs is at angle 45 degrees.
Chef has enlisted your help to decide whether he should use stairs or the elevator to minimise his travel time. Can you help him out?
Input
The first line contains a single integer T, the number of test cases.
Each test case is described by a single line containing three space-separated integers N,V1,V2.
Output
For each test case, output a single line with string Elevator or Stairs, denoting the answer to the problem.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    d=2**0.5
    if(a*d/b<2*a/c):
        print("Stairs")
    else:
        print("Elevator")
