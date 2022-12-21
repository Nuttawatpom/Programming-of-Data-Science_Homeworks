#630510619 
#nuttawat khamwangsawat
#Lab09_4

def bmi_reports(stu_list):
    value = {'Normal' : [],'Over' : [],'Under' : [],'Obesity' : []}
    check = ["Over","Normal","Under","Obesity"]
    for i in stu_list:
        bmi = (i[3]/((i[2])**2))
        bmi = round(bmi, 1)
        if  25<= bmi < 30 :
            value['Over'].append([i[0], bmi])
        elif 18.5<= bmi < 25:
            value['Normal'].append([i[0], bmi])
        elif bmi < 18.5:
            value['Under'].append([i[0], bmi])
        elif bmi >= 30:
            value['Obesity'].append([i[0], bmi])
    for i in check:
        if value[i] == []:
            value.pop(i)
    return value
    

def main():
    stu_list = [['6101001', 'Female', 1.38, 50.9],['6102002', 'Male', 1.48, 60.2],['6204222', 'Male', 1.55, 45.75]]
    result = bmi_reports(stu_list)
    print(result)

if __name__=="__main__":
    main()