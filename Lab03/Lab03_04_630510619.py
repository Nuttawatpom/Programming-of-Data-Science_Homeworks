#630510619 
#nuttawat khamwangsawat
#Lab03_4

def cal_bmi(w,h):
    check_h = h * 30.48
    if check_h < 300:
        h = h * 12
        BMI = (w/(h*h))*703
        print(("%.1f")%BMI)
    else:
        h = h/100
        BMI = (w/(h*h))
        print(("%.1f")%BMI)

def main():
    weight= float(input())
    height= float(input()) 
    cal_bmi(weight,height)# เรียกใช้ฟังก์ชัน cal_bmi()

if __name__ == '__main__':
    main()