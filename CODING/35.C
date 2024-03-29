/*
PROBLEM CATEGORY difficulty rating:860
Chef prepared a problem. The admin has rated this problem for x points.
A problem is called :
Easy if 1≤x<100
Medium if 100≤x<200
Hard if 200≤x≤300
Find the category to which Chef’s problem belongs.
Input Format
The first line contains T denoting the number of test cases. Then the test cases follow.
The first and only line of each test case contains a single integer x.
Output Format
For each test case, output in a single line the category of Chef's problem, i.e whether it is an Easy, Medium or Hard problem. The output is case sensitive.
*/

#include <stdio.h>

int main(void) {
	int t,a;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    scanf("%d",&a);
	    if(a>=1&&a<100)
	    printf("Easy\n");
	    else if(a>=100&&a<200)
	    printf("Medium\n");
	    else if(a>=200&&a<=300)
	    printf("Hard\n");
	}
	return 0;
}

