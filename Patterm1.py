def pattern1(rows):
    i=1;
    for i in range(int(rows)+1):
        print(str(i)*i)

def pattern2(rows):
    x=1;
    for i in range(x,int(rows)+1):
        j=1
        for j in range(x,i+1):
            print(j,end="")
        print("\r")

def pattern3(rows):
    x=1;
    for i in range(x,(int(rows))*2,2):
        j=1
        for j in range(x,i+1,2):
            print(j,end="")
        print("\r")        

def pattern4(rows):
    x=1;
    for i in range(x,int(rows)+1):
        j=1
        for j in range(x,i+1):
            if j%2==0:
                print('1',end="")
            else:
                print('0',end="")
        print("\r") 



rows=input("Enter the number of rows:")
pattern1(rows)
pattern2(rows)
pattern3(rows)
pattern4(rows)