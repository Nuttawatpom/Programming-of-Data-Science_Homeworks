#630510619 
#nuttawat khamwangsawat
#Lab04_5

def triangle(n):
    space = n - 1
    star = 1
    for i in range(n):
        print(" "*space + "*"*star)
        space -= 1
        star += 2
        
def main():
    n = int(input("Enter star number: ")) #รับข้อมูลนําเข้า (input)
    triangle(n)

if __name__ == '__main__':
    main()