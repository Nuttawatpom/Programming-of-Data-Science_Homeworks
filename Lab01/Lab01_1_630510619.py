#630510619 
#nuttawat khamwangsawat
#Lab01_1

def fncal_area(n):
    square = n * n #square area
    r = n/4 #radius
    p = 3.141593 #pi
    circle = p*(r**2) #circle area
    area_result = square - 4*circle#answer
    print("%.2f\n%.2f\n%.2f"%(square,circle,area_result))

def main():
    n = int(input())
    fncal_area(n)


if __name__ == '__main__':
    main()