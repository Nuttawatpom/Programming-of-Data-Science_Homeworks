#630510619 
#nuttawat khamwangsawat
#Lab04_2

def reverse_sequence_number(m,n):
    m = int(m)
    n = int(n)
    for k in range(m, n-1, -2):
        print(k,end=" ")

def  main():
    m, n = input("Enter m, n: ").split(",")
    reverse_sequence_number(m,n)

if __name__ == '__main__':
    main()