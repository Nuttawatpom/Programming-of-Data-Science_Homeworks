#630510619 
#nuttawat khamwangsawat
#Lab08_4

def multiple_list(n):
    num = 0
    if n < 12:
        list_result = make_2d_list(n, n)
        for i in range(0,n):
            for j in range(0,n):
                num += 1
                result = num*(i+1)
                list_result[i][j] = result
            num = 0
        return list_result
    else:
        return("Invalid Input")

def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a

def main():
    n = int(input("Enter n: "))
    list_result = multiple_list(n)
    print(list_result)

if __name__=="__main__":
    main()