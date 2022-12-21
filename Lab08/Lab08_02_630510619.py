#630510619 
#nuttawat khamwangsawat
#Lab08_2

def avg_number_row(list_x):
    list_backup = []
    list_sum = []
    for i in range(len(list_x)):
        for j in list_x[i]:
            if isinstance(j, int):
                list_sum.append(j)
            elif isinstance(j, float):
                list_sum.append(j)
        list_backup.append(sum(list_sum)/len(list_sum))
        list_sum = []
    return list_backup        

def main():
    list_x = [[10, 'hello', 23.5, 4],[40.0, 20.5, 30, 'world', 'I am Happy']]
    answer = avg_number_row(list_x)
    print("[%.2f, %.2f]"%(answer[0],answer[1]))

if __name__ == '__main__':
    main()