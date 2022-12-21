#630510619 
#nuttawat khamwangsawat
#Lab05_1

def multiple_table(n):
    if n <= 12:
        for i in range(1,n+1):
            for j in range(1,n+1):
                print("%4d"%(j*i),end=" ")
            print("")

    else:
        print("Invalid Input")

def main():
    n = int(input())
    multiple_table(n)

if __name__ == '__main__':
    main()