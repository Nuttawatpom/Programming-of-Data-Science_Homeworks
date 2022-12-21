#630510619 
#nuttawat khamwangsawat
#Lab07_4

def replace_sorting(list_input,item):
    list_answer = []
    for i in list_input:
        if i == item:
            list_answer.append(0)
        else:
            list_answer.append(i)
    list_answer.sort()
    return list_answer

def main():
    list_input = [1,3, 5, 7, 10]
    item = int(input("Enter item: "))
    answer = replace_sorting(list_input,item)
    print(replace_sorting(list_input,item))

if __name__ == '__main__':
    main()