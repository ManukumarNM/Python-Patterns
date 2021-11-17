'''
Date:17/11/2021
Author: MANUKUMAR N M
Language: Python 
Pattern Programs
'''
####################################################################################################

#print below pattern 
'''
      *
      * *
      * * *
      * * * *
      * * * * *
'''
#Method-1
'''
def pattern(rows):
    for col in range(rows):
        print(" "*(rows)+" *"*(col+1))
    
pattern(5)
'''

'''
#Method-2
rows = int(input("Enter a number of rows:"))
for row in range(rows):
    for col in range(row+1):
        print("*", end=" ")
    print()
'''

############################################################################################

#print below pattern
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

'''
#Method-1
def pattern1(rows):
    for col in range(rows+1,0,-1):
        print(" "*(rows)+" *"*(col-1))
        
pattern1(5)
'''


'''
#Method-2
rows = int(input("Enter a number of rows:"))
for row in range(rows+1,0,-1):
    for col in range(row-1):
        print("*", end=" ")
    print()
'''

#############################################################################################

#print below pattern
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
'''
rows = int(input("Enter a number of rows:"))
for row in range(rows):
    for col in range(row+1):
        print("*", end=" ")
    print()
for row in range(rows-1,0,-1):
    for col in range(1,row+1):
        print("*", end=" ")
    print()
'''
############################################################################################

#print below pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

'''
rows =  int(input("Enter a number of rows:"))
for row in range(1, rows+1):
    for col in range(1, row+1):
        print(row, end=" ")
    print()
'''
#########################################################################################

#print below pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

'''
rows =  int(input("Enter a number of rows:"))
for row in range(1,rows+1):
    for col in range(1,row+1):
        print(col, end=" ")
    print()
'''
################################################################################################

#print below pattern
'''
11 
21 22 
31 32 33 
41 42 43 44 
51 52 53 54 55 
'''

'''
rows =  int(input("Enter a number of rows:"))
for row in range(1,rows+1):
    for col in range(1,row+1):
        print("{0}{1}".format(row,col), end=" ")
    print()
'''

###########################################################################################

#print below pattern
'''
@ 
@ @ 
@ @ @ 
@ @ @ @ 
@ @ @ @ @ 
'''
'''
rows =  int(input("Enter a number of rows:"))
ch = 64
for row in range(1,rows+1):
    for col in range(1,row+1):
        print("{0}".format(chr(ch)), end=" ")
    print()
'''

#########################################################################################

#print below pattern
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''

'''
rows =  int(input("Enter a number of rows:"))
ch = 64
for row in range(1,rows+1):
    for col in range(1,row+1):
        ch = ch + 1
        print("{0}".format(chr(ch)), end=" ")
    print()
'''
###########################################################################################

#print below pattern

'''
A 
A B 
A B C 
A B C D 
A B C D E
'''
'''
rows =  int(input("Enter a number of rows:"))
ch = 64
for row in range(1,rows+1):
    for col in range(1,row+1):
        print("{0}".format(chr(ch+col)), end=" ")
    print()
'''

##########################################################################################

#print below pattern

'''
11 
12 13 
14 15 16 
17 18 19 20 
21 22 23 24 25 
'''
rows =  int(input("Enter a number of rows:"))
var = 10
for row in range(1,rows+1):
    for col in range(1,row+1):
        var = var+1
        print("{0}".format(var), end=" ")
    print()
    
############################################################################################
