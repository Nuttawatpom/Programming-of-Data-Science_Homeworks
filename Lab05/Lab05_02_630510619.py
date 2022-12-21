#630510619 
#nuttawat khamwangsawat
#Lab05_2

def print_triangle(n, type):
    if type == 'U' and n > 0:
        for i in range(1,n+1):
            for j in range(i):
                print(j+1,end = '')
            print()
    elif type == 'U' and n <= 0:
        n *= -1
        sum  = n
        for i in range(1,n+1):
            for j in range(i):
                print(sum,end = '')
                sum -= 1
            print()
            sum = n
    elif type == 'D' and n > 0:
        sum  = n
        for i in range(1,n+1):
            for j in range(1,sum+1):
                print(j, end = '')
            print()
            sum -= 1
    elif type == 'D' and n <= 0:
        n *= -1
        sum  = n
        num = n
        for i in range(1,n+1):
            for j in range(1, sum+1):
                print(num, end = '')
                num -= 1
            print()
            num = n - i
            sum -= 1

def main():
    n = int(input("Enter n: "))
    type = input("Enter U or D : ")
    print_triangle(n, type)

if __name__ == '__main__':
    main()