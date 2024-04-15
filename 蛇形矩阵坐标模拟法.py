n = int(input())
matrix = [[0 for i in range(n)] for i in range(n)] #初始化矩阵
x_vector , y_vector = [1,0,-1,0] , [0,1,0,-1] 
# x,y方向的前进分量，顺序为下右上左
# 注意：为符合编程习惯，x在实际中是竖直方向，y在实际中是水平方向
x,y,d = 0,0,0 # 初始化坐标
for k in range(1,n**2+1):
    matrix[x][y] = k    # 填入
    temp_x , temp_y = x+x_vector[d] , y+y_vector[d] # 暂时更新坐标
    #遇到边界，转向
    if temp_x == -1 or temp_x == n or temp_y == -1 or temp_y == n or matrix[temp_x][temp_y] != 0:
        d = (d + 1) % 4 #新的方向
        temp_x,temp_y = x+x_vector[d] , y+y_vector[d]#遇到边界时重新更新坐标
    x,y = temp_x,temp_y

for i in range(n): # 输出
    for j in range(n):
        print('{0:<2d}'.format(matrix[i][j]), end = ' ')
    print() 
