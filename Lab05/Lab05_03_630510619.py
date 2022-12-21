#630510619 
#nuttawat khamwangsawat
#Lab05_3
def divide_3or7(m,n):
    m = int(m)
    n = int(n)
    max = 0
    count_3 = 0
    count_7 = 0
    last_number = 0
    for i in range(m, n+1):
        if i % 3 == 0 or i % 7 == 0:
            max = i
            if max >= last_number:
                last_number = max
        if i % 3 == 0:
            count_3 += 1
        if i % 7 == 0:
            count_7 += 1
    if last_number == 0:
        last_number = None
    return (last_number, count_3, count_7)

def main():
    m, n = input("Enter m n: ").split(" ")
    print(divide_3or7(m,n))

if __name__ == '__main__':
    main()