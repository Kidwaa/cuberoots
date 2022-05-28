import numpy as np
import math




def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums


def get_cube_root(x):
    cube_num=x
    cube_Pow = 1/3
    cube_Root = cube_num**cube_Pow

    floor=math.floor(cube_Root)

    if floor**3==cube_num:
        return(floor)

    elif (floor+1)**3==cube_num:
        return (floor+1)

    else:
        return(cube_Root)


lon=[]
for x in range(1,100000000):
    lon.append(x)

sp_numbers=[]

for n in lon:
    if get_cube_root(n)==sum(get_pos_nums(n)):
        sp_numbers.append(n)

print(sp_numbers)
