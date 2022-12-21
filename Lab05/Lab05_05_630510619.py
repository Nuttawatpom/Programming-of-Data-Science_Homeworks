#630510619 
#nuttawat khamwangsawat
#Lab05_5

def show_space_star(i,j):
    print(" "*i,end="")
    print(" "*i,"* "*j,sep = "",end = "\n")

def triangle_tree(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            show_space_star(n-j,j*2-1)
def main():
    n = int(input("Enter star number: "))
    triangle_tree(n)
    
if __name__ == '__main__':
    main()