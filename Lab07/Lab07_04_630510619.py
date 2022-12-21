#630510619 
#nuttawat khamwangsawat
#Lab07_4

def reverse_list_number(m,n):
    m = int(m)
    n = int(n) - 1 
    list_answer = []
    for i in range(m,n,-2):
        list_answer.append(i)
    return list_answer

def main():
    m, n = input("Enter m, n: ").split(",")
    answer = reverse_list_number(m,n)
    print(answer)

if __name__ == '__main__':
    main()