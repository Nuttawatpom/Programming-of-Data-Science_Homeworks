#630510619 
#nuttawat khamwangsawat
#Lab02_4

def square_area(a):
    a = float(a)
    sq_value = a * a#พื้นที่ 4 เหลี่ยม
    return sq_value

def triangle_area(a,b):
    a = float(a)
    b = float(b)
    t_value = (a/4)*(4*(b**2) - (a**2))**0.5
    return t_value

def  fncal_shaded_area(a, b):
    square_area(a)
    triangle_area(a,b)
    anwer = square_area(a) - triangle_area(a, b)
    print("%.2f %.2f"%(triangle_area(a,b),anwer))

def main():
   a, b = input().split(",")
   fncal_shaded_area(a, b)

if __name__ == '__main__':
    main()