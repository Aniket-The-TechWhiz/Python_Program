# if - elif - else Statement
# Conditonal Satement
'''
m>=90 grade A
90 >m >80 grade B
80 > m >70 grade c
70 > m grade D
'''

'''
output :
Enter a marks out of 100 :91
A grade
'''

m =int (input("Enter a marks out of 100 :"))
if(m>=90):
    print("A grade")
elif(m<90 and m>=80):
    print("B grade")
elif(m<80 and m>=70):
    print("C grade")
elif(m<70 ):
    print("D grade")
