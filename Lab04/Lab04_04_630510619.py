#630510619 
#nuttawat khamwangsawat
#Lab04_4

def xy_factors(x, y, n):
    index = 0
    for i in range(1,n+1):
        if i % x == 0:
            index += 1
        elif i % y == 0:
            index += 1
    return index

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    n = int(input("Enter n: "))
    print(xy_factors(x, y, n))

if __name__ == '__main__':
    main()