#630510619 
#nuttawat khamwangsawat
#Lab01_3

def fncal_bmi(w, h):
    w = w/2.2 #change unit weight 
    h = (h*30.48)/100 #change unit hight 
    bmi = w/(h*h)#find bmi
    print("%.2f"%(bmi))#result and display show

def main():
    w = int(input())
    h = int(input())
    fncal_bmi(w, h)

if __name__ == '__main__':
    main()