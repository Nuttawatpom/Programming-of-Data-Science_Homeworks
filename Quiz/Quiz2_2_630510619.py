#630510619 
#nuttawat khamwangsawat

def pair_request(list_input, sum):
    ans = []
    for i in range (len(list_input)):
        for j in range (i+1,len(list_input)):
            if list_input[i] + list_input[j] == sum:
                ans.append([list_input[i],list_input[j]])
    return ans

def main():
    list_input = [1, 9, 5, 7, 10, 3]
    sum = 20
    result = pair_request(list_input, sum)
    print(pair_request(list_input, sum))

if __name__ == '__main__':
    main()