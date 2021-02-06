##traingle pyramid
#rows=int(input("Enter No of Rows: "))
#k=2*rows-2
#for i in range(0,rows):
#    for j in range(0,k):
#        print(end=" ")
#    k=k-2
#    for j in range (0,i+1):
#        print("*",end=" ")
#    print("")


##simple Triangle
#rows=int(input("Enter No of Rows: "))
#for i in range (0,rows):
#    for j in range(i+1):
#        print("*",end="")
#    print()

#Daimond Shape 
#rows=int(input("Enter No of Rows: "))
#
#k=2*rows-2
#for i in range(0,rows):
#    for j in range(0,k):
#        print(end=" ")
#        
#    k=k-1
#    
#    
#    for j in range (0,i+1):
#        print("* ",end="")
#    print("")
#k=rows-1
#for i in range(k+1,-1,-1):
#    for j in range(k,0,-1):
#        print(end=" ")
#        
#    k=k+1
#    for j in range (0,i):
#        print("* ",end="")
#    print("")

##Downword Triangle pyramid
#rows=int(input("Enter No of Rows: "))
#k=2*rows-2
#for i in range(k,0,-1):
#    for j in range(k-i):
#        print(end=" ")
#    
#    k=k-2
#    for j in range (0,i-1):
#        print("* ",end="")
#    print("")
#    
#
##
#
# Two pyramid in single Pattern    
#rows=int(input("Enter No of Rows: "))
#for i in range (0,rows):
#    for j in range(i+1):
#        print("*",end="")
#    print()
#    
#for i in range(rows,0,-1):
#    for j in range(i-1):
#        print("*",end="")
#    
#    print()

##Hour glass Pattern 
rows=int(input("Enter No of Rows: "))
k=rows-2
for i in range (rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
        
    k=k+1
    for j in range(0,i+1):
        print("* ",end="")
    print()
        
 
k=2*rows-2
for i in range(0,rows+1):
    for j in range(0,k):
        print(end=" ")
        
    k=k-1
    
    
    for j in range (0,i+1):
        print("* ",end="")
    print("")