#630510619 
#nuttawat khamwangsawat
#Lab06_2

def create_new_string(n,my_str):   #ฟังก์ชันสร้างสตริงใหม่
    len_old_str = len(my_str)
    comma_ct= my_str.count(",")#นับจ านวน comma ในสตริงที่รับเข้า
    my_str_ct= comma_ct+ 1

    if(my_str_ct< n):
        temp_str = "meaw meaw cat song".upper()
        m = 0
        for k in range(my_str_ct,n):
            new_str = temp_str[m:m+2]
            my_str = my_str + "," + new_str
            m =  m + 2

    elif(my_str_ct> n):
        my_str = my_str.upper()
        comma = my_str_ct
        k = 0
        temp_str = ''
        while comma != n:
            if my_str[k] == ',':
                comma -= 1
                k += 1
            else:
                temp_str += my_str[k]
                k += 1
        my_str = temp_str + my_str[k::]

    else:
        my_str = my_str.lower()
        temp_str = my_str[-1::-1]
        my_str = temp_str

    len_new_str= len(my_str)
    return len_old_str,my_str,len_new_str

def main():
    n_str= int(input("Enter n: "))#รับข้อมูลน าเข้า
    input_str= input("Enter str: ")
    new_str= (create_new_string(n_str, input_str))     #เรียกใช้ฟังก์ชันเพื่อท างานตามโจทย์ก าหนด
    print(new_str[0])
    print(new_str[1])
    print(new_str[2])
    
if __name__ == '__main__':
    main()