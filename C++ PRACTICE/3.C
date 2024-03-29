/*
PEACEFUL PARTY difficulty rating:898
Problem
The mayor of your city has decided to throw a party to gather the favour of his people in different regions of the city.
There are 3 distinct regions in the city namely A, B, C comprising of PA,PB and PC number of people respectively.
However, the mayor knows that people of the region B are in conflict with people of regions A and C. So, there will be a conflict if people from region B are present at the party along with people from region A or C.
The mayor wants to invite as many people as possible and also avoid any conflicts. Help him invite maximum number of people to the party.
Input Format
The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains three integers PA,PB and PC-number of people living in regions A,B and C respectively.
Output Format
For each test case, output the maximum number of people that can be invited to the party.
*/
#include <iostream>
using namespace std;

int main() {
	int t,a,b,c;
	cin>>t;
	while(t>0)
	{
	    t--;
	    cin>>a>>b>>c;
	    if(a+c>=b)
	    cout<<a+c<<endl;
	    else
	    cout<<b<<endl;
	}
		return 0;
}
