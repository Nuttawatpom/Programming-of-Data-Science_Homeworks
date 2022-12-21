#630510619 
#nuttawat khamwangsawat
#Lab03_2

def wavelength(w):
    if 380 <= w < 450:
        return "Violet"
    elif 450 <= w < 495:
        return "Blue"
    elif 495 <= w < 570:
        return "Green"
    elif 570 <= w < 590:
        return "Yellow"
    elif 590 <= w < 620:
        return "Orange"
    elif 620 <= w < 750:
        return "Red"
    else:
        return "Invalid Input"

def main():
    wl_input= input("Enter wavelength: ")# รับค่าinput จาก Keyboard
    wl = int(wl_input)#แปลงเค่าที่ได้จาก keyboard ป็นค่าตัวเลข
    result = wavelength(wl)# สร้างตัวแปรresultมารับค่าที่คืนมาจากการเรียกใช้ฟังก์ชันwavelength()
    print(result)# เอาตัวแปร resultมาแสดงผลแบบที่2

if __name__ == '__main__':
    main()