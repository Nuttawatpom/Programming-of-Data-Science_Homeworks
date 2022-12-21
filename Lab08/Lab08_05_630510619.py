#630510619 
#nuttawat khamwangsawat
#Lab08_5

def  pretty_print_list(list_a):
    row = len(list_a)
    col = len(list_a[0])
    length_list = []
    for i in range(row):
        for j in range(col):
            length_list.append(len(str(list_a[i][j])))
    
    max_length = max(length_list)

    max_l = "{0:>" + str(max_length) + "}"

    print("[", end='')
    for i in range(row):
        if i == 0:
            print("[", end='')
        else:
            print(" [", end='')
        for j in range(col):
            if j == col-1:
                print(max_l.format(list_a[i][j]),end='')
            else:
                print(max_l.format(list_a[i][j]),end=',')
        if i == row - 1:
            print("]", end='')
        else:
            print("],")
    print("]")

def main():
    list_a =  [[134, 2, 3], [4, 75, 6],[122, 3, 1233331234]]  
    pretty_print_list(list_a)

if __name__=="__main__":
    main()