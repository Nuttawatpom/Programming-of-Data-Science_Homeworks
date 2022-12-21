#630510619 
#nuttawat khamwangsawat
#Lab02_1

def show_sharp_star(i,j):
    print("#"*i,"*"*j)

def draw_square(n):
    a = n*2
    b = n//2
    show_sharp_star(a - b,b)
    show_sharp_star(n,n)
    show_sharp_star(0,a)
    show_sharp_star(n,n)
    show_sharp_star(a - b,b)
    
def main():
    n= int(input())
    draw_square(n)


if __name__ == '__main__':
    main()