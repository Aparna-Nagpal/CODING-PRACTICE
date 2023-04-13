"""
GRANDMA RECIPES difficulty rating:1337
Chef has learned a new technique for comparing two recipes. A recipe contains a list of ingredients in increasing order of the times they will be processed. An ingredient is represented by a letter 'a'-'z'. The i-th letter in a recipe denotes the i-th ingredient. An ingredient can be used multiple times in a recipe.
The technique is as follows. Compare two recipes by comparing their respective lists. If the sets of ingredients used in both recipes are equal and each ingredient is used the same number of times in both of them (processing order does not matter), they are declared as granama recipes. ("granama" is the Chef-ian word for "similar".)
Chef took two recipes he invented yesterday. He wanted to compare them using the technique. Unfortunately, Chef forgot to keep track of the number of times each ingredient has been used in a recipe. He only compared the ingredients but NOT their frequencies. More precisely, Chef considers two recipes as granama if there are no ingredients which are used in one recipe and not used in the other recipe.
Your task is to report whether Chef has correctly classified the two recipes (as granama or not granama) although he forgot to keep track of the frequencies.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description for T test cases follows. Each test case consists of a single line containing two space-separated strings R and S denoting the two recipes.
Output
For each test case, output a single line containing "YES" (quotes for clarity) if Chef correctly classified the two recipes as granama or not granama. Otherwise, output a single line containing "NO" (quotes for clarity) if Chef declared two recipes as granama when they actually are not.
"""
t=int(input())
while(t>0):
    t=t-1
    a,b=map(str,input().split())
    if(set(a)!=set(b)):
        f=1
    else:
        for i in set(a):
            if(a.count(i)!=b.count(i)):
                f=0
                break
        else:
            f=1
    if(f==1):
        print("YES")
    else:
        print("NO")