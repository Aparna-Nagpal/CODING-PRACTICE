/*
PASSING MARKS difficulty rating:904
Recently, Chef's College Examination has concluded. He was enrolled in 3 courses and he scored A,B,C in them, respectively. To pass the semester, he must score at least Amin,Bmin,Cmin marks in the respective subjects along with a cumulative score of at least Tmin ,i.e, A+B+C≥Tmin.
Given seven integers Amin,Bmin,Cmin,Tmin,A,B,C, tell whether Chef passes the semester or not.
Input:
The first line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, seven integers Amin,Bmin,Cmin,Tmin,A,B,C each separated by aspace.
Output: Output in a single line, the answer, which should be "YES" if Chef passes the semester and "NO" if not.
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
*/
#include <iostream>
using namespace std;

int main() {
    int t,a,b,c,a1,b1,c1,t1;
    cin>>t;
    while(t>0)
    {
        t--;
        cin>>a>>b>>c>>t1>>a1>>b1>>c1;
        if(a1+b1+c1>=t1)
        {
            if(a<=a1&&b<=b1&&c<=c1)
            cout<<"yes";
            else
            cout<<"no";
        }
        else
        cout<<"no";
        cout<<endl;
    }
	
	return 0;
}
