"""
SOLUBILITY difficulty rating:922
Suppose for a unit rise in temperature, the solubility of sugar in water increases by Bg/100 mL.
Chef does an experiment to check how much sugar (in g) he can dissolve given that he initially has 1 liter of water at X degrees and the solubility of sugar at this temperature is Ag/100 mL. Also, Chef doesn't want to lose any water so he can increase the temperature to at most 100 degrees.
Assuming no loss of water takes place during the process, find the maximum amount of sugar (in g) can be dissolved in 1 liter of water under the given conditions.
Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains three integers X,A,B.
Output
For each testcase, output in a single line the answer to the problem.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b,c=map(int,input().split())
    d=b+(100-a)*c
    print(d*10)
