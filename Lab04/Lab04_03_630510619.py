#630510619 
#nuttawat khamwangsawat
#Lab04_3

def prime_factorization(x):
    num = 2
    while True:
        if x % num == 0:
            print(num)
            x /= num
        else:
            num += 1
        if num > x :
            break
        
def main():
    x = int(input()) #รับข้อมูลนําเข้า (input)
    prime_factorization(x)

if __name__ == '__main__':
    main()