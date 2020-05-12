# Uses python3
import sys


def optimal_points(seg):
    points=[]
    seg.sort()
    i=0
    while(i<len(seg)):
        l_l=seg[i][0]
        u_l=seg[i][1]
        lis=[]
        lis.append(u_l)
        if i+1<len(seg) and u_l!=l_l:
        
            while(seg[i+1][0]<=u_l and i+1<len(seg)):
                i+=1
                lis.append(seg[i][0])
                
                if (i+1)>=(len(seg)):
                    break
        i+=1
        # print(lis)
        points.append(lis[-1])
    return points
        

if __name__ == '__main__':
    n=int(input())
    seg=[]
    
    for i in range(n):
        seg.append(list(map(int,input().split(" "))))
    points = optimal_points(seg)
    
    print(len(points))
    for i in range(len(points)):
        print(points[i],end=" ")
