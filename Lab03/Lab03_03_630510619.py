#630510619 
#nuttawat khamwangsawat
#Lab03_3

def credit_balance(price, n, money):
    paid = price * n
    print("%.1f*%d=%.1f"%(price, n, paid))
    if money >= paid:
        answer = money - paid
        print(("%.1f")%answer)
    else:
        print("Not enough money")

def main():
    price = float(input("Enter price = "))
    n = int(input("Enter n = "))
    money = int(input("Enter money = "))
    credit_balance(price, n, money)# เรียกใช้ฟังก์ชัน credit_balance()

if __name__ == '__main__':
    main()