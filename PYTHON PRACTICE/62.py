"""
CAR RANGE difficulty rating:938
The fuel economy of a car is the distance which it can travel on one litre of fuel.
The base fuel economy (i.e, its fuel economy when there is only one person - the driver - in the car) of a certain car is M kilometres per litre. It was also observed that every extra passenger in the car decreases the fuel economy by 1 kilometre per litre.P people want to take this car for a journey. They know that the car currently has V litres of fuel in its tank.
What is the maximum distance this car can travel under the given conditions, assuming that all P people always stay in the car and no refuelling can be done?
Note that among the P people is also a driver, i.e, there are exactly P people in the car.
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
Each test case consists of a single line of input, containing three space-separated integers P,M, and V - the number of people, base fuel economy, and amount of fuel present in the car, respectively.
Output Format
For each test case, output a single line containing one integer - the maximum distance that the car can travel.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    f=b-a+1
    print(f*c)
