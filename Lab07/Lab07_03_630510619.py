#630510619 
#nuttawat khamwangsawat
#Lab07_3

def list_number(n):
    limit = n*2
    list_answer = []

    for i in range(1,limit,2):
        list_answer.append(i)
    return list_answer
    
def main():
    n = int(input("Enter n: "))
    answer = list_number(n)
    print(answer)

if __name__ == '__main__':
    main()