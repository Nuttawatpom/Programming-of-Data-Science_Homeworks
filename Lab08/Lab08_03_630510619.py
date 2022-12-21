#630510619 
#nuttawat khamwangsawat
#Lab08_3

import copy

def remove_row_col(list_a, row, col):
    list_x = copy.deepcopy(list_a)
    del list_x[row]
    for i in range(len(list_x)):
        del list_x[i][col]
    return list_x

def main():
    list_a = [[2, 3, 4, 5], [8, 7, 6, 5], [0, 1, 2, 3]]
    row = int(input())
    col = int(input())
    answer = remove_row_col(list_a, row, col)
    print(answer)

if __name__ == '__main__':
    main()