#MAGIC SQUARE
#POSITION OF 1 = (N/2,N-1) = (3/2,3-1)=(1,2)
#POSITION OF 2 = (1-1,2+1) = (0,3)=(0,0) TAKING PREVIOUS MATRIX
#POSITION OF 3 = (0-1,0+1) = (3-1,1)=(2,1)
#POSITION OF 4 = (2-1,2+1) = (1,2) SINCE 1 IS PRESENT APPLY 2ND CONDITION = (1+1,2-2)=(2,0)
#WHICH IS INCREMENT ROW BY 1 AND DECREMENT COLUMN BY 2
#POSITION OF 5 = (1,1)
#POSITION OF 6 = (0,2)
#POSITION OF 7 = (0-1,2+1)=(-1,3)
#USE CONDITION 3 = (0,1) WHICH IS IF ANYTIME ROW BECOME -1 AND COLUMN BECOE N,SWITCH IT TO (0,N-2)
#POSITION OF 8 = (2,2)
#POSITION OF 9 = (1,0)

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    # for i in range(n):
    #     for j in range(n):
    #         print(magicSquare[i][j],end=" ")
    #     print()
        
    i = n//2
    j = n-1
    num = n*n
    count = 1

    while(count<=num):
        if(i==-1 and j==n): #condition 4
            j=n-2
            i=0
        else:
            if(j==n): #column value is exceeding
                j=0
            if(i<0): #row is becoming -1
                i=n-1

        if (magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        i=i-1
        j=j+1   #condition 1

    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    print("The sum of each row/column/diagonal is: "+str(n*(n**2+1)/2))

magic_square(7)
        