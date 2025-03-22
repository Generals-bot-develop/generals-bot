import numpy as np

array = np.load('./result.npy')

i = array.shape[0]
j = array.shape[1]
k = array.shape[2]
color = 0

def judge(x, y, color):
    for ii in range(-1,2):
        for jj in range(-1,2):
            xx = x + ii
            yy = y + jj
            if xx < 0 or xx > i or yy < 0 or yy > j:
                continue
            if(array[xxx][xx][yy][1] == color):
                return True
    return False
    
for xxx in range(0,i):
    for x in range(0,j):
        for y in range(0,k):
            if judge(x,y,color):
                continue
            array[xxx][x][y][1] = -1
            array[xxx][x][y][2] = 0
            if array[xxx][x][y][0] == 1:
                array[xxx][x][y][0] = 0
                array[xxx][x][y][2] = np.inf
            if array[xxx][x][y][0] == 2:
                array[xxx][x][y][0] = 0
                array[xxx][x][y][2] = 0
np.save("./result-mask.npy", array)
