/*
CRICKET RANKING:966
In a season, each player has three statistics: runs, wickets, and catches. Given the season stats of two players A and B, denoted by R, W, and C respectively, the person who is better than the other in the most statistics is regarded as the better overall player. Tell who is better amongst A and B. It is known that in each statistic, the players have different values.
Input Format
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains two lines of input.
The first line contains three integers R1,W1,C1, the stats for player A.
The second line contains three integers R2,W2,C2,the stats for playerB.
Output Format
For each test case, output in a single line "A" (without quotes) if player A is better than player B and "B" (without quotes) otherwise.
*/
#include <stdio.h>

int main(void) {
	int t,i,l,g;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    l=0;
	    g=0;
	    int a[3],b[3];
	    for(i=0;i<3;i++)
	    scanf("%d",&a[i]);
	    for(i=0;i<3;i++)
	    scanf("%d",&b[i]);
	    for(i=0;i<3;i++)
	    {
	        if(a[i]>b[i])
	        l++;
	        else
	        g++;
	    }
	    if(l>g)
	    printf("A\n");
	    else
	    printf("B\n");
	    
	    
	}
		return 0;
}

