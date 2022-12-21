#630510619 
#nuttawat khamwangsawat
#Lab07_2

def sum_number(list_x):
    list_int = []
    for i in list_x:
        if isinstance(i, int):
            list_int.append(i)
        elif isinstance(i, float):
            list_int.append(i)
    return sum(list_int)

def main():
    list_x = [10, 'hello', 23.5, 4]
    print(sum_number(list_x))

if __name__ == '__main__':
    main()