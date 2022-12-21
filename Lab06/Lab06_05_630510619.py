#630510619 
#nuttawat khamwangsawat
#Lab06_5

import string

def check_palindrome(text):
    text = text.lower()
    temp_text = ""
    for i in range(len(text)):
        if text[i] not in string.punctuation and text[i] not in string.whitespace:
            temp_text += text[i]
    text = temp_text
    if text == text[-1::-1]:
        return True
    else:
        return False

def main():
    text = input("Enter str: ")
    print(check_palindrome(text))

if __name__ == '__main__':
    main()