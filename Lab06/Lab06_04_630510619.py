#630510619 
#nuttawat khamwangsawat
#Lab06_4

def new_string(name1, name2, name3, name4, name5):
    string1 = name1[0:2] + "_" + name2[0:2] +  "_" + name3[0:2] +  "_" +  name4[0:2] +  "_" + name5[0:2]
    string2 = name1[-1:-3:-1] + "/" + name2[-1:-3:-1] +  "/" + name3[-1:-3:-1] +  "/" +  name4[-1:-3:-1] +  "/" + name5[-1:-3:-1]
    string3 = name1[0] + name1[-1] + "*"+ name2[0] + name2[-1] +  "*" +  name3[0] + name3[-1] +  "*" + name4[0] + name4[-1] +  "*" +  name5[0] + name5[-1] 
    return string1,string2,string3

def main():
    name = input("Enter str: ").split(",")
    print(new_string(name[0], name[1], name[2], name[3], name[4]))

if __name__ == '__main__':
    main()