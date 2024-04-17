'''本题要求显示给定整数M和N区间内素数并对它们求和。

输入格式:
在一行输入两个正整数M和N（1≤M≤N≤1000）。

输出格式:
显示指定范围的素数，素数间空一格，每五个换一行。
单独一行输出素数的个数及素数的和。

输入样例:
在这里给出一组输入。例如：
4 30

输出样例:
在这里给出相应的输出。例如：
5 7 11 13 17 
19 23 29 
amount=8 sum=124'''

def IsPrime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        flag = True
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                flag = False
                break
        return flag

a,b = map(int,input().split())
ans = []
for i in range(a,b):
    if IsPrime(int(i)):
        ans.append(int(i))
s = 0
for i in ans:
    print(i, end = " ")
    s += 1
    if s == 5:
        print()
        s = 0
if s < 5 and len(ans)>0:
    print()
print('amount={0:d} sum={1:d}'.format(len(ans),sum(ans)))