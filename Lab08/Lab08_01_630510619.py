#630510619 
#nuttawat khamwangsawat
#Lab08_1

def classify_lists_result(list_x):
    list_a = []
    list_b = []
    list_c = []

    for i in list_x:
        if isinstance(i, int):
            list_a.append(i)
        if isinstance(i, float):
            list_b.append(i)
        if isinstance(i, str):
            list_c.append(i)
    avg = sum(list_b)/len(list_b)
    list_c.sort(key=lambda x: x.upper())
    return sum(list_a),avg,list_c

def main():
    list_x = ['Python', -23, 40, 500,45,33.45,65545,'az',1.1,'za']
    list_result = classify_lists_result(list_x)
    print(list_result[0])
    print("%.3f"%(list_result[1]))
    print(list_result[2])

if __name__ == '__main__':
    main()