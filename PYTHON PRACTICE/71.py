"""
CHEF AND DIGITS OF A NUMBER difficulty rating:1209
Chef has a number D containing only digits 0's and 1's. He wants to make the number to have all the digits same. For that, he will change exactly one digit, i.e. from 0 to 1 or from 1 to 0. If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "Yes", else print "No" (quotes for clarity)
Input
The first line will contain an integer T representing the number of test cases.
Each test case contain a number made of only digits 1's and 0's on newline
Output
Print T lines with a "Yes" or a "No", depending on whether its possible to make it all 0s or 1s or not. 
"""
t=int(input())
while(t>0):
    t=t-1
    a=input()
    if(a.count("0")==1 or a.count("1")==1):
        print("Yes")
    else:
        print("No")
