#630510619 
#nuttawat khamwangsawat
#Lab02_3

import math

def fncal_all_area(n):
    area = n * n
    print(("%.2f")%area)
    circle_big = fncal_circle_area(n/4) * 4
    print(("%.2f")%circle_big)
    circle_small = fncal_circle_area((n/8)*((2**0.5)-1)) * 3
    print(("%.2f")%circle_small)
    total = area - circle_big - circle_small
    print(("%.2f")%total)

def fncal_circle_area(r):
    return(math.pi* r* r)
    
def main():
    n = int(input())
    fncal_all_area(n)

if __name__ == '__main__':
    main()