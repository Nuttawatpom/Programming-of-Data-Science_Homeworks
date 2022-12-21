#630510619 
#nuttawat khamwangsawat
#Lab02_2

def show_sharp_star(ch1,  ch2, i, j):
    print(ch1*i+ch2*j)

def draw_square(n, ch1, ch2):
    a = n*2
    b = n//2
    show_sharp_star(ch1, ch2,a - b,b)
    show_sharp_star(ch1, ch2,n,n)
    show_sharp_star(ch1, ch2,0,a)
    show_sharp_star(ch1, ch2,n,n)
    show_sharp_star(ch1, ch2,a - b,b)
    
def main():
    n = int(input())
    ch1 = str(input())
    ch2 = str(input())
    draw_square(n, ch1, ch2)

if __name__ == '__main__':
    main()