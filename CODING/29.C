/*
NETFLIX
Problem
Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two users to share a subscription.
Given that Alice, Bob, and Charlie have A,B, and C rupees respectively and a Netflix subscription costs X rupees, find whether any two of them can contribute to buy a subscription.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case contains four space-separated integers A,B,C, and X — the amount that Alice, Bob, and Charlie have, and the cost of a Netflix subscription respectively.
Output Format
For each test case, output YES, if any two of Alice, Bob, and Charlie can contribute to buy a Netflix subscription or NO otherwise.
You may print each character in uppercase or lowercase. For example, NO, no, No, and nO are all considered identical.
*/

#include <stdio.h>

int main(void) {
    int t,a,b,c,d;
    scanf("%d",&t);
    while(t>0)
    {
        t--;
        scanf("%d%d%d%d",&a,&b,&c,&d);
        if(a+b>=d||b+c>=d||c+a>=d)
        printf("yes\n");
        else
        printf("no\n");
    }
    


	return 0;
}

