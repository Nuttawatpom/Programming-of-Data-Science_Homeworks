#630510619 
#nuttawat khamwangsawat
#Lab02_5

def net_price(price1, price2, price3):
    a = cal_price(price1, 5)
    b = cal_price(price2, 10)
    c = cal_price(price3, 20)
    total = a + b + c
    print("%.2f %.2f %.2f %.2f"%(a, b, c, total))

def cal_price(price, discount):
    price = price - ((price/100)*discount)
    answer = price + (price/100)*7
    return answer

def main():
    price1 = int(input())
    price2 = int(input())
    price3 = int(input())
    net_price(price1, price2, price3)

if __name__ == '__main__':
    main()