#630510619 
#nuttawat khamwangsawat
#Lab03_5

def cal_bmi(w,h):
    check_h = h * 30.48
    if check_h < 300:
        h = h * 12#chang hight to inch
        BMI = (w/(h*h))*703#equation cal bmi
        return BMI
    else:
        h = h/100#chang hight to m
        BMI = (w/(h*h))#equation cal bmi
        return BMI

def bmi_guide(bmi):
    if bmi < 18.5:
        print(("%.1f")%bmi)
        print("underweight")
    elif bmi < 22.9:
        print(("%.1f")%bmi)
        print("normal") 
    elif bmi < 24.9:
        print(("%.1f")%bmi)
        print("overweight")
    elif bmi < 29.9:
        print(("%.1f")%bmi)
        print("obese")
    else:
        print(("%.1f")%bmi)
        print("severely obese")

def main():
    weight= float(input())
    height= float(input()) 
    bmi = cal_bmi(weight,height)# เรียกใช้ฟังก์ชัน cal_bmi()
    bmi_guide(bmi)# เรียกใช้ฟังก์ชัน bmi_guide()

if __name__ == '__main__':
    main()