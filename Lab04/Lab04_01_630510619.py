#630510619 
#nuttawat khamwangsawat
#Lab04_1

def sequence_number(n):
    for k in range(n):
        result = (2*k)+1
        print(result,end=" ")

def main():
    n = int(input("Enter n: ")) #รับข้อมูลนําเข้า (input)
    sequence_number(n)

if __name__ == '__main__':
    main()