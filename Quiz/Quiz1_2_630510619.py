#630510619 
#nuttawat khamwangsawat

def shows_series(a, b):
    if a > 0 and b > 0:
        if a < b:
            for i in range(a,b+1):
                print(i)
                i += 1
        elif a > b:
            for i in range(a, b-1, -1):
                print(i)
        else:
            print(0)
    else:
        print(0)

def main():
    a = int(input())
    b = int(input())
    shows_series(a, b) 

if __name__ == '__main__':
    main()