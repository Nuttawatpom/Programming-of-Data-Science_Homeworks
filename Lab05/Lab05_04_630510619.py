#630510619 
#nuttawat khamwangsawat
#Lab05_4
import math

def count_prime(m,n):
    num = 2
    x = 0
    answer = 0
    index = 0
    m = int(m)
    n = int (n)
    if m < n:
        m = m
        n = n
    elif m > n:
        x += m
        m = n
        n = x

    for i in range(m, n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                index += 1
                break
        if index == 0 :
            answer += 1
        index = 0
    return answer

def main():
    m, n = input("Enter m n: ").split(" ")
    print(count_prime(m,n))

if __name__ == '__main__':
    main()