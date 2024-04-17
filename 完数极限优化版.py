import math #引入math模块比直接算开根更快
a,b = map(int,input().split())
ans = []
for i in range(a,b+1):
    factor = [1]
    if i % 2 == 0:  #观察发现，所有完数都是偶数，可以减少一半的工作量
        for j in range(2,int(math.sqrt(i))+1):#因子都是成对出现的
            if i % j == 0:                   #例如28 = 2 x 14
                factor.append(j)#其中一个因子小于根号28，一个因子大于根号28
                if j**2 != i: #如果遇到4=2x2这种情况，可以防止加进去两个相同因子
                    factor.append(i//j)#加入另一个因子
    if sum(factor) == i:
        ans.append(i) #按要求输出
        factor.sort()
        print(str(i)+' = '+" + ".join(map(str,factor)))
if len(ans)==0:
    print('None')