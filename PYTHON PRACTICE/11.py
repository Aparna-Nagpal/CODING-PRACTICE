'''
BATH IN WINTERS difficulty rating:643
A geyser has a capacity of X litres of water and a bucket has a capacity of Y litres of water.
One person requires exactly 2 buckets of water to take a bath. Find the maximum number of people that can take bath using water from one completely filled geyser..
Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains a single line of input, two integers X,Y.
Output Format
For each test case, output the maximum number of people that can take bath.
  '''
  t=int(input())
while(t>0):
    t=t-1
    a,b=map(int,input().split())
    g=b*2
    print(a//g)
