#630510619 
#nuttawat khamwangsawat
#Lab01_2

def fncal_shade_area(n):
    square = 3*(n**2) #square area
    r = n/4 #radius
    p = 3.141593 #pi
    circle = (p*(r**2))*3 #circle area
    area_result = square - 4*circle#answer
    print("%.2f"%(area_result))

def main():
    n = int(input())
    fncal_shade_area(n)


if __name__ == '__main__':
    main()