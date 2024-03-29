/*
A-SAVE WATER SAVE LIFE difficulty rating:918
To address the situation of Water Scarcity in Chefland, Chef has started an awareness campaign to motivate people to use greywater for toilets, washing cars, gardening, and many other chores which don't require the use of freshwater. These activities presently consume y liters of water every week per household and Chef thinks through this campaign he can help cut down the total usage to 
⌊y/2 ⌋.

Assuming x liters of water every week per household is consumed at chores where using freshwater is mandatory and a total of C liters of water is available for the entire Chefland having H households for a week, find whether all the households can now have sufficient water to meet their requirements.

Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, four integers H,x,y,C.
Output Format
Print a single line containing the string "YES" if it is possible to meet the requirement of all the households in Chefland or "NO" if it is impossible (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
*/
#include <iostream>
using namespace std;

int main() {
    int t,h,x,y,c;
    cin>>t;
    while(t>0)
    {
        t--;
        cin>>h>>x>>y>>c;
        if((x+y/2)*h<=c)
        cout<<"yes"<<endl;
        else
        cout<<"no"<<endl;
        
    }
	
	return 0;
}
