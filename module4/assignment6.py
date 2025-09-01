#%%
import random
point =int(input())
square_list = 0
circle_list =0
i =1
for i in range(0, point*1000):
    point_x =random.uniform (-1,-1)
    point_y=random.uniform(-1,-1)
    square_list +=1
    if (point_x**2)+(point_y**2) <=1:
        circle_list +=1
result =(circle_list/square_list)*4
print("your solution correctly calculates an approximation of pi",result)