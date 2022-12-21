#630510619 
#nuttawat khamwangsawat
#Lab06_1

def replace_string(input_str):            #ฟังก์ชันสร้างสตริงใหม่
    check= "AEIOU"
    replace="@#$&*"

    for i in range(len(input_str)):
        input_str= input_str.upper()
        if input_str[i] == 'A':
            input_str = input_str.replace('A', '@')
        elif input_str[i] == 'E':
            input_str = input_str.replace('E', '#')
        elif input_str[i] == 'I':
            input_str = input_str.replace('I', '$')
        elif input_str[i] == 'O':
            input_str = input_str.replace('O', '&')
        elif input_str[i] == 'U':
            input_str = input_str.replace('U', '*')
        elif input_str[i] == '0':
            input_str = input_str.replace('0', '0')
        elif input_str[i] == '1':
            input_str = input_str.replace('1', '0')
        elif input_str[i] == '2':
            input_str = input_str.replace('2', '0')
        elif input_str[i] == '3':
            input_str = input_str.replace('3', '0')
        elif input_str[i] == '4':
            input_str = input_str.replace('4', '0')
        elif input_str[i] == '5':
            input_str = input_str.replace('5', '0')
        elif input_str[i] == '6':
            input_str = input_str.replace('6', '0')
        elif input_str[i] == '7':
            input_str = input_str.replace('7', '0')
        elif input_str[i] == '8':
            input_str = input_str.replace('8', '0')
        elif input_str[i] == '9':
            input_str = input_str.replace('9', '0')                                     
    return input_str

def main():
    input_str= input("Enter str: ")        #รับข้อมูลนำเข้า(input) เป็นข้อความ
    new_str= replace_string(input_str)     #เรียกใช้ฟังก์ชันเพื่อท างานตามโจทย์กาหนด
    print(new_str)

if __name__ == '__main__':
    main()