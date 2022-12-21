#630510619 
#nuttawat khamwangsawat
#Lab06_3

def replace_string(str_input,str_check,str_replace):
    if len(str_check) == len(str_check):
        for i in range(len(str_input)):
            for j in range(len(str_check)):
                if str_input[i] == str_check[j]:
                    str_input = str_input.replace(str_input[i], str_replace[j])
        return str_input

def main():
    str_input = input("Enter str: ")
    str_check = input()
    str_replace = input()
    replace_string(str_input,str_check,str_replace)

if __name__ == '__main__':
    main()