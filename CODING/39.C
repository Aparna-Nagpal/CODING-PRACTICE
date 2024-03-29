/*
CHEF ON VACATION difficulty rating:891
After a very long time, the Chef has a vacation. Chef has planned for two trips during this vacation - one with his family and the other with his friends. The family trip will take X days and the trip with friends will take Y days. Currently, the dates are not decided but the vacation will last only for Z days.
Chef can be in at most one trip at any time and once a trip is started, Chef must complete it before the vacation ends. Will Chef be able to go on both these trips if he chooses the dates optimally?
Input Format
The first line will contain a single integer T denoting the number of test cases. The description of the test cases follows.
Each test case consists of a single line of input, which contains three space-separated integers X,Y and Z.
Output Format
For each test case, output in a single line the answer: "YES" if Chef can go on both the trips and "NO" if not.
You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
*/
#include <stdio.h>

int main(void) {
	int t,a,b,c;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    scanf("%d%d%d",&a,&b,&c);
	    if((a+b)<=c)
	    printf("yes\n");
	    else
	    printf("no\n");
	}
	return 0;
}
