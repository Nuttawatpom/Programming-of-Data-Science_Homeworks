#630510619 
#nuttawat khamwangsawat
#Lab03_1

def divide_3and5(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Both"
    elif n % 5 == 0:
        return "Five"
    elif n % 3 == 0:
        return "Three"
    else:
        return "None"

def main():
    number = int(input("Enter number: "))# รับค่าและแปลงเป็นค่าตัวเลข
    result = divide_3and5(number)# เรียกใช้ฟังก์ชัน divide_3and5()# และสร้างตัวแปร resultมารับค่าที่คืนมา
    print(result)# เอาตัวแปร resultมาแสดงผล

if __name__ == '__main__':
    main()