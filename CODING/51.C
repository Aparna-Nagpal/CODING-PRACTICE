/*
SELF DEFENCE TRAINING difficulty rating:716
After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.
The only condition for a woman to be eligible for the special training is that she must be between 10 and 60 years of age, inclusive of both 10 and 60.
Given the ages of N women in his village, please help San Te find out how many of them are eligible for the special training.
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N, the number of women.
The second line of each test case contains N space-separated integers A1,A2,...,AN,the ages of the women.
Output Format
For each test case, output in a single line the number of women eligible for self-defence training.
*/
#include <stdio.h>

int main(void) {
	int t,l,i,a;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    l=0;
	    scanf("%d",&a);
	    int k[a];
	    for(i=0;i<a;i++)
	    scanf("%d",&k[i]);
	    for(i=0;i<a;i++)
	    {
	        if(k[i]>=10&&k[i]<=60)
	        l++;
	    }
	    printf("%d\n",l);
	}
	return 0;
}

