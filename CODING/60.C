/*
CHEF AND COOK OFF difficulty rating:961
Chef has obtained the results of a past Cook-Off. He wants to estimate the skill level of each contestant. The contestants can be classified with high probability (w.h.p.) based on the number of solved problems:
A contestant that solved exactly 0 problems is a beginner.
A contestant that solved exactly 1 problem is a junior developer.
A contestant that solved exactly 2 problems is a middle developer.
A contestant that solved exactly 3 problems is a senior developer.
A contestant that solved exactly 4 problems is a hacker.
A contestant that solved all five problems is Jeff Dean.
Please help Chef to identify the programming level of each participant.
Input
The first line of the input contains a single integer N denoting the number of competitors.
N lines follow. The i-th of these lines contains five space-separated integers Ai, 1, Ai, 2, Ai, 3, Ai, 4, Ai, 5. The j-th of these integers (1 ≤ j ≤ 5) is 1 if the i-th contestant solved the j-th problem and 0 otherwise.
Output
For each participant, print a single line containing one string denoting Chef's classification of that contestant — one of the strings "Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean" (without quotes).
*/
#include <stdio.h>

int main(void) {
	int t,i,l;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    l=0;
	    int a[5];
	    for(i=0;i<5;i++)
	    scanf("%d",&a[i]);
	    for(i=0;i<5;i++)
	    if(a[i]>0)
	    l++;
	    if(l==0)
	    printf("Beginner\n");
	    else if(l==1)
	    printf("Junior Developer\n");
	    else if(l==2)
	    printf("Middle Developer\n");
	    else if(l==3)
	    printf("Senior Developer\n");
	    else if(l==4)
	    printf("Hacker\n");
	    else if(l==5)
	    printf("Jeff Dean\n");
	}
	return 0;
}

