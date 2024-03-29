/*
CHEFLAND VISA difficulty rating:857
Ash is trying to get visa to Chefland. For the visa to be approved, he needs to satisfy the following three criteria:

Solve at least x1 problems on Codechef.
Have at least y1 current rating on Codechef.
Make his last submission at most z1 months ago.
You are given the number of problems solved by Chef (x2), his current rating (y2) and the information that he made his last submission z2 months ago. Determine whether he will get the visa.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains six space-separated integers x1,x2,y1,y2,z1 and z2.
Output
For each test case, print a single line containing the string "YES" if Chef will get the visa or "NO" if he will not.
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
*/

#include <stdio.h>

int main(void) {
	int t,a,b,m,l,c,k;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    scanf("%d%d%d%d%d%d",&a,&m,&b,&l,&c,&k);
	    if((m>=a)&&(l>=b)&&(k<=c))
	    printf("yes\n");
	    else
	    printf("no\n");
	}
	return 0;
}

