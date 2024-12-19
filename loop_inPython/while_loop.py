#WAP to print 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#---------------------------------------------------------------------------------------------------

#WAP to print 10 to 1
i=10
while i>=1:
    print(i)
    i-=1

#---------------------------------------------------------------------------------------------------

#WAP print the table of n number

num=(int(input("Enter Number :")))
i=1

while i<=10:
    print(num,"*",i,"=",(num*i))
    i+=1

#---------------------------------------------------------------------------------------------------

#WAP to print the following list
#[1,4,9,16,25,36,49,64,81,100]

l= [1,4,9,16,25,36,49,64,81,100]
i=0
while i<=(len(l)-1):
    print(l[i])
    i+=1
'''
Output :-
1
4
9
16
25
36
49
64
81
100
'''

#---------------------------------------------------------------------------------------------------


#search a number x from the tuple (1,4,2,5,6)
t=(1,4,2,5,6)
num=int(input("Enter number to find:"))
i=0
while i <= (len(t)-1):
    if(num==t[i]):
        print("Number found at indx :",t[i])
    else:
        print("finding...")
    i+=1