#630510619 
#nuttawat khamwangsawat

def leap_years(y, m):
    leapyear = 0
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                leapyear += 1
                print("Leap Year")
            else:
                print("Non Leap Year")
        else:#หาร 4 ลงตัว
            leapyear += 1
            print("Leap Year")
    else:
        print("Non Leap Year")
        

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print("31")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("30")
    elif m == 2:
        if leapyear > 0:
            print("29")
        else:
            print("28")
        
def main():
    y = int(input())
    m = int(input())
    leap_years(y, m)

if __name__ == '__main__':
    main()