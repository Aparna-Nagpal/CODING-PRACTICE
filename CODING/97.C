/*
ENOUGH SPACE
Chef's computer has N GB of free space. He wants to save X files, each of size 1 GB and Y files, each of size 2 GB on his computer. Will he be able to do so?
Chef can save all the files on his computer only if the total size of the files is less than or equal to the space available on his computer.
Input Format
The first line contains an integer T, denoting the number of test cases. The T test cases then follow:
The first and only line of each test case contains three integers N,X,Y, denoting the free-space in computer, the number of 1 and 2 GB files respectively.
Output Format
For each test case, print YES if Chef is able to save the files and NO otherwise.
You may print each character of the string in uppercase or lowercase (for example, the strings yEs, yes, Yes and YES will all be treated as identical).
*/
#include <stdio.h>

int main(void) {
	int t,n,a,b;
	scanf("%d",&t);
	while(t>0)
	{
	    t--;
	    scanf("%d%d%d",&n,&a,&b);
	    if(a+b*2<=n)
	    printf("yes\n");
	    else
	    printf("no\n");
	}
	return 0;
}

