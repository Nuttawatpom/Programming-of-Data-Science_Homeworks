#630510619 
#nuttawat khamwangsawat

def multiple_mn(m,n):
    top = []
    body = []
    ans = []
    for i in range (0,n):
        top.append(1)
    for i in range (0,n):
        if i == 0:
            body.append(1)
        elif i == n-1:
            body.append(1)
        else:
            body.append(0)
    for i in range(0, m):
        if i == 0:
            ans.append(top)
        elif i == m - 1:
            ans.append(top)
        else:
            ans.append(body)
    return ans

def main():
    m = int(input(""))
    n = int(input(""))
    result = multiple_mn(m,n)
    print(result)

if __name__ == '__main__':
    main()