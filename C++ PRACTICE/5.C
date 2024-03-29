/*
AVOID CONTACT difficulty rating:905
A hostel has N rooms in a straight line. It has to accommodate X people. Unfortunately, out of these X people, Y of them are infected with chickenpox. Due to safety norms, the following precaution must be taken:
No person should occupy a room directly adjacent to a room occupied by a chickenpox-infected person. In particular, two chickenpox-infected people cannot occupy adjacent rooms.
For example, if room 4 has a chickenpox-infected person, then nobody should occupy rooms 3 and 5. Similarly, if room 1 has a chickenpox-infected person then nobody should occupy room 2.
What's the minimum value of N for which all the people can be accommodated in the hostel, following the above condition?
Input Format
The first line of input contains a single integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two integers X and Y — the total number of people and the number of chickenpox-infected people.
Output Format
For each test case, output on a new line a single integer — the minimum value of N for which all the people can be accommodated in the hostel.
*/
#include <iostream>
using namespace std;

int main() {
	int t,h,a,b;
	cin>>t;
	while(t>0)
	{
	    t--;
	    cin>>a>>b;
	    if(a-b==0)
	    h=b*2-1;
	    else
	    h=b*2+a-b;
	    cout<<h<<endl;
	}
	
	return 0;
}
