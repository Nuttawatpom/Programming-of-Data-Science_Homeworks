#630510619 
#nuttawat khamwangsawat
#Lab01_4

def to_seconds(d, h, m, s):
    d = int (d)#change srting to int
    h = int (h)#change srting to int
    m = int(m)#change srting to int
    s = int(s)#change srting to int
    h = h + (d * 24)#hours add Day change to hours
    m = m + (h * 60)#minute add hours change to minute
    s = s + (m * 60)#second add minute change to second
    print(s)#result

def main():
    d, h, m, s = input().split(",")
    to_seconds(d, h, m, s)

if __name__ == '__main__':
    main()